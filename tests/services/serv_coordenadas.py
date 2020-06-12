import sys

sys.path.append("..")

from guerraterritorios.services.serv_coordenadas import *
from guerraterritorios.tests.testsFunctions import *

#Caso1: posicion1 == posicion2
def coompararPosicionPuedeValorarCaso1():
    posicion = [90, 40, 20]

    posicionM = compararPosicion(posicion, posicion)

    sonIguales(posicion, posicionM)

#Caso2: grado1 > grado2    
def coompararPosicionPuedeValorarCaso2():
    posicion1 = [90, 40, 20]
    posicion2 = [-29, 20, 30]

    posicionM = compararPosicion(posicion1, posicion2)

    sonIguales(posicionM, posicion1)

#Caso3: grado1 < grado2    
def coompararPosicionPuedeValorarCaso3():
    posicion1 = [-29, 20, 30]
    posicion2 = [90, 40, 20]

    posicionM = compararPosicion(posicion1, posicion2)

    sonIguales(posicionM, posicion2)

#Caso4: minuto1 > minuto2
def coompararPosicionPuedeValorarCaso4():
    posicion1 = [90, 20, 20]
    posicion2 = [90, 10, 20]

    posicionM = compararPosicion(posicion1, posicion2)

    sonIguales(posicionM, posicion1)

#Caso5: minuto1 < minuto2
def coompararPosicionPuedeValorarCaso5():
    posicion1 = [90, 10, 20]
    posicion2 = [90, 20, 20]

    posicionM = compararPosicion(posicion1, posicion2)

    sonIguales(posicionM, posicion2)

#Caso6: segundo1 > segundo2
def coompararPosicionPuedeValorarCaso6():
    posicion1 = [90, 20, 20]
    posicion2 = [90, 20, 5]

    posicionM = compararPosicion(posicion1, posicion2)

    sonIguales(posicionM, posicion1)

#Caso6: segundo1 < segundo2
def coompararPosicionPuedeValorarCaso7():
    posicion1 = [90, 20, 4]
    posicion2 = [90, 20, 20]

    posicionM = compararPosicion(posicion1, posicion2)

    sonIguales(posicionM, posicion2)

def crearUnidadConvierteCorrectamente():
    posicion = [90, 20, 4]
    expected = 902004

    sonIguales(crearUnidad(posicion), expected)

def crearUnidadValidaCeros():
    posicion = [0, 20, 4]
    expected = 2004

    sonIguales(crearUnidad(posicion), expected)

def puedeObtenerLatitud():
    coordenada = [[-10, 50, 3], [12, 30, 0]]

    sonIguales(obtenerLatitud(coordenada), [12, 30, 0])

def puedeObtenerLongitud():
    coordenada = [[-10, 50, 3], [12, 30, 0]]

    sonIguales(obtenerLongitud(coordenada), [-10, 50, 3])

def crearUnidadValidaNegativos():
    posicion = [-10, 50, 3]

    sonIguales(crearUnidad(posicion), -105003)
    
def correrTests():
    printTitulo("Testeando guerraterritorios/services/serv_posicions.py")

    print("Caso 1: posicion1 == posicion2:")
    coompararPosicionPuedeValorarCaso1()

    print("Caso 2: grado1 > grado2:")
    coompararPosicionPuedeValorarCaso2()

    print("Caso 3: grado1 < grado2:")
    coompararPosicionPuedeValorarCaso3()

    print("Caso 4: minuto1 > minuto2:")
    coompararPosicionPuedeValorarCaso4()

    print("Caso 5: minuto1 < minuto2:")
    coompararPosicionPuedeValorarCaso5()

    print("Caso 6: segundo1 > segundo2:")
    coompararPosicionPuedeValorarCaso6()

    print("Caso 7: segundo1 < segundo2:")
    coompararPosicionPuedeValorarCaso7()

    print("Crear Unidades puede convertir correctamente:")
    crearUnidadConvierteCorrectamente()

    print("Crear unidades puede validar 0s:")
    crearUnidadValidaCeros()

    print("Crear unidades puede validar negativos:")
    crearUnidadValidaNegativos()

    print("Puede obtener la latitud de una coordenada")
    puedeObtenerLatitud()

    print("Puede obtener la longitud de una coordenada")
    puedeObtenerLongitud()

correrTests()