
from google.appengine.ext import ndb

from post import Post

class Comentario(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True)
    autor = ndb.StringProperty(required=True)
    contenido = ndb.StringProperty(required=True)
    clave_post = ndb.KeyProperty(kind=Post)

    @staticmethod
    def recupera_post_comentarios(req):
        try:
            id_post = req.GET["post"]
        except KeyError:
            id_post = ""

        if id_post:
            clave_post = ndb.Key(urlsafe=id_post)
            comentarios = Comentario.query(Comentario.clave_post == clave_post)
            return (clave_post.get(), comentarios)
        else:
            print("Error: post no encontrado")

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()