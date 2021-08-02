 from google.appengine.ext import ndb

""" 
    Modelo de estruturação do objeto que armazena um token para um usuario logado
"""
class Login(ndb.Model):
  token = ndb.StringProperty()
  nome = ndb.StringProperty()
  sobrenome = ndb.StringProperty()
  email = ndb.StringProperty()
  urlFoto = ndb.StringProperty()
  data = ndb.DateTimeProperty(auto_now_add=True)
