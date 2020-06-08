import sys

sys.path.append("..")

from guerraterritorios.models.provincias import esUnaProvincia
from guerraterritorios.utils.utils import cumpleEstructura

paises = [
    str,  # nombre
    float,  # vida
    float,  # extensionTotal
    list  # provincias : Lista de provincias
]

# E: Una lista
# S: Un booleano
# D: Retorna True si la lista cumple el modelo de paises
def esUnPais(lista):
    if not cumpleEstructura(lista, paises):
        return False
    
    for provincia in lista[3]:
        if not esUnaProvincia(provincia):
            return False

    return True