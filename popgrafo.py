import grafo

def popular_grafo(archivo):
	with open(archivo,'r+') as file:
		# saltear comentarios
		for i in range(5):
			line = file.readline()

		# crear el grafo
		nuevoGrafo = grafo.Grafo()
		
		# popular el grafo
		while line: 
			par = line.replace('\n','').split('\t')
			if not nuevoGrafo.vertice_pertenece(par[0]):
				nuevoGrafo.agregar_vertice(par[0])
			if not nuevoGrafo.vertice_pertenece(par[1]):
				nuevoGrafo.agregar_vertice(par[1])
			nuevoGrafo.agregar_arista(par[0],par[1])
			line = file.readline()
	return nuevoGrafo

if __name__ == "__main__":
	popular_grafo()