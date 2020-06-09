import sys

sys.path.append("..")

from guerraterritorios.utils.utils import cumpleEstructura
from guerraterritorios.models.coordenadas import esUnaCoordenada

cantones = [
    str,  # nombre
    list,  # coordenadas
]

# E: Una lista
# S: Un booleano
# D: Retorna true si cumple con el modelo de cantones
def esUnCanton(lista):
    if not cumpleEstructura(lista, cantones):
        return False

    if len(lista[1]) != 2:
        return False

    if not esUnaCoordenada(lista[1][0]) and not esUnaCoordenada(lista[1][1]):
        return False

    return True