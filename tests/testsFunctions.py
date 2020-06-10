import sys

sys.path.append("..")

from guerraterritorios.utils import constantes as colores

def printTitulo(string):
    print(colores.WARNING + string + "\n" + colores.NORMAL)

def printPass():
    print(colores.SUCCESS+ "PASS" + colores.NORMAL + "\n")

def printFail(received, expected):
    print(colores.FAIL + "FAIL: " + colores.NORMAL + " se recibio: " + str(received) + " y se esperaba " + str(expected) + "\n")

def sonIguales(var1, var2):
    if var1 == var2:
        printPass()
    else:
        printFail(var1, var2)

def esVerdadero(var):
    if var:
        printPass()
    else:
        printFail(var, True)

def esFalso(var):
    if not var:
        printPass()
    else:
        printFail(var, False)

def esUnString(string):
    if type(string) == str:
        printPass()
    else:
        printFail(type(string), str)

def esUnaLista(lista):
    if type(lista) == list:
        printPass()
    else:
        printFail(type(lista), list)

def esMayorQue(num1, num2):
    if num1 > num2:
        printPass()
    else:
        printFail(num1, num2)