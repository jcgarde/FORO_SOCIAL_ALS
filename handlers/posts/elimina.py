# coding: utf-8

import webapp2
import time

from webapp2_extras import jinja2

from model.post import Post

class EliminaPostHandler(webapp2.RequestHandler):
    def get(self):

        # Recuperamos el post para luego poder eliminarlo a través de su clave
        post = Post.recupera(self.request)
        post.key.delete()
        time.sleep(1)
        return self.redirect("/home")




app = webapp2.WSGIApplication([
    ('/posts/elimina', EliminaPostHandler)
], debug=True)

