from grafo import *
from random import randint
import random
from time import time
''' CONSTANTES '''
CANTIDAD_CAMINOS = 20
LARGO_CAMINO = 10000
LARGO_CAMINO_CENTRALIDAD = 10000

''' --------------------------	METODOS AUXILIARES	--------------------------'''
def rw (grafo,usuario,guardar_adyacentes):
	''' REALIZA UN RANDOM WALK Y GUARDA LOS VERTICES Y SUS OCURRENCIAS EN UN HASH 
	SI <guardar_adyacentes> ES FALSE ENTONCES NO SE GUARDARAN EN EL DICCIONARIO SI ES TRUE SI SE GUARDARAN'''

	random_walk = {}
	for i in range(0,CANTIDAD_CAMINOS):
		adyacentes = grafo.obtener_adyacentes(usuario)
		for j in range(0,LARGO_CAMINO):
			random = randint(0,len(adyacentes)-1)
			if (adyacentes[random] in random_walk):
				random_walk[adyacentes[random]] +=1
			elif ((adyacentes[random]) != usuario):
				if (not guardar_adyacentes and not grafo.son_adyacentes(usuario,adyacentes[random])):
					random_walk[adyacentes[random]] = 1
				elif (guardar_adyacentes):
					random_walk[adyacentes[random]] = 1
			adyacentes = grafo.obtener_adyacentes(adyacentes[random])
	return random_walk

def crear_lista_rw(diccionario):
	''' TRANSFORMA UN DICCIONARIO DE CLAVES Y OCURRENCIAS EN UNA LISTA DE LISTAS "ORDENADA"
	DE MAYOR A MENOR '''
	lista_rw = [None] * (max(diccionario.values())+1)
	for i in range(0,len(lista_rw)):
		lista_rw[i] = []
	for clave,ocurrencias in diccionario.iteritems():
		lista_rw[ocurrencias].append(clave)
	return lista_rw

def imprimir_lista_rw(lista,cantidad):
	''' IMPRIME LA CANTIDAD ESPECIFICADA EN ORDEN DE UNA LISTA DE LISTAS '''
	contador = 0
	corte_control = False
	for i in range(len(lista)-1,0,-1):
		if (lista[i] != []):
			for j in range(0,len(lista[i])):
				print lista[i][j],
				contador +=1
				if (contador == cantidad):
					corte_control = True
					break
		if corte_control:
			break
	print

''' --------------------------	FUNCIONALIDADES TP3	--------------------------'''
class Comandos(object):
	
	def similares(self,grafo,usuario,cantidad):
		'''DEVUELVE UNA LISTA CON LOS N USUARIOS MAS SIMILARES AL USUARIO
		DE MAYOR A MENOR SIMILARIDAD'''
		t_i = time()
		if (not grafo.vertice_pertenece(usuario)):
			return None
		similares = rw(grafo,usuario,True) # Realizar random walk
		lista_similares = crear_lista_rw(similares) #Trasformar hash en lista de listas
		imprimir_lista_rw(lista_similares,int(cantidad)) #Imprimir vertices similares
		t_f = time()
		t_t = t_f -t_i
		print ("Similares tardo: ") + str(t_t)
		
	def recomendar(self,grafo,usuario,cantidad):
		'''DEVUELVE UNA LISTA DE USUARIOS SIMILARES CON LOS CUALES NO TENGA RELACION'''
		t_i = time()
		if (not grafo.vertice_pertenece(usuario)):
			return None
	
		if (grafo.obtener_densidad() == 1):
			print ("El grafo es completo todos estan conectados con todos, nadie que recomendar")
			return None
		recomendables = rw(grafo,usuario,False) #Realizar random walk
		lista_recomendables = crear_lista_rw(recomendables) #Transformar hash en lista de listas
		imprimir_lista_rw(lista_recomendables,int(cantidad)) #Imprimir vertices recomendables
		t_f = time()
		t_t = t_f - t_i
		print ("Recomendar tardo: ") + str(t_t)

	def centralidad(self,grafo,cantidad):
		t_i = time()
		v_centrales = {}
		vertices = grafo.obtener_identificadores()
		for i in range(0,CANTIDAD_CAMINOS):
			vertice_random = random.choice(vertices)
			adyacentes = grafo.obtener_adyacentes(vertice_random)
			for j in range(0,LARGO_CAMINO_CENTRALIDAD):
				p_random = randint(0,len(adyacentes)-1)
				if (adyacentes[p_random] in v_centrales):
					v_centrales[adyacentes[p_random]] +=1
				else:
					v_centrales[adyacentes[p_random]] = 1
				adyacentes = grafo.obtener_adyacentes(adyacentes[p_random])
	
		''' TENGO UN HASH DE USUARIOS Y CANTIDAD DE OCURRENCIAS EN CAMINOS ALEATORIOS'''
		lista_centrales = crear_lista_rw(v_centrales)
		imprimir_lista_rw(lista_centrales,int(cantidad))
		t_f = time()
		t_t = t_f - t_i
		print ("Centralidad tardo: ") + str(t_t)

	def camino(self,grafo,origen,destino):
		padres = caminos_minimos(grafo,origen,destino)
		camino = []
		llegada = padres[destino]
		while llegada != origen :
			camino.insert(0,llegada)
			llegada = padres[llegada]
	
			print str(origen) + "->",
			for i in range(0,len(camino)):
				print str(camino[i]) + "->",
			print str(destino)
	
	def distancias(self,grafo,usuario):
		print ("Iniciando BFS...")
		tiempo_inicial = time()
		orden = bfs_orden(grafo,usuario) #Diccionario con vertices y sus distancias respecto del usuario
		tiempo_final = time()
		tiempo_total = tiempo_final - tiempo_inicial
		print ("BFS Tardo: ") + str(tiempo_total)
		print ("Iniciando impresion...")
		tiempo_inicial = time()
		lista_distancia = crear_lista_rw(orden) #Lo paso a la famosa lista de listas
		for i in range(1,len(lista_distancia)):
			if (lista_distancia[i] != []):
				print ("Distancia ") + str(i) +  ": " + str(len(lista_distancia[i]))
		tiempo_final = time()
		tiempo_total = tiempo_final - tiempo_inicial
		print ("Impresion y listas anidadas tardo: ") + str(tiempo_total)
		
	def estadisticas(self,grafo):
		t_i = time()
		print ("Cantidad de vertices: ") + str(grafo.tamanio_grafo())
		print ("Cantidad de aristas: ") + str(grafo.cantidad_aristas())
		grados_promedio = grafo.obtener_grado_promedio()
		print ("Promedio de grado de salida de cada vertice: ") + str(grados_promedio)
		print ("Promedio de grado de entrada de cada vertice: ") + str(grados_promedio)
		print ("Densidad del grafo: ") + str(grafo.obtener_densidad())
		t_f = time()
		t_t = t_f - t_i
		print ("Estadisticas tardo: ") + str(t_t)

	def comunidades(self,grafo,usuario = '1',ncaminos = 1000, lcamino = 500):
		"""
		utiliza label propagation para clasificar los usuarios en comunidades
		"""
		comunidades = {}
		
		for i in range(ncaminos):
			adyacentes = grafo.obtener_adyacentes(usuario)							
			for j in range(lcamino):
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
