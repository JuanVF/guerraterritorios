import sys

sys.path.append("..")

from guerraterritorios.utils.utils import *
from guerraterritorios.tests.testsFunctions import *

def obtenerFechaRetornaLaFechaComoString():
    fecha = obtenerFecha()
    
    esUnString(fecha)

def correrTests():
    printTitulo("Testeando guerraterritorios/utils/utils.py:")

    print("Obtener fecha retorna un string")
    obtenerFechaRetornaLaFechaComoString()

correrTests()