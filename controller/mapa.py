import sys

sys.path.append("..")

from guerraterritorios.services.serv_cantones import *
from guerraterritorios.services.serv_provincias import *
from guerraterritorios.services.serv_paises import *
from guerraterritorios.controller.operaciones import *
from guerraterritorios.utils.constantes import *

codigosError = [
    [0, "No hay error!"],
    [1, "El mapa no contiene la estructura correcta de paises"],
    [2, "La siguiente lista se traslapa", []]
]

# E: Un string
# S: Una lista de territorios
# D: Dada la ruta de un mapa, lo carga y lo retorna, retorna [] si hay error o esta vacia
def obtenerMapa(PATH):
    try:
        mapa = eval(leer(PATH))

        return mapa
    except:
        return []


# E: Dos listas de coordenadas, (deben pertenecer al modelo canton)
# S: Booleano
# D: Verifica si un area esta contenida en otra
def estaContenido(cuadrante1, cuadrante2):
    lat1 = obtenerLatitudes(cuadrante1)
    lat2 = obtenerLatitudes(cuadrante2)

    long1 = obtenerLongitudes(cuadrante1)
    long2 = obtenerLongitudes(cuadrante2)

    for longitud in long2:
        if crearUnidad(long1[0]) <= crearUnidad(longitud) and crearUnidad(longitud) <= crearUnidad(long1[1]):
            for latitud in lat2:
                if lat1[0] <= latitud and latitud <= lat1[1]:
                    return True

    return False

# E: Dos listas de coordenadas, (deben pertenecer al modelo canton)
# S: Booleano
# D: Verifica primero si el primer cuadrante esta contenido en el segundo, para evitar hacer 
#    Comparaciones innecesarias, si no, se verifica si el segundo contiene al primero
def hayTraslapacion(cuadrante1, cuadrante2):
    if estaContenido(cuadrante1, cuadrante2):
        return True

    return estaContenido(cuadrante2, cuadrante1)

# E: Una lista de paises
# S: Booleano
# D: Verifica que el 
def hayTraslapacionEnMapa(paises):
    provincias = obtenerProvincias(paises)
    cantones = obtenerCantones(provincias)
    
    for i in range(0, len(cantones)):
        for canton in cantones[i+1:]:
            if hayTraslapacion(cantones[i], canton):
                return True
    
    return False

# E: Una lista de paises
# S: Una lista
# D: Verifica que el mapa de territorios contenga la estructura de listas adecuada
def verificarEstructuraMapa(paises):
    if not sonPaises(paises):
        return codigosError[1]

    if hayTraslapacionEnMapa(paises):
        return codigosError[2]
        
    return codigosError[0]

# E: Una lista del modelo pais
# S: Un entero positivo
# D: Retorna la extension de un solo pais
def calcularExtension(pais):
    cantones = obtenerCantones(pais[3])
    extensionT = 0

    for canton in cantones:
        latitudes = obtenerLatitudes(canton)
        longitudes = obtenerLongitudes(canton)

        dLatitudes = calcularDistancia(latitudes)
        dLongitudes = calcularDistancia(longitudes)

        extension = dLatitudes[0]*GRADO + dLatitudes[1]*MINUTOS + dLatitudes[2]*SEGUNDOS
        extension *= (dLongitudes[0]*GRADO + dLongitudes[1]*MINUTOS + dLongitudes[2]*SEGUNDOS)

        extensionT += extension
        
    return extensionT

# E: Una lista de coordenadas
# S: Un entero positivo
# D: Calcula la distancia entre dos coordenadas
def calcularDistancia(coordenadas):
    posicion1 = calcularSegundos(coordenadas[0])
    posicion2 = calcularSegundos(coordenadas[1])

    distancia = abs(posicion1 - posicion2)

    return segundosAPosicion(distancia)

# E: Una posicion
# S: Un entero positivo
# D: Convierte una posicion a segundos
def calcularSegundos(posicion):
    segundos = posicion[0] * 3600 + posicion[1] * 60 + posicion[2]

    return segundos

# E: Un entero positivo
# S: Una posicion
# D: Convierte segundos a una posicion
def segundosAPosicion(segundos):
    minutos = segundos // 60
    segundos = segundos % 60
    grados = minutos // 60
    minutos = minutos % 60
        
    return [grados, minutos, segundos]
