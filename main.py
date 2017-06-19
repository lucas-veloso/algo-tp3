import argparse
from popgrafo import popular_grafo
from comandos import Comandos
from time import time


# hay que hacer que se puedan parsear varias acciones

def unpack(list):
	return list.pop(0), list



command = Comandos()
dic = { "similares" : command.similares,
		"recomendar" : command.recomendar,
		"centralidad" : command.centralidad,
		"camino" : command.camino,
		"distancias" : command.distancias,
		"estadisticas" : command.estadisticas,
		"comunidades" : command.comunidades
	  }


def main():
	parser = argparse.ArgumentParser(description='TP3 - Grafos y eso')
	parser.add_argument('narchivo', help='nombre del archivo que tiene los datos del grafo')
	args = parser.parse_args()
	print ("Poblar grafo...")
	t_i = time()
	grafo = popular_grafo(args.narchivo)
	t_f = time()
	t_t = t_f - t_i
	print ("Poblar el grafo tardo: ") + str(t_t)		
	comando = ""

	print 'ingresar comando a utilizar ("salir" para salir de programa)'
	while comando != "salir":
		comando = raw_input('--> ')
		if comando != "salir":
			ncomando, args  = unpack(comando.split(' '))
			try:
				dic[ncomando](grafo,*args)
			except KeyError:
				print "{} No es una accion valida, Intente nuevamente".format(ncomando)
			except Exception as e:
				print "{}.Intente nuevamente".format(e)


	
if __name__ == "__main__":
	main()


