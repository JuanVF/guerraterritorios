import sys

sys.path.append("..")

from guerraterritorios.utils.utils import cumpleEstructura

coordenadas = [
    list,  # longitud
    list,  # latitud
]

pos = [
    int,  # grados
    int,  # minutos
    int  # segundos
]

# E: Una lista
# S: Un booleano
# D: Retorna True si cumple el modelo de coordenadas
def esUnaCoordenada(lista):
    if not cumpleEstructura(lista, coordenadas):
        return False
    
    if not esUnaLongitud(lista[0]) or not esUnaLatitud(lista[1]):
        return False
    return True

# E: Una lista
# S: Un booleano
# D: Retorna True si cumple el modelo de posicion
def esUnaLatitud(lista):
    if not cumpleEstructura(lista, pos):
        return False

    grados = lista[0]
    minutos = lista[1]
    segundos = lista[2]

    if -90 > grados or grados > 90:
        return False
    
    if 0 > segundos or segundos > 59:
        return False
    
    if 0 > minutos or minutos > 59:
        return False

    return True

# E: Una lista
# S: Un booleano
# D: Retorna True si cumple el modelo de posicion
def esUnaLongitud(lista):
    if not cumpleEstructura(lista, pos):
        return False

    grados = lista[0]
    minutos = lista[1]
    segundos = lista[2]

    if -180 > grados or grados > 180:
        return False
    
    if 0 > segundos or segundos > 59:
        return False
    
    if 0 > minutos or minutos > 59:
        return False

    return True