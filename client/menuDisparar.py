import sys

sys.path.append("..")

from guerraterritorios.services.serv_disparos import disparar
from guerraterritorios.services.serv_potencias import buscarPotencias
from guerraterritorios.models.coordenadas import esUnaLatitud, esUnaLongitud

from guerraterritorios.utils.utils import clear, convertAInt
from guerraterritorios.utils import constantes as colores

potencias = buscarPotencias()

def menuDisparar(mapa, turno, PATH_MAPA):
    global potencias
    potencias = buscarPotencias()

    if not hayPotenciasActivas():
        turno = -1
    elif turno == -1:
        turno = calcularTurno(turno)

    if turno == -1:
        print("No hay potencias vivas... inserte algunas para jugar")
        input("")
        return turno

    return menuDisparos(mapa, turno, PATH_MAPA)


def menuDisparos(mapa, turno, PATH_MAPA):
    global potencias
    print(colores.WARNING, "Seccion de disparos!", colores.NORMAL, "\n")
    
    print("Es el turno de:", potencias[turno][0], " y le quedan", potencias[turno][2], "misiles!")
    
    confirmacion = input("Desea disparar un misil? Y/N: ")

    if confirmacion.lower() == "y":
        return menuRealizarDisparo(mapa, turno, PATH_MAPA)

    return turno

def menuRealizarDisparo(mapa, turno, PATH_MAPA):
    global potencias
    clear()
    Longitud = obtenerLongitud()
    clear()
    latitud = obtenerLatitud()

    coordenada = [[Longitud, latitud], [Longitud, latitud]]
        
    disparo = disparar(coordenada, potencias[turno][0], PATH_MAPA)

    if disparo[7]:
        print(disparo[0], "acerto el disparo! en:")
        print(disparo[1],disparo[2], disparo[3], sep=",",end="\n\n")
        print("Ahora tiene:", disparo[6], "% de vida")
    else:
        print("Lo lamentamos, no acerto su disparo!")
    input("\n\n Presione cualquier tecla para volver...")

    return calcularTurno(turno)

def calcularTurno(turno):
    avanzar = True
    length = len(potencias) - 1

    while avanzar:
        turno += 1

        if turno > length:
            turno = 0
        
        if not hayPotenciasActivas():
            return -1

        if potencias[turno][1]:
            avanzar = False
    
    return turno

def hayPotenciasActivas():
    for potencia in potencias:
        if potencia[1]:
            return True
    
    return False
            

def obtenerLatitud():
    print(colores.NORMAL, "Latitud", colores.NORMAL)
    grados = convertAInt(input("Inserte los grados:"), neg=True)
    minutos = convertAInt(input("Inserte los minutos:"), neg=True)
    segundos = convertAInt(input("Inserte los segundos:"), neg=True)

    posicion = [grados, minutos, segundos]

    if grados == "Error" or minutos == "Error" or segundos == "Error" or not esUnaLatitud(posicion):
        clear()
        print("Uno de los datos que ingreso no es correcto")
        return obtenerLatitud()
    else:
        return posicion

    return []

def obtenerLongitud():
    print(colores.NORMAL, "Longitud", colores.NORMAL)
    grados = convertAInt(input("Inserte los grados:"), neg=True)
    minutos = convertAInt(input("Inserte los minutos:"), neg=True)
    segundos = convertAInt(input("Inserte los segundos:"), neg=True)

    posicion = [grados, minutos, segundos]

    if grados == "Error" or minutos == "Error" or segundos == "Error" or not esUnaLongitud(posicion):
        clear()
        print("Uno de los datos que ingreso no es correcto")
        return obtenerLatitud()
    else:
        return posicion

    return []
