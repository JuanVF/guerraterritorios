import sys

sys.path.append("..")

from guerraterritorios.services.serv_potencias import buscarPotencias, asignarDanoAPotencia, buscarPotenciaPorPais
from guerraterritorios.services.serv_provincias import obtenerProvincias
from guerraterritorios.services.serv_cantones import obtenerCantones
from guerraterritorios.controller.mapa import hayTraslapacion
from guerraterritorios.controller.registros import guardarRegistroAtaque

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

# E: Una coordenada, una lista de paises, un string
# S: Una lista del modelo disparo
# D: Se encarga de realizar el disparo, recibe el nombre del jugador
def disparar(coordenada, mapa, nombre):
    impacto = hayImpactoDisparo(coordenada, mapa)

    if impacto != []:
        danoProducido = calcularDano(impacto[0])

        disparo = [
                    nombre, 
                    impacto[0][0], 
                    impacto[1][0], 
                    impacto[2][0], 
                    coordenada[0], 
                    danoProducido[0],
                    danoProducido[1],
                    danoProducido[2],
                    True]

        potencia = buscarPotenciaPorPais(impacto[0][0])
        #TODO: Falta: Agregar impactos recibidos, misiles, impactos dados!
        if potencia != []:
            asignarDanoAPotencia(potencia, danoProducido)

    else:
        disparo = [nombre, "","","", coordenada[0], 0,0,False]

    guardarRegistroAtaque(disparo)

    return disparo

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

    return [vidaAnterior*100, vidaActiva*100, pais]


