#Importaciones de los modulos
import random
import sys
import os

# Agregar el directorio padre al path para permitir importaciones relativas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importaciones de módulos propios
from LogicTTY.logica import *

# Creación de excepciones personalizadas
class CoordenadasValorIncorrecto(ValueError):
    pass
class CantidadValorIncorrecto(ValueError):
    pass

# Función para ingresar cantidad de barcos, fila o columna
def Ingresar_cantidad(i):
    while True:
        try:
            if i == 1:
                cantidad = int(input("Ingrese la cantidad de barcos (1 - 9) que desea: "))
            if i == 2: 
                cantidad = int(input("Ingrese la fila (1 - 10) a la que desea disparar: "))
            if i == 3:
                cantidad = int(input("Ingrese la columna (1 - 10) a la que desea disparar: "))

            if i == 2 or i == 3:
                if 1 <= cantidad <= 10:
                    return cantidad
                else:
                    raise CantidadValorIncorrecto
            if i == 1:
                if 0 < cantidad <= 9:
                    return cantidad
                else:
                    raise CantidadValorIncorrecto
            
        except CantidadValorIncorrecto:
            if i == 1:
                print("Ingrese un valor entre 1 y 9")
            else:
                print("Ingrese un valor entre 1 y 10")
        except Exception:
            if i == 1:
                print("Ingrese un valor entre 1 y 9")
            else:
                print("Ingrese un valor entre 1 y 10")

# Función para preguntar al usuario si desea seguir jugando
def preguntar_seguir_jugando():
    print("\n")
    print("_______________________________________________")
    try:
        if int(input("Si desea continuar ingrese cualquier cosa, si desea terminar ingrese '0': ")) != 0:
            return False
        return True
    except Exception:
        return False

# Función principal para jugar
def Jugar():
    juego = Tablero()
    print("\n")
    juego.colocar_barcos(Ingresar_cantidad(1))
    juego_terminado = False
    while not juego_terminado:
        print("\n")
        juego.mostrar_tablero()
        print("\n")
        juego.imprimir_tablerocolor()
        print("\n")
        fila = Ingresar_cantidad(2)
        columna = Ingresar_cantidad(3)
        juego.disparar(fila, columna)
        juego.eliminar_barco(fila, columna)

        if juego.buscar_barco():
            print("\n")
            print("________________________")
            print(" ¡Felicidades, ganaste! ")
            return
        juego_terminado = preguntar_seguir_jugando()

    print("\n")
    print(" ¡Gracias por jugar! ")

# Llamada a la función principal para iniciar el juego
Jugar()