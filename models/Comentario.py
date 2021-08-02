from google.appengine.ext import ndb

""" 
    Modelo de estruturação do objeto Comentario
""" 
class Comentario(ndb.Model):
  id = ndb.StringProperty()
  idlivro = ndb.StringProperty()
  usuario = ndb.StringProperty()
  conteudo = ndb.StringProperty()
  data = ndb.DateTimeProperty(auto_now_add=True)
