import sys

sys.path.append("..")

from guerraterritorios.models.paises import esUnPais
from guerraterritorios.services.serv_provincias import obtenerProvincias
from guerraterritorios.services.serv_cantones import obtenerCantonesDistintos
from guerraterritorios.utils import constantes as colores
from guerraterritorios.controller.operaciones import *

# E: Un string
# S: Una lista de territorios
# D: Dada la ruta de un mapa, lo carga y lo retorna, retorna [] si hay error o esta vacia
def obtenerPaises(PATH):
    try:
        paises = eval(leer(PATH))

        return paises
    except:
        return []

# E: Un string y una lista de paises
# S: Un booleano
# D: Se encarga de guardar un mapa
def guardarPaises(PATH, paises):
    paises = str(paises)

    return guardar(PATH, paises)

# E: Una lista
# S: Un booleano
# D: Retorna True si la lista, solo contiene paises
def sonPaises(paises):
    for pais in paises:
        if not esUnPais(pais):
            return False
    
    return True

def hayNombresRepetidos(paises):
    for i in range(0, len(paises)):
        for pais in paises[i+1:]:
            if paises[i][0].lower() == pais[0].lower():
                return True
    
    return False

# E: Una lista de paises y un string
# S: Un pais
# D: Busca un pais y lo retorna
def buscarPais(paises, nombre):
    for pais in paises:
        if pais[0].lower() == nombre.lower():
            return pais
    
    return []

# E: Un pais, un string
# S: Un booleano
# D: Actualiza un pais
def actualizarPaises(pais, PATH):
    paises = obtenerPaises(PATH)

    for i in range(0, len(paises)):
        if paises[i][0] == pais[0]:
            paises[i] = pais

    return guardarPaises(PATH, paises)

# E: Una lista de paises
# S:
# D: Imprime la lista de paises
def imprimirPaises(paises):
    for pais in paises:
        imprimirPais(pais)

# E: Una lista de paises, un int y un string
# S: Una pais
# D: Busca un territorio cuya vida sea apta para pagar los misiles y retorna la lista de paises
#    la retorna igual si no puede pagar
def pagarMisiles(paises, porcentaje):
    for pais in paises:

        vida = pais[1] / 100
        areaTotal = pais[2] / vida
        
        precio = areaTotal * porcentaje
        
        disponible = pais[2]
        
        if disponible >= precio:
            pais[1] = ((disponible - precio) / areaTotal)*100
            pais[2] = disponible - precio

            return pais
    
    return []

# E: Un pais
# S:
# D: Imprime un pais
def imprimirPais(pais):
    provincias = obtenerProvincias([pais])
    cantones = obtenerCantonesDistintos(provincias)

    print(pais[0], end="\n\n")
    print(colores.WARNING,"Vida:",colores.NORMAL, pais[1],colores.WARNING,"Extension:",colores.NORMAL,pais[2],"km2",sep="  ")
    print(colores.WARNING, "cantidad de provincias:",colores.NORMAL,len(provincias),colores.WARNING, "cantidad de cantones distintos:",colores.NORMAL,len(cantones),sep="  ")