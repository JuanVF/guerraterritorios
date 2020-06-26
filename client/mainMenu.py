import sys

sys.path.append("..")

from guerraterritorios.utils import constantes as colores
from guerraterritorios.utils.utils import clear, convertAInt
from guerraterritorios.services.serv_potencias import consultarPotencias
from guerraterritorios.controller.registros import consultarHistorico

#Menus
from guerraterritorios.client.menuEstado import menuCambiarEstado
from guerraterritorios.client.menuComprar import menuComprarMisiles
from guerraterritorios.client.menuConsultas import menuConsultas
from guerraterritorios.client.menuPotencias import menuInsertarPotencias
from guerraterritorios.client.menuDisparar import menuDisparar

turno = 0

# E: Una lista de paises y un string
# S:
# D: Menu Inicial del juego!
def seleccionMenu(mapa, PATH_MAPA):
    global turno
    print(colores.WARNING, "Seleccione una opcion:", colores.NORMAL)
    print("___")
    print("|1| - Cambiar estado")
    print("|2| - Comprar misiles")
    print("|3| - Consultas")
    print("|4| - Disparar")
    print("|5| - Insertar potencia")
    print("|6| - Consultar potencias")
    print("|7| - Consultar registros")
    print("|0| - Salir")
    print("---")

    opt = input(colores.WARNING+"Escriba su opcion:"+colores.NORMAL)
    opt = convertAInt(opt)
    
    clear()
    if opt == 1:
        menuCambiarEstado()
    elif opt == 2:
        menuComprarMisiles(PATH_MAPA)
    elif opt == 3:
        menuConsultas(mapa)
    elif opt == 4:
        turno = menuDisparar(mapa, turno, PATH_MAPA)
    elif opt == 5:
        menuInsertarPotencias()
    elif opt == 6:
        consultarPotencias()
        input("Presione enter para volver...")
    elif opt == 7:
        consultarHistorico()
        input("Presione enter para volver...")
    elif opt == 0:
        exitLogo()
        return
    else:
        print(colores.FAIL,"Inserte una opcion valida...", colores.NORMAL)
        seleccionMenu(mapa, PATH_MAPA)
    clear()
    seleccionMenu(mapa, PATH_MAPA)

#D: Imprime el logo del juego
def logoJuego():
    print("░██████╗░██╗░░░██╗███████╗██████╗░██████╗░░█████╗░")
    print("██╔════╝░██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗")
    print("██║░░██╗░██║░░░██║█████╗░░██████╔╝██████╔╝███████║")
    print("██║░░╚██╗██║░░░██║██╔══╝░░██╔══██╗██╔══██╗██╔══██║")
    print("╚██████╔╝╚██████╔╝███████╗██║░░██║██║░░██║██║░░██║")
    print("░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝")
    print("████████╗███████╗██████╗░██████╗░██╗████████╗░█████╗░██████╗░██╗░█████╗░░██████╗")
    print("╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝")
    print("░░░██║░░░█████╗░░██████╔╝██████╔╝██║░░░██║░░░██║░░██║██████╔╝██║██║░░██║╚█████╗░")
    print("░░░██║░░░██╔══╝░░██╔══██╗██╔══██╗██║░░░██║░░░██║░░██║██╔══██╗██║██║░░██║░╚═══██╗")
    print("░░░██║░░░███████╗██║░░██║██║░░██║██║░░░██║░░░╚█████╔╝██║░░██║██║╚█████╔╝██████╔╝")
    print("░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═════╝░")
    print("\n\n")

#D: Imprime el logo de salida
def exitLogo():
    print("───▄▀▌─▄▄▄▄")
    print("──▄█▀──▌─▌─▌─▄▄▄▄")
    print("▄▀─█▄──▌─▌─▌─▌─▌─▌")
    print("█─▀█─▌█▌█▌█▌─▌─▌─▌")
    print("▀█▄█▀───────█▌█▌█▌")
    print("\n\n")
    input("Gracias por jugar!!!"+colores.WARNING)
