# coding: utf-8

from google.appengine.ext import ndb

# Clase que crea el usuario una vez se logea con el correo y almacenar todos los usuarios que se están conectando al foro
class Usuario(ndb.Model):
    email = ndb.StringProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()