# -*- coding: utf-8 -*-

""" Main Aplicatin LivrariaJS

Arquivo principal que controla a aplicação contectando as interfaces cliente-servidor REST API
"""

import os
import json
from util import *
from datetime import datetime, timedelta

import webapp2
from google.appengine.ext.webapp import template 
from google.appengine.ext import ndb

from models.Usuario import *
from models.Login import *
from models.Livro import *
from models.Comentario import *

"""
Classe que carrega a interface de Documentação dos serviços diponíveis na REST API disponibilizada pela aplicação
"""

class RestApiPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'livrariaJS-REST-API.html') 
        self.response.out.write(template.render(path, {}))  

"""
Classe que carrega a interface cliente que permite utilizar os serviços
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html') 
        self.response.out.write(template.render(path, {}))    

class MyJsonEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, datetime):
         return obj.strftime("%d/%m/%y - %H:%M")

      return json.JSONEncoder.default(self, obj)

"""
Classe Gerenciador de Livros que oferece as funcionalidades de postar, carregar, editar e remover os itens cadastrados no banco de dados
"""

class GerenciadorDeLivros(webapp2.RequestHandler):
    def get(self):
        url = BASE_URL+'getComentarios?idlivro='
        url_del = BASE_URL+'deletarLivro?id='
        url_put = BASE_URL+'updateLivro'
        url_post_c = BASE_URL+'postarComentario'
        self.response.headers['Content-Type'] = 'application/json' 
        result = json.dumps([dict(p.to_dict().items() + [('urlGetCometarios',  url+'%s' %p.id),
            ('exampleDeletaLivro',  '-X DELETE '+url_del+'%s' %p.id),
            ('examplePostComentario',  '-X POST -d \'idlivro=%s&usuario=user1&conteudo=Texto exemplo\' %s' %(p.id, url_post_c)),
            ('exampleUpdateLivro',  '-X PUT -d \'id=%s&titulo=%s&desc=%s&autores=%s&preco=%s&urlCapa=%s\' %s' %(p.id, p.titulo, p.desc, p.autores, p.preco, p.urlCapa, url_put))]) for p in Livro.query(Livro.id == self.request.get('id')).fetch()], cls=MyJsonEncoder) 
        self.response.out.write(result)    

    def post(self):
        livro = Livro(id=id_generator(),
        	titulo=self.request.get('titulo'),
        	autores=self.request.get('autores'),
        	desc=self.request.get('desc'),
          preco=self.request.get('preco'),
          urlCapa=self.request.get('urlCapa'),
          data=datetime.now())
        livro.put()
        self.response.out.write('ok');

    def put(self):
  		livro = Livro.query( Livro.id == self.request.get('id') ).fetch(keys_only=True)[0].get()
  		livro.titulo = self.request.get('titulo')
  		livro.autores = self.request.get('autores')
  		livro.desc = self.request.get('desc')
  		livro.preco = self.request.get('preco')
  		livro.urlCapa = self.request.get('urlCapa')
  		livro.put()
  		self.response.out.write('ok');

    def delete(self):
      livro = Livro.query( Livro.id == self.request.get('id') ).fetch(keys_only=True)
      comentarios = Comentario.query( Comentario.idlivro == self.request.get('id') ).fetch(keys_only=True)
      ndb.delete_multi(livro)
      ndb.delete_multi(comentarios)
      self.response.out.write('ok');

class DeleteLivros(webapp2.RequestHandler):
    def delete(self):
  		livros = Livro.query().fetch(keys_only=True)
  		ndb.delete_multi(livros)
  		self.response.out.write('ok');


class GetLivros(webapp2.RequestHandler):
    def get(self):
        url = BASE_URL+'getComentarios?idlivro='
        url_livro = BASE_URL+'getLivro?id='
        self.response.headers['Content-Type'] = 'application/json' 
        result = json.dumps([dict(p.to_dict().items() + [('urlGetCometarios',  url+'%s' %p.id),
            ('urlGetDetalhesLivro',  url_livro+'%s' %p.id)]) for p in Livro.query().order(Livro.data).fetch()], cls=MyJsonEncoder) # Query com filtro: Livro.query(Livro.attr == "XLZ")
        self.response.out.write(result)   
"""
Classe Gerenciador de Comentarios que oferece as funcionalidades de postar, carregar, editar e remover os objetos do tipo Comentario inseridos por usuarios cadastrados no sisterma
"""
class GerenciadorDeComentarios(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json' 

        url = BASE_URL+'getLivro?id='
        id_ = self.request.get('idlivro', '')
        if id_ != '':
          query_comentarios = Comentario.query( Comentario.idlivro ==  id_).order(Comentario.data)
        else:
          query_comentarios = Comentario.query().order(Comentario.data)
        result = json.dumps([dict(p.to_dict().items() + [('urlGetLivro',  url+'%s' %p.idlivro)]) for p in query_comentarios.fetch()], cls=MyJsonEncoder) 
        self.response.out.write(result)

    def post(self):
    	try:
    		_data= datetime.strptime(self.request.get('data'), '%b %d %Y %H:%M:%S')
    	except:
    		_data= utc_to_local(datetime.now()).replace(tzinfo=None)

        comentario = Comentario(id=id_generator(),
        	idlivro=self.request.get('idlivro'),
        	usuario=self.request.get('usuario'),
        	data=_data,
            conteudo=self.request.get('conteudo'))
        comentario.put()
        self.response.out.write('ok');


"""
Classe Gerenciador de Usuario que oferece as funcionalidades de postar, carregar, editar e remover os usuarios no banco de dados
"""
class GerenciadorDeUsuarios(webapp2.RequestHandler):
    def get(self):
        email = self.request.get('email')
        hashsenha = self.request.get('hashsenha')
        self.response.headers['Content-Type'] = 'application/json' 

        query_usuario = Usuario.query(Usuario.email == email, Usuario.hashSenha == hashsenha)
        result = json.dumps([p.to_dict() for p in query_usuario.fetch()], cls=MyJsonEncoder)

        self.response.out.write(result)    

    def post(self):
        u = Usuario(id=id_generator(),
          nome=self.request.get('nome'),
          sobrenome=self.request.get('sobrenome'),
          email=self.request.get('email'),
          hashSenha=self.request.get('hashsenha'),
          data=datetime.now())
        u.put()
        self.response.out.write('ok');
  
class DeleteLivros(webapp2.RequestHandler):
    def delete(self):
      livros = Livro.query().fetch(keys_only=True)
      ndb.delete_multi(livros)
      self.response.out.write('ok');


class GetLivros(webapp2.RequestHandler):
    def get(self):
        url = BASE_URL+'getComentarios?idlivro='
        url_livro = BASE_URL+'getLivro?id='
        self.response.headers['Content-Type'] = 'application/json' 
        result = json.dumps([dict(p.to_dict().items() + [('urlGetCometarios',  url+'%s' %p.id),
            ('urlGetDetalhesLivro',  url_livro+'%s' %p.id)]) for p in Livro.query().order(Livro.data).fetch()], cls=MyJsonEncoder) # Query com filtro: Livro.query(Livro.attr == "XLZ")
        self.response.out.write(result)  

"""
Classe de Gerenciamento e controle para resetar e remover todos os dados do sistema 
"""


class ResetaSistema(webapp2.RequestHandler):
    def get(self):
      comentarios = Comentario.query().fetch(keys_only=True)
      ndb.delete_multi(comentarios)

      livros = Livro.query().fetch(keys_only=True)
      ndb.delete_multi(livros)

      for livro in lista_default:		
        novo_livro = Livro(id=livro['id'],
          titulo= livro['titulo'],
          autores= livro['autores'],
          desc= livro['desc'],
          preco= livro['preco'],
          urlCapa= livro['urlCapa'],
          data=utc_to_local(datetime.now()).replace(tzinfo=None))
        novo_livro.put()

      for comentario in lista_comentarios: 
        novo_comentario = Comentario(id=id_generator(),
          idlivro= comentario['idlivro'],
          usuario= comentario['usuario'],
          conteudo= comentario['conteudo'],
          data= utc_to_local(datetime.now()).replace(tzinfo=None))
        novo_comentario.put()

      self.response.out.write('ok');

"""
Interface de roteamento que liga as fucnionalidades disponíveis na REST API as respectivas classes de gerenciamento:
  /                 : Disponibiliza ao usuário a interface web inicial da aplicação
  /api              : Disponibiliza a interface de Documentação explicando detalhadament o uso da API REST
  /inserirLivro     : Disponibliza a funcionalidade POST para inserir livros no servidor da API
  /getLivros        : Disponibliza a funcionalidade GET que retorna os livros cadastrados no seridor da API
  /inserirLivro     : Disponibliza a funcionalidade GET que retorna um livro especifico a partir de uma chave identificadora
  /deletarLivro     : Disponibliza a funcionalidade DELETE para remover um livro no servidor da API
  /updateLivro      : Disponibliza a funcionalidade PUT para atualizar atributos de um livro no servidor da API
  /deletarLivros    : Disponibliza a funcionalidade DELETE para remover livros no servidor da API
  /postarComentario : Disponibliza a funcionalidade POST para inserir comentarios no servidor da API
  /getComentarios   : Disponibliza a funcionalidade GET que retorna os comentarios cadastrados no seridor da API
  /postUsuario      : Disponibliza a funcionalidade POST para inserir um novo usuário no servidor da API
  /getUsuario       : Disponibliza a funcionalidade GET que retorna os dados de um usuário cadastrado no seridor através da chave identificadora
  /resetaSistema    : Oferece a opção de suporte e manutenção para reiniciar e limpar os dados do servidor
  
    
  
  
"""
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api', RestApiPage),
    ('/inserirLivro', GerenciadorDeLivros),
    ('/getLivros', GetLivros),
    ('/getLivro', GerenciadorDeLivros),
    ('/deletarLivro', GerenciadorDeLivros),
    ('/updateLivro', GerenciadorDeLivros),
    ('/deletarLivros', DeleteLivros),
    ('/postarComentario', GerenciadorDeComentarios),
    ('/getComentarios', GerenciadorDeComentarios),
    ('/postUsuario', GerenciadorDeUsuarios),
    ('/getUsuario', GerenciadorDeUsuarios),   
    ('/resetaSistema', ResetaSistema),
    
], debug=True)
