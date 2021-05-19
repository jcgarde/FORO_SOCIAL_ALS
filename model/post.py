
from google.appengine.ext import ndb

class Post(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    contenido = ndb.StringProperty(required=True)
    autor = ndb.StringProperty(required=True)
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()