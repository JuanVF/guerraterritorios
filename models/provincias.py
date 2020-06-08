import sys

sys.path.append("..")

from guerraterritorios.models.cantones import esUnCanton
from guerraterritorios.utils.utils import cumpleEstructura

provincias = [
    str,  # nombre,
    list,  # cantones
]

# E: Una lista
# S: Un booleano
# D: Retorna True si la lista cumple el modelo de provincia
def esUnaProvincia(lista):
    if not cumpleEstructura(lista, provincias):
        return False

    for canton in lista[1]:
        if not esUnCanton(canton):
            return False

    return True