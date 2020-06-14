import sys

sys.path.append("..")

from guerraterritorios.models.paises import esUnPais

# E: dos strings
# S: una lista
# D: Retorna una lista de paises segun el nombre
def obtenerPais(nombre):
    pais = []

    return pais

# E: Una lista
# S: Un booleano
# D: Retorna True si la lista, solo contiene paises
def sonPaises(paises):
    for pais in paises:
        if not esUnPais(pais):
            return False
    
    return True