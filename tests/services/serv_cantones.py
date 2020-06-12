import sys

sys.path.append("..")

from guerraterritorios.services.serv_cantones import *
from guerraterritorios.tests.testsFunctions import *

a = [ [[-10, 50, 3], [12, 30, 0]], [[95, 30, 0],[20, 59, 59]] ]

def puedeObtenerLatitudes():
    canton = ["San Carlos mi linda tierra", a]

    sonIguales(obtenerLatitudes(canton), [[12, 30, 0], [20, 59, 59]])

def puedeObtenerLongitudes():
    canton = ["San Carlos mi linda tierra", a]

    sonIguales(obtenerLongitudes(canton), [[-10, 50, 3], [95, 30, 0]])

def correrTests():
    printTitulo("Testeando guerraterritorios/services/serv_cantones.py")

    print("Puede obtener latitudes:")
    puedeObtenerLatitudes()
    
    print("Puede obtener longitudes:")
    puedeObtenerLongitudes()

correrTests()