#-*- coding: utf-8-*-
import datetime
import sys

class Usuario:
  
  '''
  A classe user contém os atributos:
  login (privado, string e não contém números)
  password (privado, string)
  listaItens (privado)

  Os métodos são:
  construtor
  toString
  getters/setters para os atributos privados
  '''
  
  def __init__ (self, login, password):
  	listaItens = []
  	 #verifica se o login contém números. Caso positivo, retorna a mensagem de erro e a exceção antes da criação do usuário.
    try:
      if login.isalpha() == False:
        raise ValueError("O campo deve conter somente letras. Nada de números.")
      
        self.__login = login
        self.__password = password
        self.__listaItens = listaItens
      
      except ValueError as error:
        print error.message

  #Criação e modificação de login:

  def getLogin (self):
    return self.__login
    
  def setLogin (self, novoLogin):
    self.__login = novoLogin
    print "O login foi alterado com sucesso." 
    #Esta última linha pode ser removida sem prejuízo a função.

  #Criação e modificação da senha.

  def getPassword (self):
    return self.__password

  def setPassword (self, novoPassword):
    self.__password = novoPassword
    return self.__password 
    #As últimas duas linhas podem ser removidas sem prejuízo a função.

  def getListaItens (self):
    return self.__listaItens

  def setListaItens (self):
    novaLista = []
    self.__listaItens = novaLista
    return self.__listaItens

class ItemDeCompra (Usuario):

	def __init__(self, nome, preco, dataCompra, localCompra):
		try:
			if nome.isalpha() == False:
				raise ValueError("O campo deve conter somente letras.")

			if preco.isdigit() == False
				raise ValueError("O campo deve conter somente números.")

			self.__nome = nome
			self.__preco = preco
			self.__dataCompra = dataCompra
			self.localCompra = localCompra

		except ValueError as erroLetras:
			print erroLetras.message

		except ValueError as erroNumeros:
			print erroNumeros.message

	def getNome(self):
		return self.__nome

	def setNome(self, nomeProduto):
		self.__nome = nomeProduto
		print "O nome do produto foi alterado com sucesso."

	def getPreco(self):
		return self.__preco

	def setPreco(self, novoPreco):
		self.__preco = float(novoPreco)
		print "O preço foi alterado com sucesso."

	def getDataCompra(self):
		return self.__dataCompra

	def setDataCompra(self, data):
    dia = data[:2]
    mes = data[3:5]
    ano = data[6:]
    
		