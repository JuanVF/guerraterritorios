import sys

sys.path.append("..")

from guerraterritorios.controller.registros import *
from guerraterritorios.tests.testsFunctions import *

def leerRegistroPuedeObtenerLaListaDeLosRegistros():
    registros = leerRegistros()

    esUnaLista(registros)

def registrarDisparoDetectaUnaListaQueNoCumpleRequisitos():
    disparo = ["Esto no cumple el modelo de disparos"]

    esFalso(guardarRegistroAtaque(disparo))

def registrarDisparoPuedeRegistrarDisparoQueAtino():
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

    esVerdadero(guardarRegistroAtaque(disparo))

def registrarDisparoPuedeRegistrarDisparoQueNoAtino():
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
        False
    ]

    esVerdadero(guardarRegistroAtaque(disparo))

def correrTests():
    printTitulo("Testeando guerraterritorios/controller/registros.py:")
    print("LeerRegistro puede obtener la lista de registros.log")
    leerRegistroPuedeObtenerLaListaDeLosRegistros()

    print("RegistrarDisparos es capaz de detectar que la entrada no cumple los requisitos")
    registrarDisparoDetectaUnaListaQueNoCumpleRequisitos()

    print("RegistrarDisparos puede registrar un disparo que atino:")
    registrarDisparoPuedeRegistrarDisparoQueAtino()

    print("RegistrarDisparos puede registrar un disparo que no atino:")
    registrarDisparoPuedeRegistrarDisparoQueNoAtino()

if __name__ == "__main__":
    correrTests()