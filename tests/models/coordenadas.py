import sys

sys.path.append("..")

from guerraterritorios.tests.testsFunctions import *
from guerraterritorios.models.coordenadas import *

def esUnaPosicionPuedeVerificarSiLaListaNoCumpleLaEstructura():
    posicion = [120, 30, 20, 40]

    esFalso(esUnaPosicion(posicion))

def esUnaPosicionPuedeVerificarUnaPosicionErronea():
    posicion = [-190, 50, 70]

    esFalso(esUnaPosicion(posicion))

def esUnaPosicionPuedeVerificarSiLaListaCumpleLaEstructura():
    posicion = [120, 30, 20]

    esVerdadero(esUnaPosicion(posicion))

def esUnaCoordenadaPuedeVerificarSiLaListaCumpleLaEstructura():
    coordenada = [[120, 30, 20],[140, 20, 50]]
    esVerdadero(esUnaCoordenada(coordenada))

def esUnaCoordenadaPuedeVerificarSiLaListaNoCumpleLaEstructura():
    coordenada= [[[120, 30, 20],[140, 20, 50]], [[120, 30, 20],[140, 20, 50]]]
    esFalso(esUnaCoordenada(coordenada))

def correrTests():
    printTitulo("Testeando guerraterritorios/models/coordenadas.py:")

    print("EsUnaPosicion puede verficar si la lista cumple la estructura:")
    esUnaPosicionPuedeVerificarSiLaListaCumpleLaEstructura()

    print("EsUnaPosicion puede verificar si la lista tiene datos incorrectos")
    esUnaPosicionPuedeVerificarUnaPosicionErronea()

    print("EsUnaPosicion puede verificar si la lista no cumple la estructura")
    esUnaPosicionPuedeVerificarSiLaListaNoCumpleLaEstructura()

    print("EsUnaCoordenada puede verificar si la lista cumple la estructura")
    esUnaCoordenadaPuedeVerificarSiLaListaCumpleLaEstructura()

    print("EsUnaCoordenada puede verificar si la lista no cumple la estructura")
    esUnaCoordenadaPuedeVerificarSiLaListaNoCumpleLaEstructura()

correrTests()
