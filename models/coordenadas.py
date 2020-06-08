import sys

sys.path.append("..")

from guerraterritorios.utils.utils import cumpleEstructura

coordenadas = [
    list,  # pos1
    list,  # pos2
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
    
    if not esUnaPosicion(lista[0]) and not esUnaPosicion(lista[1]):
        return False
    return True

# E: Una lista
# S: Un booleano
# D: Retorna True si cumple el modelo de posicion
def esUnaPosicion(lista):
    return cumpleEstructura(lista, pos)