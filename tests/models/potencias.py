import sys

sys.path.append("..")

from guerraterritorios.models.potencias import *
from guerraterritorios.tests.testsFunctions import *

def esUnaPotenciaPuedeValidarUnaListaQueNoEsPotencia():
    lista = ["no es una potencia"]

    esFalso(esUnaPotencia(lista))

def esUnaPotenciaPuedeValidarPaises():
    potencia = [
        "Sirios",
        "Activo",
        900,
        123,
        400,
        75.0,
        True,
        [
            []
        ]
    ]

    esFalso(esUnaPotencia(potencia))

def esUnaPotenciaRetornaTrueSiEsUnaPotencia():
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
                                [100, 50, 30], [150, 60, 40]
                            ],
                            [
                                [100, 90, 30], [180, 30, 40]
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
    potencia = [
        "Sirios",
        "Activo",
        900,
        123,
        400,
        75.0,
        True,
        [
            pais
        ]
    ]

    esVerdadero(esUnaPotencia(potencia))

def correrTests():
    printTitulo("Testeando guerraterritorios/models/potencias.py:")

    print("EsUnaPotencia puede validar una lista que no cumple la estructura:")
    esUnaPotenciaPuedeValidarUnaListaQueNoEsPotencia()

    print("EsUnaPotencia puede validar la estructura de los territorios:")
    esUnaPotenciaPuedeValidarPaises()

    print("EsUnaPotencia retorna True si se envia una potencia:")
    esUnaPotenciaRetornaTrueSiEsUnaPotencia()

correrTests()