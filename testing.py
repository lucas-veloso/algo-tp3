from grafo import *

def print_test(cadena,bool):
	if (bool):
		print cadena + ": OK"
	else:
		print cadena + ": ERROR"
	return


def pruebas_grafo():
	print("-------- PRUEBAS CREAR GRAFO --------")
	grafo = Grafo()
	print_test("El grafo esta vacio",grafo.tamanio_grafo() == 0)
	print_test("Quitar un vertice en un grafo vacio es false",grafo.quitar_vertice(1) == False)
	print_test("Agrego el vertice aceite es true",grafo.agregar_vertice("aceite"))
	print_test("Aceite pertenece al grafo",grafo.vertice_pertenece("aceite"))
	print_test("Agrego el vertice huevos es true",grafo.agregar_vertice("huevos"))
	print_test("El grafo tiene 2 vertices",grafo.tamanio_grafo() == 2)
	print_test("Huevos y Aceites no son adyacentes",grafo.son_adyacentes("aceite","huevos") == False)
	print_test("Agrego una arista entre huevos y aceite",grafo.agregar_arista("aceite","huevos"))
	print_test("Huevos y Aceite ahora son adyacentes",grafo.son_adyacentes("aceite","huevos"))
	print_test("Agrego un vertice leche",grafo.agregar_vertice("leche"))
	print_test("Leche pertenece al grafo",grafo.vertice_pertenece("leche"))
	print_test("El grafo tiene 3 vertices",grafo.tamanio_grafo() == 3)
	print_test("Leche no es adyacente a huevos",grafo.son_adyacentes("leche","huevos") == False)
	print_test("Agrego una arista entre leche y huevos",grafo.agregar_arista("leche","huevos"))
	print_test("Leche y huevos son adyacentes",grafo.son_adyacentes("leche","huevos"))

	adyacentes = grafo.obtener_adyacentes("huevos")
	print ("Verificar que la lista de adyacentes sea correcta:")
	for i in adyacentes:
		print i

	print_test("Quitar la arista leche-huevos",grafo.quitar_arista("leche","huevos"))
	print_test("Leche y huevos no son adyacentes",grafo.son_adyacentes("leche","huevos") == False)
	print_test("Eliminar el vertice Aceite",grafo.quitar_vertice("aceite"))
	print_test("Verificar que huevos no sea adyacente a aceite",grafo.son_adyacentes("huevos","aceite") == False)
	print_test("El tamanio del grafo es 2",grafo.tamanio_grafo() == 2)
	print_test("Agregar Leche otra vez es falso ya pertenece al grafo",grafo.agregar_vertice("leche") == False)

def pruebas_volumen():
	print("-------- PRUEBAS VOLUMEN --------")
	grafo = Grafo()
	ok = True
	print("Prueba agregar 50000 elementos")
	for i in range(0,50000):
		ok = grafo.agregar_vertice(i)
		if not ok:
			break

	if (not ok):
		print("Prueba agregar 50000 vertices error")

	print_test("Verificar tamanio del grafo",grafo.tamanio_grafo() == 50000)

	for i in range(0,50000):
		ok = grafo.vertice_pertenece(i)
		if not ok:
			break

	if (not ok):
		print("ERROR")
	else:
		print("Prueba vertices que pertenecen: OK")

	for i in range(0,1000):
		ok = grafo.agregar_arista(i,i+1)
		if (not ok):
			break

	if (ok):
		print("Prueba agregar 10000 aristas Ok")

	for i in range(0,1000):
		ok = grafo.son_adyacentes(i,i+1)
		if (not ok):
			break
	if (ok):
		print("Prueba son adyacentes: Ok")

	for i in range(0,25000):
		ok = grafo.quitar_vertice(i)
		if not ok:
			break

	if (ok):
		print("Prueba quitar 2500 vertices: OK")
	else:
		print("ERROR")

	print_test("Verificar tamanio del grafo",grafo.tamanio_grafo() == 25000)



'''    MAIN   '''
pruebas_grafo()
pruebas_volumen()