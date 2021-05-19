# coding: utf-8

import webapp2
import time

from webapp2_extras import jinja2
from webapp2_extras.users import users
from datetime import datetime

from model.comentario import Comentario

class ModificaComentarioHandler(webapp2.RequestHandler):
    def get(self):

        usr = users.get_current_user()

        comentario = Comentario.recupera(self.request)

        valores_plantilla = {
            "usr": usr,
            "comentario": comentario
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_comentario.html",
            **valores_plantilla))

    def post(self):
        autor = self.request.get("edAutor", "")
        contenido = self.request.get("edContenido", "")


        if (not autor
            or not contenido):
                return self.redirect("/home")
        else:
            comentario = Comentario.recupera(self.request)
            clave_post = comentario.clave_post.urlsafe()
            # Obtenemos la hora actual, si se modifica el comentario dicha hora debe ser actualizada
            hora = datetime.today()
            comentario.autor = autor
            comentario.contenido = contenido
            comentario.hora = hora
            # Modificamos comentario con los nuevos cambios
            comentario.put()
            time.sleep(1)
            return self.redirect("/comentarios/ver?post="+clave_post)


app = webapp2.WSGIApplication([
    ('/comentarios/modifica', ModificaComentarioHandler)
], debug=True)

