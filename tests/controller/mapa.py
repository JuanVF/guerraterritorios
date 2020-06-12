import sys

sys.path.append("..")

from guerraterritorios.controller.mapa import * 
from guerraterritorios.tests.testsFunctions import *

a = [ [[-10, 50, 3], [12, 30, 0]], [[95, 30, 0],[20, 59, 59]] ]
b = [ [[-20,30,2], [-10,49,3]], [[96,4,2],[40,8,6]] ]               #contiene a a
c = [ [[-10, 50, 3], [20, 59, 59]], [[-80, 8, 9],[70, 50, 30]] ]    #tiene un punto en comun con a, toca a b en el este
d = [ [[-93, 6, 7], [-10, 49, 8]], [[-80, 8, 10],[70, 50, 30]] ]    #no toca a c por 1s
e = [ [[-6, 8, 0], [19,8,7]], [[60, 3, 7],[-40, 50, 39]] ]          #toca a a y a b por el sur, no toca a c ni a d
f = [ [[80, 4,27], [90,8,41]], [[75, 13, 52],[-80, 0, 0]] ]         #no toca nada, esta suuuuper largo

#Caso1: B contien a A
def hayTraslapacionCaso1():
    cantonA = ["Upala", a]
    cantonB = ["San Carlos mi tierra", b]
    esVerdadero(hayTraslapacion(cantonB, cantonA))

#Caso2: C toca a A
def hayTraslapacionCaso2():
    cantonA = ["Upala", a]
    cantonB = ["San Carlos mi tierra", c]
    esVerdadero(hayTraslapacion(cantonA, cantonB))

#Caso3: D no toca a C
def hayTraslapacionCaso3():
    cantonA = ["Upala", d]
    cantonB = ["San Carlos mi tierra", c]
    esFalso(hayTraslapacion(cantonA, cantonB))

#Caso4: B no toca a C
def hayTraslapacionCaso4():
    cantonA = ["Upala", b]
    cantonB = ["San Carlos mi tierra", c]
    esVerdadero(hayTraslapacion(cantonA, cantonB))

#Caso5: e toca a a y a b por el sur, no toca a c ni a d
def hayTraslapacionCaso5():
    cantonA = ["Upala", a]
    cantonB = ["San Carlos mi tierra", b]
    cantonC = ["Liberia", c]
    cantonD = ["Turrialba", d]
    cantonE = ["Cartago", e]

    expected = [True, True, False, False]
    traslapaciones = [
        hayTraslapacion(cantonA, cantonE),
        hayTraslapacion(cantonA, cantonE),
        hayTraslapacion(cantonE, cantonC),
        hayTraslapacion(cantonD, cantonE)
    ]

    sonIguales(traslapaciones, expected)

def correrTests():
    printTitulo("Tests guerraterritorios/controller/mapa.py")

    print("Caso1: B contien a A:")
    hayTraslapacionCaso1()

    print("Caso2: C toca a A:")
    hayTraslapacionCaso2()

    print("Caso3: D no toca a C:")
    hayTraslapacionCaso3()

    print("Caso4: B no toca a C:")
    hayTraslapacionCaso4()

    print("Caso5: e toca a a y a b por el sur, no toca a c ni a d:")
    hayTraslapacionCaso5()

correrTests()