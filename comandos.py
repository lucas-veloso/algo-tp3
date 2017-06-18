from grafo import *
from random import randint
import random

''' CONSTANTES '''
CANTIDAD_CAMINOS = 1000
LARGO_CAMINO = 500
LARGO_CAMINO_CENTRALIDAD = 500


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
		if (not grafo.vertice_pertenece(usuario)):
			return None
		similares = rw(grafo,usuario,True) # Realizar random walk
		lista_similares = crear_lista_rw(similares) #Trasformar hash en lista de listas
		imprimir_lista_rw(lista_similares,cantidad) #Imprimir vertices similares
	
	def recomendar(self,grafo,usuario,cantidad):
		'''DEVUELVE UNA LISTA DE USUARIOS SIMILARES CON LOS CUALES NO TENGA RELACION'''
		if (not grafo.vertice_pertenece(usuario)):
			return None
	
		if (grafo.obtener_densidad() == 1):
			print ("El grafo es completo todos estan conectados con todos, nadie que recomendar")
			return None
		recomendables = rw(grafo,usuario,False) #Realizar random walk
		lista_recomendables = crear_lista_rw(recomendables) #Transformar hash en lista de listas
		imprimir_lista_rw(lista_recomendables,cantidad) #Imprimir vertices recomendables
	
	def centralidad(self,grafo,cantidad):
		v_centrales = {}
		for i in range(0,CANTIDAD_CAMINOS):
			vertices = grafo.obtener_identificadores()
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
		imprimir_lista_rw(lista_centrales,cantidad)
	
	def distancias(self,grafo,usuario):
		orden = bfs(grafo,usuario) #Diccionario con vertices y sus distancias respecto del usuario
		lista_distancia = crear_lista_rw(orden) #Lo paso a la famosa lista de listas
		for i in range(1,len(lista_distancia)):
			print ("Distancia ") + str(i) +  ": " + str(len(lista_distancia[i]))
		
	def estadisticas(self,grafo):
		print ("Cantidad de vertices: ") + str(grafo.tamanio_grafo())
		print ("Cantidad de aristas: ") + str(grafo.cantidad_aristas())
		print ("Promedio de grado de salida de cada vertice: ") + str(grafo.obtener_grado_promedio())
		print ("Promedio de grado de entrada de cada vertice: ") + str(grafo.obtener_grado_promedio())
		print ("Densidad del grafo: ") + str(grafo.obtener_densidad())	