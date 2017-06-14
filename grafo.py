class Grafo(object):

	def __init__(self):
		self.vertices = {}
		self.cantidadVertices = 0

 	def agregar_vertice (self,vertice):
 		''' AGREGA UN VERTICE AL GRAFO, SI EL VERTICE YA ESTA EN EL GRAFO DEVUELVE FALSE
 		SI NO ESTA DEVUELVE TRUE'''
		if (vertice in self.vertices): 
			return False
		self.vertices[vertice] = {} 
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
		'''DEVUELVE TRUE SI DOS VERTICES SON ADYACENTES'''
		if (vertice1 in self.vertices[vertice2]): 
			return True
		else:
			return False

	def obtener_adyacentes(self,vertice):
		'''DEVUELVE UNA LISTA CON TODOS LOS VERTICES ADYACENTES'''
		lista_adyacentes = []
		for vertice in self.vertices[vertice]:
			lista_adyacentes.append(vertice)

