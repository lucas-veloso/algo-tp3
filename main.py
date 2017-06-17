import argparse
from popgrafo import popular_grafo


# hay que hacer que se puedan parsear varias acciones

def main():
	parser = argparse.ArgumentParser(description='TP3 - Grafos y eso')
	parser.add_argument('narchivo', help='nombre del archivo que tiene los datos del grafo')
	args = parser.parse_args()

	grafo = popular_grafo(args.narchivo)
	
if __name__ == "__main__":
	main()


