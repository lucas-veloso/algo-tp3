from grafo import *
from random import randint

''' CONSTANTES '''
CANTIDAD_CAMINOS = 1000
LARGO_CAMINO = 20

def similares(grafo,usuario,cantidad):
	'''DEVUELVE UNA LISTA CON LOS N USUARIOS MAS SIMILARES AL USUARIO
	DE MAYOR A MENOR SIMILARIDAD'''

	if (not grafo.vertice_pertenece(usuario)):
		return None

	similares = {} #Diccionario para guardar los usuarios y la cantidad de ocurrencias O(1)

	for i in range(0,CANTIDAD_CAMINOS):
		adyacentes = grafo.obtener_adyacentes(usuario) #Lista de adyacentes del usuario
		for j in range(0,LARGO_CAMINO):
			random = randint(0,len(adyacentes)-1) #Posicion random de la lista de adyacentes.
			if (adyacentes[random] in similares ): #Si no esta en el diccionario lo agrego, si esta aumento en 1 su ocurrencia.
				similares[adyacentes[random]] +=1
			elif (adyacentes[random] != usuario): #No tiene sentido decir que es similar a uno mismo.
				similares[adyacentes[random]] = 1
			adyacentes = grafo.obtener_adyacentes(adyacentes[random])

	''' EN ESTE PUNTO TENGO UN DICCIONARIO CON USUARIOS SIMILARES Y SU CANTIDAD DE OCURRENCIAS '''
	lista_similares = [None] * (max(similares.values())+1)

	for i in range(0,len(lista_similares)):
		lista_similares[i] = []

	for usuario,ocurrencias in similares.iteritems():
		lista_similares[ocurrencias].append(usuario)

	contador = 0
	corte_control = False
	for i in range(len(lista_similares)-1,0,-1):
		if (lista_similares[i] != []):
			for j in range(0,len(lista_similares[i])):
				print lista_similares[i][j],
				contador +=1
				if (contador == cantidad):
					corte_control = True
					break
		if corte_control:
			break
	return lista_similares
