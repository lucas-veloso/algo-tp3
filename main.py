import argparse
from pobgrafo import poblar_grafo


# hay que hacer que se puedan parsear varias acciones

def main():
	parser = argparse.ArgumentParser(description='TP3 - Grafos y eso')
	parser.add_argument('narchivo', help='nombre del archivo que tiene los datos del grafo')
	args = parser.parse_args()

	grafo = poblar_grafo(args.narchivo)
	
if __name__ == "__main__":
	main()


