# coding: utf-8

import webapp2
from webapp2_extras import jinja2

from webapp2_extras.users import users

from model.usuario import Usuario

class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
        else:
            url_usr = users.create_login_url("/")

        usuarios = Usuario.query()

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "usr": usr,
            "usuarios": usuarios,
            "url_usr": url_usr
        }

        self.response.write(jinja.render_template("index.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
