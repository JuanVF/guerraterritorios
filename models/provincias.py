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

def verificarNombresCantones(provincia):
    cantones = provincia[1]
    for i in range(0, cantones):
        for canton in cantones[i+1:]:
            if cantones[i][0] == canton[0]:
                return False
    
    return True