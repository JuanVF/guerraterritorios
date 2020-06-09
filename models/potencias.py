import sys

sys.path.append("..")

from guerraterritorios.utils.utils import cumpleEstructura
from guerraterritorios.models.paises import esUnPais

potencias = [
    str,  # nombre
    str,  # estado
    int,  # cantMisiles
    int,  # cantDisparos
    int,  # cantImpRec,
    float,  # vida
    bool,  # estadoVida
    list  # lista de paises o territorios
]

# E: Una lista
# S: Un booleano
# D: Dada una lista retorna True si cumple la estructura de potencias
def esUnaPotencia(lista):
    if not cumpleEstructura(lista, potencias):
        return False

    for pais in lista[7]:
        if not esUnPais(pais):
            return False
            
    return True