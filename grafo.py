class Grafo(object):

	def __init__(self):
		self.vertices = {}
		self.cantidadVertices = 0

 	def agregar_vertice(self,vertice):
 		''' AGREGA UN VERTICE AL GRAFO, SI EL VERTICE YA ESTA EN EL GRAFO DEVUELVE FALSE
 		SI NO ESTA DEVUELVE TRUE'''
		if (vertice in self.vertices): 
			return False
		self.vertices[vertice] = {} 
		self.cantidadVertices += 1
		return True

	def quitar_vertice(self,vertice):
		'''ELIMINA UN VERTICE, DEBO SACARLO DE SUS ADYACENTES TAMBIEN'''
		adyacentes = self.obtener_adyacentes(vertice) 
		for i in adyacentes:
			del self.vertices[i][vertice]
		del self.vertices[vertice]
		self.cantidadVertices -= 1

	def agregar_arista(self,vertice1,vertice2):
                if (vertice1 == vertice2):
                        return False
                self.vertices[vertice1][vertice2] = True
                self.vertices[vertice2][vertice1] = True
                return True
	#def quitar_arista (self,vertice_origen,vertice_destino):

	def tamanio_grafo(self):
		'''DEVUELVE LA CANTIDAD DE VERTICES QUE TIENE EL GRAFO'''
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
		for adyacente in self.vertices[vertice]:
			lista_adyacentes.append(adyacente)
		return lista_adyacentes

