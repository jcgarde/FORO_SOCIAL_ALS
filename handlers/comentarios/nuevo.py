# coding: utf-8

import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.ext import ndb
from webapp2_extras.users import users

from model.comentario import Comentario

class NuevoComentarioHandler(webapp2.RequestHandler):
    def get(self):

        usr = users.get_current_user()

        valores_plantilla = {
            "clave_post": self.request.GET["post"],
            "usr": usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_comentario.html",
            **valores_plantilla))

    def post(self):
        autor = self.request.get("edAutor", "")
        contenido = self.request.get("edContenido", "")
        clave_post = self.request.GET["post"]

        if (not autor
            or not contenido):
                return self.redirect("/home")
        else:
            comentario = Comentario(autor=autor,
                                contenido=contenido,
                                clave_post=ndb.Key(urlsafe=clave_post))
            comentario.put()
            time.sleep(1)
            return self.redirect("/comentarios/ver?post=" + clave_post)


app = webapp2.WSGIApplication([
    ('/comentarios/nuevo', NuevoComentarioHandler)
], debug=True)

