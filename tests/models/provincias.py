import sys

sys.path.append("..")

from guerraterritorios.tests.testsFunctions import *
from guerraterritorios.models.provincias import *

def esUnaProvinciaPuedeDetectarSiUnaListaCumpleLaEstructura():
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

    esVerdadero(esUnaProvincia(provincia))

def esUnaProvinciaPuedeDetectarSiUnaListaNoCumpleLaEstructura():
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

    esFalso(esUnaProvincia(provincia))

def correrTests():
    printTitulo("Testeando guerraterritorios/models/cantones.py:")

    print("EsUnaProvincia puede detectar si una lista cumple la estructura:")
    esUnaProvinciaPuedeDetectarSiUnaListaCumpleLaEstructura()

    print("EsUnaProvincia puede detectar si una lista no cumple la estructura:")
    esUnaProvinciaPuedeDetectarSiUnaListaNoCumpleLaEstructura()

correrTests()
