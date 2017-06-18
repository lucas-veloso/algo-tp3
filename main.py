import argparse
from popgrafo import popular_grafo
from comandos import Comandos


# hay que hacer que se puedan parsear varias acciones

def unpack(list):
	return list.pop(0), list



command = Comandos()
dic = { "similares" : command.similares,
		"recomendar" : command.recomendar,
		"centralidad" : command.centralidad,
		"distancias" : command.distancias,
		"estadisticas" : command.estadisticas,
	  }


def main():
	parser = argparse.ArgumentParser(description='TP3 - Grafos y eso')
	parser.add_argument('narchivo', help='nombre del archivo que tiene los datos del grafo')
	args = parser.parse_args()
	grafo = popular_grafo(args.narchivo)		
	comando = ""

	print 'ingresar comando a utilizar ("salir" para salir de programa)'
	while comando != "salir":
		comando = raw_input('--> ')
		if comando != "salir":
			ncomando, args  = unpack(comando.split(' '))
			dic[ncomando](grafo,*args)


	
if __name__ == "__main__":
	main()


