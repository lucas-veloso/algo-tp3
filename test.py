import unittest
from grafo import Grafo

class GrafoTestCrear(unittest.TestCase):
	"""pruebas de instanciado de la clase 'Grafo'"""

	def setUp(self):
		self.grafo = Grafo()
		self.assertTrue(self.grafo, msg = "el grafo no fue creado de forma exitosa") 
		frutas = ["manzana", "banana", "pera"]
		for fruta in frutas:
			self.grafo.agregar_vertice(fruta)
		
	def test_tamanio_grafo(self):
		"""
		verificar que el tamanio sea 3 
		"""
		value = self.grafo.tamanio_grafo()
		self.assertTrue(value == 3, msg = "el tamanio es incorrecto, es {} cuando deberia ser 3".format(value))

	def test_agregar_vertice_ya_creado(self):
		"""
		agrega el vertice 'manzana' al grafo y devuelve false		
		"""

		value = self.grafo.agregar_vertice("manzana")
		self.assertFalse(value, msg = 'agregar un elemento que ya existe al grafo deberia devolver false')
		self.assertTrue(self.grafo.tamanio_grafo() == 3, msg = "el tamanio es incorrecto, es {} cuando deberia ser 3".format(value))

if __name__ == "__main__":
	unittest.main(verbosity=2)


