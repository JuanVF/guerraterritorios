import sys

sys.path.append("..")

from guerraterritorios.tests.testsFunctions import *
from guerraterritorios.services.serv_potencias import *

def guardarPotenciaPuedeValidarDatosIncorrectos():
    nombre = "U.R.S.S" 
    estado = "no activo"
    cantMisiles = 600
    vida = 99.0
    estadoVida = True

    esFalso(guardarPotencia(nombre, estado, vida, cantMisiles, estadoVida))

def guardarPotenciaPuedeGuardarUnaPotencia():
    nombre = "U.R.S.S" 
    estado = "inactivo"
    cantMisiles = 600
    vida = 100.0
    estadoVida = True
    
    esVerdadero(guardarPotencia(nombre, estado, vida, cantMisiles, estadoVida))

def buscarPotenciasPuedeRecibirDatosCorrectamente():
    potencias = buscarPotencias()

    esMayorQue(len(potencias), 0)

def buscarPotenciaPuedeEncontrarUnaPotencia():
    potencia = buscarPotencia("U.R.S.S")

    esMayorQue(len(potencia), 0)

def actualizarPotenciaPuedeActualizarCorrectamente():
    potencia = buscarPotencia("U.R.S.S")
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
    potencia[7] = [pais]

    esVerdadero(actualizarPotencia(potencia))    

def cambiarEstadoPuedeActualizarCorrectamente():
    potencia = buscarPotencia("U.R.S.S")

    esVerdadero(cambiarEstado(potencia[0], "activo"))

def sePuedenComprarMisilesCorrectamente():
    potencia = buscarPotencia("U.R.S.S")

    esVerdadero(comprarMisiles(potencia[0], 200))

def correrTests():
    printTitulo("Testeando guerrapotencias/services/serv_potencias.py")

    print("GuardarPotencia puede validar datos incorrectos")
    guardarPotenciaPuedeValidarDatosIncorrectos()

    print("GuardarPotencia puede guardar correctamente")
    guardarPotenciaPuedeGuardarUnaPotencia()

    print("BuscarPotencias retorna todas las potencias")
    buscarPotenciasPuedeRecibirDatosCorrectamente()

    print("BuscarPotencias puede encontrar una potencia por su nombre")
    buscarPotenciaPuedeEncontrarUnaPotencia()
    
    print("ActualizarPotencia puede actualizar correctamente")
    actualizarPotenciaPuedeActualizarCorrectamente()

    print("CambiarEstado puede actualizar el estado correctamente")
    cambiarEstadoPuedeActualizarCorrectamente()

    print("comprarMisiles puede pagar los misiles correctamente")
    sePuedenComprarMisilesCorrectamente()

correrTests()