import sys

sys.path.append("..")

from guerraterritorios.controller.operaciones import *
from guerraterritorios.tests.testsFunctions import *

def guardarRetornaFalseSiLaDireccionNoEsCorrecta():
    path = "..../esto no es un path"
    string = "debe dar error"

    esFalso(guardar(path, string))

def guardarPuedeCrearElArchivo():    
    path = "tests/controller/prueba.txt"
    string = "Hola! Soy una prueba!"

    esVerdadero(guardar(path, string))

def leerPuedeObtenerLosDatosDePrueba():
    path = "tests/controller/prueba.txt"
    expected = "Hola! Soy una prueba!"

    sonIguales(leer(path), expected)

def leerRetornaFalseSiElArchivoNoExiste():
    path = "a-complete-false path.no_existo"

    esFalso(leer(path))


def correrTests():
    printTitulo("Testeando guerraterritorios/controller/operaciones.py:")

    print("Guardar va a retornar False si el path es incorrecto:")
    guardarRetornaFalseSiLaDireccionNoEsCorrecta()

    print("Guardar puede crear un archivo en esta carpeta:")
    guardarPuedeCrearElArchivo()

    print("Leer puede leer correctamente los datos de prueba.txt:")
    leerPuedeObtenerLosDatosDePrueba()

    print("Leer va a retornar False si el archivo no existe:")
    leerRetornaFalseSiElArchivoNoExiste()

correrTests()