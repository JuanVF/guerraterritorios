import sys

sys.path.append("..")

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
    print(disparo[4])
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
    if not esUnaPotencia(potencia):
        return False
    
    if not potencia[1]:
        formato = potencia[0] + " paso a Activo"
    else:
        formato = potencia[0] + " paso a Inactivo"

    registro = leerRegistros()
    registro += [[obtenerFecha(), tiposRegistro[2], formato]]
    
    registro = str(registro)

    return guardar(REGISTROS_PATH, registro)

# E: Un string (debe ser la variable nombre del modelo potencia) e int mayor o igual que 100
#    y menor o igual que 1000
# S: Un booleano
# D: Guarda en registros.log informacion acerca de una compra de misiles
#   retorna True si se guardo bien
def guardarRegistroCompra(nombre, cant):
    formato = nombre + " compro " + str(cant) + " misiles."

    registro = leerRegistros()
    registro += [[obtenerFecha(), tiposRegistro[1], formato]]
    registro = str(registro)

    return guardar(REGISTROS_PATH, registro)

# E: Un string, que debe ser la variable nombre del modelo potencia
# S: Un booleano
# D: Guarda en registros.log informacion acerca de la muerte de una potencia
#   retorna True si se guardo bien
def guardarRegistroMuerte(nombre):
    formato = nombre.upper()

    registro = leerRegistros()
    registro += [[obtenerFecha(), tiposRegistro[3], formato]]

    registro = str(registro)

    return guardar(REGISTROS_PATH, registro)

# E: Un string (debe ser la variable nombre del modelo potencia)
#    Un string (debe ser la variable nombre del modelo pais)
#    Un string (debe ser la variable nombre del modelo canton)
#    Un float (debe ser la variable vida del modelo pais)
# S: Un booleano
# D: Guarda en registros.log informacion acerca del estado de un territorio
#   retorna True si se guardo bien
def guardarRegistroTerritorio(potencia, pais, vida):
    localizacion = potencia + ", " + pais

    formato = localizacion + " paso a " + str(vida) + "%"

    registro = leerRegistros()
    registro += [[obtenerFecha(), tiposRegistro[4], formato]]

    registro = str(registro)

    return guardar(REGISTROS_PATH, registro)

# E/S:
# D: Imprime todos los registros del juego
def consultarHistorico():
    registros = leerRegistros()

    for registro in registros:
        print(registro[0], registro[1], registro[2], sep="  ", end="\n\n")