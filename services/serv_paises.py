import sys

sys.path.append("..")

from guerraterritorios.models.paises import esUnPais
from guerraterritorios.services.serv_provincias import obtenerProvincias
from guerraterritorios.services.serv_cantones import obtenerCantonesDistintos
from guerraterritorios.utils import constantes as colores

# E: Una lista
# S: Un booleano
# D: Retorna True si la lista, solo contiene paises
def sonPaises(paises):
    for pais in paises:
        if not esUnPais(pais):
            return False
    
    return True

# E: Una lista de paises y un string
# S: Un pais
# D: Busca un pais y lo retorna
def buscarPais(paises, nombre):
    for pais in paises:
        if pais[0].lower() == nombre.lower():
            return pais
    
    return []


# E: Una lista de paises
# S:
# D: Imprime la lista de paises
def imprimirPaises(paises):
    for pais in paises:
        imprimirPais(pais)

# E: Un pais
# S:
# D: Imprime un pais
def imprimirPais(pais):
    provincias = obtenerProvincias([pais])
    cantones = obtenerCantonesDistintos(provincias)

    print(pais[0], end="\n\n")
    print(colores.WARNING,"Vida:",colores.NORMAL, pais[1],colores.WARNING,"Extension:",colores.NORMAL,pais[2],"km2",sep="  ")
    print(colores.WARNING, "cantidad de provincias:",colores.NORMAL,len(provincias),colores.WARNING, "cantidad de cantones distintos:",colores.NORMAL,len(cantones),sep="  ")