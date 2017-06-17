class Grafo(object):

	def __init__(self):
		self.vertices = {}
		self.cantidadVertices = 0
		self.cantidadAristas = 0

 	def agregar_vertice(self,vertice):
 		''' AGREGA UN VERTICE AL GRAFO, SI EL VERTICE YA ESTA EN EL GRAFO DEVUELVE FALSE
 		SI NO ESTA DEVUELVE TRUE'''
		if (self.vertice_pertenece(vertice)): #Si ya existe en el grafo no lo agrego 
			return False
		self.vertices[vertice] = {} 
		self.cantidadVertices += 1
		return True

	def quitar_vertice(self,vertice):
		'''BOOLEAN ELIMINA UN VERTICE, DEBO SACARLO DE SUS ADYACENTES TAMBIEN'''
		if (not self.vertice_pertenece(vertice)): #Si no pertenece al grafo no lo puedo quitar
			return False
		adyacentes = self.obtener_adyacentes(vertice) 
		for i in adyacentes:
			self.vertices[i].pop(vertice,None)
		self.vertices.pop(vertice,None)
		self.cantidadVertices -= 1
		return True

	def agregar_arista(self,vertice1,vertice2):
		'''BOOLEAN AGREGA LA ARISTA FORMADA POR EL VERTICE 1 Y EL VERTICE 2 
		(SE CREA UNA ADYACENCIA ENTRE ELLOS)'''
		if (not self.vertice_pertenece(vertice1) or not self.vertice_pertenece(vertice2)): #Si no existe algun vertice entonces no puede haber adyacencia
			return False
		if (vertice1 == vertice2):
			return False
		if (self.son_adyacentes(vertice1,vertice2)): #Si ya existe la arista no la vuelvo a agregar
			return False
		self.vertices[vertice1][vertice2] = True
		self.vertices[vertice2][vertice1] = True
		self.cantidadAristas += 1
		return True

	def quitar_arista (self,vertice1,vertice2):
		'''BOOLEAN ELIMINA LA ARISTA FORMADA POR ELV ERTICE 1 Y EL VERTICE2
		(ELIMINA SU ADYACENCIA'''
		if (vertice1 == vertice2):
			return False
		if (not self.son_adyacentes(vertice1,vertice2)): #Si no existe adyacencia no puedo borrar la arista
			return False 
		self.vertices[vertice1].pop(vertice2,None)
		self.vertices[vertice2].pop(vertice1,None)
		self.cantidadAristas -=1
		return True

	def tamanio_grafo(self):
		'''DEVUELVE LA CANTIDAD DE VERTICES QUE TIENE EL GRAFO'''
		return self.cantidadVertices

	def cantidad_aristas(self):
		''' DEVUELVE LA CANTIDAD DE ARISTAS QUE TIENE EL GRAFO'''
		return self.cantidadAristas

	def vertice_pertenece(self,vertice):
		'''BOOLEAN VERIFICA SI UN VERTICE EXISTE EN EL GRAFO'''
		if (vertice in self.vertices):
			return True
		else:
			return False

	def son_adyacentes(self,vertice1,vertice2):
		'''BOOLEAN DEVUELVE TRUE SI DOS VERTICES SON ADYACENTES'''
		if (not self.vertice_pertenece(vertice1) or not self.vertice_pertenece(vertice2)): #Si no existe algun vertice entonces no puede haber adyacencia
			return False
		if (vertice1 in self.vertices[vertice2] and vertice2 in self.vertices[vertice1]): #Doble verificacion de adyacencia 
			return True
		else:
			return False

	def obtener_adyacentes(self,vertice):
		'''DEVUELVE UNA LISTA CON TODOS LOS VERTICES ADYACENTES'''
		if (not self.vertice_pertenece(vertice)):
			return None
		lista_adyacentes = list(self.vertices[vertice].keys())
		return  lista_adyacentes

	def obtener_identificadores(self):
		'''DEVUELVE UNA LISTA CON TODOS LOS VERTICES DEL GRAFO'''
		lista_vertices = list(self.vertices.keys())
		return lista_vertices

	def obtener_grado_promedio(self):
		''' DEVUELVE EL PROMEDIO DE  LOS GRADOS DE LOS VERTICES'''
		suma_grados = 0
		for i in self.vertices.keys():
			suma_grados += len(self.obtener_adyacentes(i))
		grado_promedio = suma_grados / self.cantidadVertices
		return grado_promedio