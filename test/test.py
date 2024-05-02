# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
#Lo importamos para incluir la ruta de busqueda de python
import sys
sys.path.append("src")
#Importar archivo de lógicxa para hacer las pruebas

# Importa la clase Tablero desde LogicTTY.logica
from src.LogicTTY.logica import Tablero, CoordenadasValorIncorrecto, CoordenadasNegativas


class TestTablero(unittest.TestCase):

    pass