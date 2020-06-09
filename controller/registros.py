import sys

sys.path.append("..")

from guerraterritorios.models.disparos import esUnDisparo
from guerraterritorios.models.potencias import esUnaPotencia
from guerraterritorios.controller.operaciones import *
from guerraterritorios.utils.constantes import REGISTROS_PATH
from guerraterritorios.utils.utils import obtenerFecha

tiposRegistro = [
    "ATAQUE",
    "COMPRA",
    "CAMBIO",
    "MUERTE",
    "TERRITORIO"
]

# E: 
# S: Una lista
# D: Lee los registros y retorna una lista con todos los registros
def leerRegistros():
    registros = eval(leer(REGISTROS_PATH))

    return registros

# E: Lista del modelo disparo
# S: Un booleano
# D: Guarda en registros.log informacion acerca de un disparo, retorna True si se guardo bien
def guardarRegistroAtaque(disparo):
    if not esUnDisparo(disparo):
        return False

    formatoCoordenadas = "("+ str(disparo[4][0][0]) + "," + str(disparo[4][0][1]) + "," + str(disparo[4][0][2]) +"), ("+ str(disparo[4][1][0]) + "," + str(disparo[4][1][1]) + "," + str(disparo[4][1][2]) +")"

    if disparo[7]:
        formato = disparo[0] + " disparo en " + formatoCoordenadas + " atino a " + disparo[1] + " en " + disparo[2] + ", " + disparo[3] + ". " + disparo[1] + " paso de " + str(disparo[5]) + "% a " + str(disparo[6]) + "%"
    else:
        formato = disparo[0] + " disparo en " + formatoCoordenadas + " no atino"

    registro = leerRegistros()
    registro += [[obtenerFecha(), tiposRegistro[0], formato]]
    registro = str(registro)

    return guardar(REGISTROS_PATH, registro)

# E: Una lista del modelo potencia
# S: Un booleano
# D: Guarda en registros.log informacion acerca del cambio de estado de una potencia
#   retorna True si se guardo bien
def guardarRegistroCambio(potencia):
    if not esUnaPotencia(potencia)
        return False
    
    formato = potencia[0] + " paso a " + potencia[1]

    registro = leerRegistros()
    registro += [[obtenerFecha(), tiposRegistro[2], formato]]

    return guardar(REGISTROS_PATH, registro)

# E: Un string e int
# S: Un booleano
# D: Guarda en registros.log informacion acerca de una compra de misiles
#   retorna True si se guardo bien
def guardarRegistroCompra(nombre, cant):
    return True

# E: Una lista del modelo potencia
# S: Un booleano
# D: Guarda en registros.log informacion acerca de la muerte de una potencia
#   retorna True si se guardo bien
def guardarRegistroMuerte(potencia):
    return True

# E: Una lista del modelo pais
# S: Un booleano
# D: Guarda en registros.log informacion acerca del estado de un territorio
#   retorna True si se guardo bien
def guardarRegistroTerritorio(pais):
    return True
