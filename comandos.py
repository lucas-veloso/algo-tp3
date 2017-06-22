from grafo import *
from random import randint
import random

''' CONSTANTES '''
CANTIDAD_CAMINOS = 50
LARGO_CAMINO = 2000

''' --------------------------	METODOS AUXILIARES	--------------------------'''
def rw (grafo,usuario,guardar_adyacentes,centralidad):
	''' REALIZA UN RANDOM WALK Y GUARDA LOS VERTICES Y SUS OCURRENCIAS EN UN HASH 
	SI <guardar_adyacentes> ES FALSE ENTONCES NO SE GUARDARAN EN EL DICCIONARIO SI ES TRUE SI SE GUARDARAN'''

	random_walk = {}
	if (centralidad):
		vertices = grafo.obtener_identificadores()
	for i in xrange(0,CANTIDAD_CAMINOS):
		if (centralidad):
			usuario = random.choice(vertices)
		adyacentes = grafo.obtener_adyacentes(usuario)
		for j in xrange(0,LARGO_CAMINO):
			v_random = randint(0,len(adyacentes)-1)
			if (adyacentes[v_random] in random_walk):
				random_walk[adyacentes[v_random]] +=1
			elif ((adyacentes[v_random]) != usuario):
				if (not guardar_adyacentes and not grafo.son_adyacentes(usuario,adyacentes[v_random])):
					random_walk[adyacentes[v_random]] = 1
				elif (guardar_adyacentes):
					random_walk[adyacentes[v_random]] = 1
			adyacentes = grafo.obtener_adyacentes(adyacentes[v_random])
	return random_walk

def dic_to_list(diccionario):
	''' TRANSFORMA UN DICCIONARIO DE CLAVES Y OCURRENCIAS EN UNA LISTA DE LISTAS "ORDENADA"
	DE MAYOR A MENOR '''
	lista_rw = [None] * (max(diccionario.values())+1)
	for i in xrange(0,len(lista_rw)):
		lista_rw[i] = []
	for clave,ocurrencias in diccionario.iteritems():
		lista_rw[ocurrencias].append(clave)
	return lista_rw

def print_list(lista,cantidad):
	''' IMPRIME LA CANTIDAD ESPECIFICADA EN ORDEN DE UNA LISTA DE LISTAS '''
	contador = 0
	corte_control = False
	for i in xrange(len(lista)-1,0,-1):
		if (lista[i] != []):
			for j in xrange(0,len(lista[i])):
				print lista[i][j],
				contador +=1
				if (contador == cantidad):
					corte_control = True
					break
		if corte_control:
			break
	print

def max_freq(grafo,vert):
	mfreq = {}
	for vertice in grafo.vertices[vert]:
		if vertice in mfreq:
			mfreq[vertice] += 1
		else:
			mfreq[vertice] = 1

	maxFreq = 0 
	nombreVertice = ''

	for key,value in mfreq.iteritems():
		if value > maxFreq:
 			nombreVertice = key

 	return nombreVertice

''' --------------------------	FUNCIONALIDADES TP3	--------------------------'''
class Comandos(object):
	
	def similares(self,grafo,usuario,cantidad):
		'''DEVUELVE UNA LISTA CON LOS N USUARIOS MAS SIMILARES AL USUARIO
		DE MAYOR A MENOR SIMILARIDAD'''
		if (not grafo.vertice_pertenece(usuario)):
			print ("El usuario espesificado no pertenece a youtube.")
			return
		if (not grafo.vertice_pertenece(usuario)):
			return None
		similares = rw(grafo,usuario,True,False) # Realizar random walk
		lista_similares = dic_to_list(similares) #Trasformar hash en lista de listas
		print_list(lista_similares,int(cantidad)) #Imprimir vertices similares

	def recomendar(self,grafo,usuario,cantidad):
		'''DEVUELVE UNA LISTA DE USUARIOS SIMILARES CON LOS CUALES NO TENGA RELACION'''
		if (not grafo.vertice_pertenece(usuario)):
			print ("El usuario espesificado no pertenece a youtube.")
			return

		if (not grafo.vertice_pertenece(usuario)):
			return None
	
		if (grafo.obtener_densidad() == 1):
			print ("El grafo es completo todos estan conectados con todos, nadie que recomendar")
			return None
		recomendables = rw(grafo,usuario,False,False) #Realizar random walk
		lista_recomendables = dic_to_list(recomendables) #Transformar hash en lista de listas
		print_list(lista_recomendables,int(cantidad)) #Imprimir vertices recomendables

	def centralidad(self,grafo,cantidad):
		v_centrales = rw(grafo,None,False,True)
		lista_centrales = dic_to_list(v_centrales)
		print_list(lista_centrales,int(cantidad))

	def camino(self,grafo,origen,destino):
		if (not grafo.vertice_pertenece(origen) or not grafo.vertice_pertenece(destino)):
			print ("El usuario espesificado no pertenece a youtube.")
			return

		padres = caminos_minimos(grafo,origen,destino)
		if (padres == None):
			print("No hay camino entre estos dos usuarios")
			return

		camino = []
		llegada = padres[destino]
		while llegada != origen :
			camino.insert(0,llegada)
			llegada = padres[llegada]
	
		print str(origen) + "->",
		for i in xrange(0,len(camino)):
			print str(camino[i]) + "->",
		print str(destino)
	
	def distancias(self,grafo,usuario):
		if (not grafo.vertice_pertenece(usuario)):
			print ("El usuario espesificado no pertenece a youtube.")
			return
		orden = bfs_orden(grafo,usuario) #Diccionario con vertices y sus distancias respecto del usuario
		lista_distancia = dic_to_list(orden) #Lo paso a la famosa lista de listas
		for i in xrange(1,len(lista_distancia)):
			if (lista_distancia[i] != []):
				print ("Distancia ") + str(i) +  ": " + str(len(lista_distancia[i]))

	def estadisticas(self,grafo):
		print ("Cantidad de vertices: ") + str(grafo.tamanio_grafo())
		print ("Cantidad de aristas: ") + str(grafo.cantidad_aristas())
		grados_promedio = grafo.obtener_grado_promedio()
		print ("Promedio de grado de salida de cada vertice: ") + str(grados_promedio)
		print ("Promedio de grado de entrada de cada vertice: ") + str(grados_promedio)
		print ("Densidad del grafo: ") + str(grafo.obtener_densidad())

	def comunidades(self,grafo,usuario = '1',ncaminos = 1000, lcamino = 500):
		"""
		utiliza label propagation para clasificar los usuarios en comunidades
		"""
		comunidades = {}
		
		for i in xrange(ncaminos):
			adyacentes = grafo.obtener_adyacentes(usuario)							
			for j in xrange(lcamino):
				random = randint(0,len(adyacentes)-1)
				nvertice = max_freq(grafo,adyacentes[random])
				if nvertice not in comunidades:
					comunidades[nvertice] = [adyacentes[random]]
				elif adyacentes[random] not in comunidades[nvertice]:
					comunidades[nvertice].append(adyacentes[random])
				adyacentes = grafo.obtener_adyacentes(adyacentes[random]) 

		for key, value in comunidades.iteritems():
			largo = len(value)
			if largo > 4 and largo < 2000:
				print "comunidad: {}, miembros {}".format(key,value) 