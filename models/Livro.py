 from google.appengine.ext import ndb

""" 
    Modelo de estruturação do objeto Livro
"""
class Livro(ndb.Model):
  id = ndb.StringProperty()
  titulo = ndb.StringProperty()
  autores = ndb.StringProperty()
  desc = ndb.StringProperty()
  preco = ndb.StringProperty()
  urlCapa = ndb.StringProperty()
  data = ndb.DateTimeProperty(auto_now_add=True)
