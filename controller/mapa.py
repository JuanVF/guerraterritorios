import sys

sys.path.append("..")

from guerraterritorios.services.serv_cantones import *

# E: Dos listas de coordenadas, (deben pertenecer al modelo canton)
# S: Booleano
# D: Verifica que ningun territorio se traslape sobre otro
def hayTraslapacion(cuadrante1, cuadrante2):
    lat1 = obtenerLatitudes(cuadrante1)
    lat2 = obtenerLatitudes(cuadrante2)

    long1 = obtenerLongitudes(cuadrante1)
    long2 = obtenerLongitudes(cuadrante2)

    for longitud in long2:
        if crearUnidad(long1[0]) <= crearUnidad(longitud) and crearUnidad(longitud) <= crearUnidad(long1[1]):
            for latitud in lat2:
                if lat1[0] <= latitud and latitud <= lat1[1]:
                    return True

    return False

# E:
# S: Booleano
# D: Verifica que el mapa de territorios contenga la estructura de listas adecuada
def verificarEstructuraMapa():
    return True
