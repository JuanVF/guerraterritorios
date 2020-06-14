import sys

sys.path.append("..")

from guerraterritorios.services.serv_coordenadas import *

# E: Una lista del modelo canton
# S: Una lista de coordenadas
# D: Dado un canton, devuelve una lista con sus dos latitudes
def obtenerLatitudes(canton):
    latitudes = []

    latitudes += [obtenerLatitud(canton[1][0])]
    latitudes += [obtenerLatitud(canton[1][1])]

    return obtenerListaOrdenada(latitudes)

# E: Una lista del modelo canton
# S: Una lista de coordenadas
# D: Dado un canton, devuelve una lista con sus dos latitudes
def obtenerLongitudes(canton):
    longitud = []

    longitud += [obtenerLongitud(canton[1][0])]
    longitud += [obtenerLongitud(canton[1][1])]

    return obtenerListaOrdenada(longitud)

# E: Una lista de provincias
# S: Una lista de cantones
# D: Dada una lista de provincias retorna una lista de cantones
def obtenerCantones(provincias):
    cantones = []

    for provincia in provincias:
        cantones += provincia[1]
    
    return cantones