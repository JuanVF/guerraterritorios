import sys

sys.path.append("..")

from guerraterritorios.services.serv_disparos import disparar
from guerraterritorios.services.serv_potencias import buscarPotencias
from guerraterritorios.models.coordenadas import esUnaLatitud, esUnaLongitud

from guerraterritorios.utils.utils import clear, convertAInt
from guerraterritorios.utils import constantes as colores

potencias = buscarPotencias()

def menuDisparar(mapa, turno):
    if turno == -1:
        print("Lo sentimos... todas las potencias estan inactivas...")
        input("")
        return calcularTurno(turno)

    global potencias
    print(colores.WARNING, "Seccion de disparos!", colores.NORMAL, "\n")

    #TODO: Si tiene 0 misiles evitar que la potencia entre en el loop
    
    print("Es el turno de:",potencias[turno][0], " y le quedan", potencias[turno][2], "misiles!")
    
    confirmacion = input("Desea disparar un misil? Y/N: ")

    if confirmacion.lower() == "y":
        clear()
        latitud = obtenerLatitud()
        clear()
        Longitud = obtenerLongitud()

        coordenada = [[latitud, Longitud], [latitud, Longitud]]
        
        disparo = disparar(coordenada, mapa, potencias[turno][0])

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
        
        if potencias[turno][1]:
            avanzar = False

        if not potenciasActivas():
            return -1
    
    return turno

def potenciasActivas():
    estado = 0

    for potencia in potencias:
        if potencia[1]:
            estado += 1
    
    return estado != 0
            

def obtenerLatitud():
    print(colores.NORMAL, "Latitud", colores.NORMAL)
    grados = convertAInt(input("Inserte los grados:"))
    minutos = convertAInt(input("Inserte los minutos:"))
    segundos = convertAInt(input("Inserte los segundos:"))

    posicion = [grados, minutos, segundos]

    if grados == -1 or minutos == -1 or segundos == -1 or not esUnaLatitud(posicion):
        clear()
        print("Uno de los datos que ingreso no es correcto")
        return obtenerLatitud()
    else:
        return posicion

    return []

def obtenerLongitud():
    print(colores.NORMAL, "Longitud", colores.NORMAL)
    grados = convertAInt(input("Inserte los grados:"))
    minutos = convertAInt(input("Inserte los minutos:"))
    segundos = convertAInt(input("Inserte los segundos:"))

    posicion = [grados, minutos, segundos]

    if grados == -1 or minutos == -1 or segundos == -1 or not esUnaLongitud(posicion):
        clear()
        print("Uno de los datos que ingreso no es correcto")
        return obtenerLatitud()
    else:
        return posicion

    return []
