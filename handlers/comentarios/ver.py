# coding: utf-8

import webapp2
from webapp2_extras import jinja2

from model.comentario import Comentario

from webapp2_extras.users import users

class VerComentariosHandler(webapp2.RequestHandler):
    def get(self):
        post, comentarios = Comentario.recupera_post_comentarios(self.request)

        usr = users.get_current_user()

        # Ordenamos los comentarios de mas viejos a mas nuevos
        comentarios = Comentario.query().order(Comentario.hora)

        valores_plantilla = {
            "comentarios": comentarios,
            "post": post,
            "usr": usr,
            "clave_post": self.request.GET["post"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("ver-comentarios-post.html",
            **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/comentarios/ver', VerComentariosHandler)
], debug=True)
