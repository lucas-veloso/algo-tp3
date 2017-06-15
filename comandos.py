from grafo import *

def similares(grafo,usuario,cantidad):
	if (not grafo.vertice_pertenece(usuario)):
		return None

	adyacentes = grafo.obtener_adyacentes(usuario)


