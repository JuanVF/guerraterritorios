import sys

sys.path.append("..")

from guerraterritorios.models.coordenadas import esUnaCoordenada
from guerraterritorios.utils.utils import cumpleEstructura

disparos = [
    str,  # atacante
    str,  # pais,
    str,  # provincia
    str,  # canton
    list, #coordenada
    float,  # vidaAnterior
    float,  # vidaActual
    bool,  # atino
]

# E: Una lista
# S: Un booleano
# D: Retorna True si la lista cumple el modelo de disparo
def esUnDisparo(lista):
    if not cumpleEstructura(lista, disparos):
        return False

    if not esUnaCoordenada(lista[4]):
        return False

    return True
