import sys

sys.path.append("..")

from guerraterritorios.tests.testsFunctions import *
from guerraterritorios.models.coordenadas import *

def esUnaLatitudPuedeVerificarSiLaListaNoCumpleLaEstructura():
    posicion = [120, 30, 20, 40]

    esFalso(esUnaLatitud(posicion))

def esUnaLatitudPuedeVerificarUnaPosicionErronea():
    posicion = [-190, 50, 70]

    esFalso(esUnaLatitud(posicion))

def esUnaLatitudPuedeVerificarSiLaListaCumpleLaEstructura():
    posicion = [59, 30, 20]

    esVerdadero(esUnaLatitud(posicion))

def esUnaCoordenadaPuedeVerificarSiLaListaCumpleLaEstructura():
    coordenada = [[120, 30, 20],[60, 20, 50]]
    esVerdadero(esUnaCoordenada(coordenada))

def esUnaCoordenadaPuedeVerificarSiLaListaNoCumpleLaEstructura():
    coordenada= [[[120, 30, 20],[140, 20, 50]], [[120, 30, 20],[140, 20, 50]]]
    esFalso(esUnaCoordenada(coordenada))

def correrTests():
    printTitulo("Testeando guerraterritorios/models/coordenadas.py:")

    print("EsUnaPosicion puede verficar si la lista cumple la estructura:")
    esUnaLatitudPuedeVerificarSiLaListaCumpleLaEstructura()

    print("EsUnaPosicion puede verificar si la lista tiene datos incorrectos")
    esUnaLatitudPuedeVerificarUnaPosicionErronea()

    print("EsUnaPosicion puede verificar si la lista no cumple la estructura")
    esUnaLatitudPuedeVerificarSiLaListaNoCumpleLaEstructura()

    print("EsUnaCoordenada puede verificar si la lista cumple la estructura")
    esUnaCoordenadaPuedeVerificarSiLaListaCumpleLaEstructura()

    print("EsUnaCoordenada puede verificar si la lista no cumple la estructura")
    esUnaCoordenadaPuedeVerificarSiLaListaNoCumpleLaEstructura()

correrTests()
