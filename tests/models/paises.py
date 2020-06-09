import sys

sys.path.append("..")

from guerraterritorios.tests.testsFunctions import *
from guerraterritorios.models.paises import *

def esUnPaisPuedeDetectarSiUnaListaCumpleLaEstructura():
    provincia = [
        "Alajuela",
        [
            [
                "Upala",
                [
                    [
                        [10, 20, 30],
                        [10,50, 53]
                    ],
                    [
                        [10, 20, 30],
                        [10,50, 53]
                    ]
                ]
            ]
        ]
    ]

    pais = [
        "Costa Rica",
        100.0,
        9800.0,
        [provincia]
    ]

    esVerdadero(esUnPais(pais))

def esUnPaisPuedeDetectarSiUnaListaNoCumpleLaEstructura():
    provincia = [
        "Alajuela",
        [
            [
                "Upala",
                [
                    [
                        [10, 20, 30],
                        [10,50, 53]
                    ]
                ]
            ]
        ]
    ]

    pais = [
        "Costa Rica",
        100.0,
        [provincia]
    ]

    esFalso(esUnPais(pais))

def correrTests():
    printTitulo("Testeando guerraterritorios/models/cantones.py:")

    print("EsUnPais puede detectar si una lista cumple la estructura:")
    esUnPaisPuedeDetectarSiUnaListaCumpleLaEstructura()

    print("EsUnPais puede detectar si una lista no cumple la estructura:")
    esUnPaisPuedeDetectarSiUnaListaNoCumpleLaEstructura()

correrTests()
