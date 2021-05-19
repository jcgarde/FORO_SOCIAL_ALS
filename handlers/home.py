# coding: utf-8

import webapp2
from webapp2_extras import jinja2

from webapp2_extras.users import users

from model.usuario import Usuario

from model.post import Post

class HomeHandler(webapp2.RequestHandler):
    def post(self):
        usr = users.get_current_user()

        # Si se ha logeado alguien, creo dicho usuario y si no es la primera vez lo modifica.
        if usr:
            usuarios = Usuario.query()
            email = usr.email()
            usuario = Usuario(email=usr.email())
            usuario.put()

        posts = Post.query().order(Post.hora)

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "usuarios": usuarios,
            "posts": posts,
            "email": email
        }

        self.response.write(jinja.render_template("home.html", **valores_plantilla))

    def get(self):
        usr = users.get_current_user()

        usuarios = Usuario.query()

        # Ordenamos los posts de mas nuevos a mas viejos
        posts = Post.query().order(-Post.hora)

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "usuarios": usuarios,
            "posts": posts,
            "usr": usr,
            "nickname": usr.nickname()
        }

        self.response.write(jinja.render_template("home.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/home', HomeHandler)
], debug=True)
