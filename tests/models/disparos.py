import sys

sys.path.append("..")

from guerraterritorios.models.disparos import *
from guerraterritorios.tests.testsFunctions import *

def esUnDisparoPuedeDetectarUnaListaQueNoCumpleLaEstructura():
    disparo = [ "Esto no es un disparo "]

    esFalso(esUnDisparo(disparo))

def esUnDisparoPuedeDetectarUnaListaQueCumpleLaEstructura():
    disparo = [
        "U.R.S.S",
        "E.E.U.U",
        "Minnesota",
        "Saint Paul",
        [
            [
                100,
                0,
                20
            ],
            [
                50,
                0,
                30
            ]
        ],
        100.0,
        90.0,
        True
    ]

    esVerdadero(esUnDisparo(disparo))

def correrTests():
    printTitulo("Testeando guerraterritorios/models/disparos.py:")

    print("EsUnDisparo puede detectar una lista que no cumple la estructura")
    esUnDisparoPuedeDetectarUnaListaQueNoCumpleLaEstructura()

    print("EsUnDisparo puede detectar una lista que cumple la estructura")
    esUnDisparoPuedeDetectarUnaListaQueCumpleLaEstructura()

correrTests()