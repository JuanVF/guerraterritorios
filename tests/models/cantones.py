import sys

sys.path.append("..")

from guerraterritorios.tests.testsFunctions import *
from guerraterritorios.models.cantones import *

def esUnCantonPuedeDetectarSiNoHayLatitudOLongitud():
    canton = [
        "Upala",
        [
            [
                [10, 20, 30],
                [10,50, 53]
            ]
        ]
    ]

    esFalso(esUnCanton(canton))

def esUnCantonPuedeDetectarSiHayMasDeTresCoordenadas():
    canton = [
        "Upala",
        [
            [
                [10, 20, 30],
                [10,50, 53]
            ],
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

    esFalso(esUnCanton(canton))

def esUnCantonPuedeDetectarUnaListaQueCumpleElModelo():
    canton = [
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

    esVerdadero(esUnCanton(canton))

def correrTests():
    printTitulo("Testeando guerraterritorios/models/cantones.py:")

    print("EsUnCanton puede detectar si no hay latitud o longitud en la lista:")
    esUnCantonPuedeDetectarSiNoHayLatitudOLongitud()
    
    print("EsUnCanton puede detectar si no hay mas de tres coordenadas:")
    esUnCantonPuedeDetectarSiHayMasDeTresCoordenadas()

    print("EsUnCanton puede detectar una lista que cumple el modelo:")
    esUnCantonPuedeDetectarUnaListaQueCumpleElModelo()

correrTests()
