class Grafo(object):

	def __init__(self):
		self.vertices = {}
		self.cantidadVertices = 0

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
			del self.vertices[i][vertice]
		del self.vertices[vertice]
		self.cantidadVertices -= 1
		return True

	def agregar_arista(self,vertice1,vertice2):
        '''BOOLEAN AGREGA LA ARISTA FORMADA POR EL VERTICE 1 Y EL VERTICE 2
        (SE CREA UNA ADYACENCIA ENTRE ELLOS)'''
        if (vertice1 == vertice2):
            return False
        if (self.son_adyacentes(vertice1,vertice2)): #Si ya existe la arista no la vuelvo a agregar
            return False
        self.vertices[vertice1][vertice2] = True
        self.vertices[vertice2][vertice1] = True
        return True

	def quitar_arista (self,vertice1,vertice2):
         '''BOOLEAN ELIMINA LA ARISTA FORMADA POR ELV ERTICE 1 Y EL VERTICE2
        (ELIMINA SU ADYACENCIA'''
        if (vertice1 == vertice2):
                return False
        if (not self.son_adyacentes(vertice1,vertice2)): #Si no existe adyacencia no puedo borrar la arista
                return False 
        del self.vertices[vertice1][vertice2]
        del self.vertices[vertice2][vertice1]
        return True
	def tamanio_grafo(self):
		'''DEVUELVE LA CANTIDAD DE VERTICES QUE TIENE EL GRAFO'''
		return self.cantidadVertices

    def vertice_pertenece(self,vertice):
        '''BOOLEAN VERIFICA SI UN VERTICE EXISTE EN EL GRAFO'''
        if (vertice in self.vertices):
            return True
        else return False

	def son_adyacentes(self,vertice1,vertice2):
		'''BOOLEAN DEVUELVE TRUE SI DOS VERTICES SON ADYACENTES'''
	    if (not self.vertice_pertenece(vertice1) || not self.vertice_pertenece(vertice2)): #Si no existe algun vertice entonces no puede haber adyacencia
	        return False
		if (vertice1 in self.vertices[vertice2] && vertice2 in self.vertices[vertice1]): #Doble verificacion de adyacencia 
			return True
		else:
			return False

	def obtener_adyacentes(self,vertice):
		'''DEVUELVE UNA LISTA CON TODOS LOS VERTICES ADYACENTES'''
        if (not self.vertice_pertenece(vertice)):
                    return None
		lista_adyacentes = []
		for adyacente in self.vertices[vertice]:
			lista_adyacentes.append(adyacente)
		return lista_adyacentes
