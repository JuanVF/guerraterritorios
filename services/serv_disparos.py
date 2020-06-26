import sys

sys.path.append("..")

from guerraterritorios.services.serv_potencias import *
from guerraterritorios.services.serv_provincias import obtenerProvincias
from guerraterritorios.services.serv_cantones import obtenerCantones

from guerraterritorios.controller.mapa import *
from guerraterritorios.controller.registros import *

#Variable del modelo disparo
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

# E: Una coordenada, dos string
# S: Una lista del modelo disparo
# D: Se encarga de realizar el disparo, recibe el nombre del jugador
def disparar(coordenada, nombre, PATH):
    mapa = obtenerMapa(PATH)
    potenciaDisparo(nombre)
    datos = hayImpactoDisparo(coordenada, mapa)

    if datos != []:
        impacto = realizarImpacto(datos, nombre, coordenada)

        disparo = impacto[0]
        pais = impacto[1]

        realizarImpactoAMapa(mapa, pais, PATH)
    else:
        disparo = [nombre, "","","", coordenada[0], 0,0,False]

    guardarRegistroAtaque(disparo)

    return disparo

# E: Una lista, un string y una coordenada
# S: Una lista del modelo disparo
# D: Se encarga de realizar los detalles del impacto
def realizarImpacto(impacto, nombre, coordenada):
    danoProducido = calcularDano(impacto[0])

    disparo = [
                nombre, 
                impacto[0][0], 
                impacto[1][0], 
                impacto[2][0], 
                coordenada[0], 
                danoProducido[0],
                danoProducido[1][1],
                danoProducido[1],
                True]

    potencia = buscarPotenciaPorPais(impacto[0][0])

    if potencia != []:
        asignarDanoAPotencia(potencia, danoProducido)
        guardarRegistroTerritorio(danoProducido[1][0], potencia[0], danoProducido[1][1])

    return [disparo, danoProducido[1]]

# E: Una coordenada y una lista de paises
# S: Una lista
# D: Se encarga de determinar si hubo un impacto
def hayImpactoDisparo(coordenada, paises):
    cantonFake = ["Disparo", coordenada]
    
    for pais in paises:
        for provincia in pais[3]:
            for canton in provincia[1]:
                if hayTraslapacion(cantonFake, canton):
                    return [pais, provincia, canton]

    return []
    
# E: Una potencia, un pais
# S: Una lista
# D: Determina el dano que recibio la potencia tras el disparo
def calcularDano(pais):
    vidaAnterior = pais[1] / 100
    extensionTotal = pais[2]/vidaAnterior

    vidaActiva = (vidaAnterior-0.1)

    if vidaActiva < 0.0:
        vidaActiva = 0.0

    extensionActiva = extensionTotal * vidaActiva

    pais[1] = vidaActiva*100
    pais[2] = extensionActiva
    
    return [vidaAnterior*100, pais]


