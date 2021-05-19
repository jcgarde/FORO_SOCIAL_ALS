# coding: utf-8

import webapp2
import time

from webapp2_extras import jinja2

from model.post import Post

from webapp2_extras.users import users

class NuevoPostHandler(webapp2.RequestHandler):
    def get(self):


        usr = users.get_current_user()


        valores_plantilla = {
            "usr": usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevo_post.html", **valores_plantilla))

    def post(self):
        titulo = self.request.get("edTitulo", "")
        autor = self.request.get("edAutor", "")
        contenido = self.request.get("edContenido", "")

        if (not titulo
            or not autor or not contenido):
                return self.redirect("/home")
        else:
            post = Post(titulo=titulo, contenido=contenido, autor=autor)
            post.put()
            time.sleep(1)
            return self.redirect("/home")


app = webapp2.WSGIApplication([
    ('/posts/nuevo', NuevoPostHandler)
], debug=True)

