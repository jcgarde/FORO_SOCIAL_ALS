# coding: utf-8

import webapp2
import time

from model.comentario import Comentario

class EliminaComentarioHandler(webapp2.RequestHandler):
    def get(self):

        # Recuperamos comentario para poder eliminarlo a través de su clave
        comentario = Comentario.recupera(self.request)
        # Podemos obtener la clave del post correspondiente para luego redirigirnos a él
        clave_post = comentario.clave_post.urlsafe()
        comentario.key.delete()
        time.sleep(1)
        return self.redirect("/comentarios/ver?post="+clave_post)




app = webapp2.WSGIApplication([
    ('/comentarios/elimina', EliminaComentarioHandler)
], debug=True)