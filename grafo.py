class Vertice(object):

	def __init__(self,valor):
		self.valor = valor
		self.adyacentes = {}
		self.buscado = False

	def fue_buscado(self):
		return self.buscado


class Grafo(object):

	def __init__(self):
		self.vertices = {}
		self.cantidadVertices = 0

	def agregar_vertice(self,vertice):
		"""
		agrega un vertice al grafo 
		"""

		# FALTARIA UNA FORMA DE DEFINIR QUIENES SON SUS VECINOS
		self.vertices[vertice.valor] = vertice
		self.cantidadVertices += 1
		return True

	def quitar_vertice(self,vertice):
		"""
		devuelve el valor del vertice si este existia dentro del diccionario
		y None en caso contrario
		"""

		# si NO ME EQUIVOCO FALTARIA QUITAR A ESTE VERTICE DE SUS RESPECTIVOS VECINOS
		return self.vertices.pop(vertice.valor,None)

	def tamanio_grafo(self):
		"""
		devuelve la cantidad de vertices en el grafo 
		"""
		return self.cantidadVertices

	def son_adyacentes(self,vertice1,vertice2):
		return vertice1 == vertice2[vertice1.valor]

	def obtener_adyacentes(self,vertice):
		return vertice.adyacentes

