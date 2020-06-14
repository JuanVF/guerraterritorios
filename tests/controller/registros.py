import sys

sys.path.append("..")

from guerraterritorios.controller.registros import *
from guerraterritorios.tests.testsFunctions import *

pais = [
        "Costa Rica",
        100.0,
        98000.0,
        [
            [
                "Alajuela",
                [
                    [
                        "Upala",
                        [
                            [
                                [100, 50, 30], [150, 59, 40]
                            ],
                            [
                                [60, 40, 30], [70, 30, 40]
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]

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

def registrarCambioPuedeInsertarUnaPotenciaActiva():
    potencia = [
        "Sirios",
        True,
        900,
        123,
        400,
        75.0,
        True,
        [
            pais
        ]
    ]

    esVerdadero(guardarRegistroCambio(potencia))

def registrarCambioPuedeInsertarUnaPotenciaInactiva():
    potencia = [
        "Sirios",
        False,
        900,
        123,
        400,
        75.0,
        True,
        [
            pais
        ]
    ]

    esVerdadero(guardarRegistroCambio(potencia))

def registrarMuertePuedeInsertarUnaMuerteCorrectamente():
    esVerdadero(guardarRegistroMuerte("Sirios"))

def registrarCompraPuedeInsertarUnaCompra():
    esVerdadero(guardarRegistroCompra("U.R.S.S", 300))

def registrarCambioTerritorioPuedeInsertarUnCambio():
    esVerdadero(guardarRegistroTerritorio("Costa Rica", "Alajuela", "Upala",75.8))

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

    print("RegistrarCambios puede registrar una potencia activa")
    registrarCambioPuedeInsertarUnaPotenciaActiva()

    print("RegistrarCambios puede registrar una potencia inactiva")
    registrarCambioPuedeInsertarUnaPotenciaInactiva()

    print("RegistrarMuerte puede registrar la muerte de una potencia")
    registrarMuertePuedeInsertarUnaMuerteCorrectamente()

    print("RegistrarCompra puede registrar la compra de misiles por parte de una potencia:")
    registrarCompraPuedeInsertarUnaCompra()

    print("RegistrarTerritorio puede registrar cambios en una coordenada en especifico")
    registrarCambioTerritorioPuedeInsertarUnCambio()

if __name__ == "__main__":
    correrTests()