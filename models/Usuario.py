from google.appengine.ext import ndb

""" 
    Modelo de estruturação do objeto Usuario
"""
class Usuario(ndb.Model):
  id = ndb.StringProperty()
  nome = ndb.StringProperty()
  sobrenome = ndb.StringProperty()
  email = ndb.StringProperty()
  hashSenha = ndb.StringProperty()
  urlFoto = ndb.StringProperty()
  data = ndb.DateTimeProperty(auto_now_add=True)
