import sys

sys.path.append("..")

from guerraterritorios.utils import constantes as colores
from guerraterritorios.utils.utils import clear, convertAInt

#Menus
from guerraterritorios.client.menuEstado import menuCambiarEstado
from guerraterritorios.client.menuComprar import menuComprarMisiles
from guerraterritorios.client.menuConsultas import menuConsultas
from guerraterritorios.client.menuPotencias import menuInsertarPotencias

# E: Un mapa
# S:
# D: Menu Inicial del juego!
def seleccionMenu(mapa):
    print(colores.WARNING, "Seleccione una opcion:", colores.NORMAL)
    print("___")
    print("|1| - Cambiar estado")
    print("|2| - Comprar misiles")
    print("|3| - Consultas")
    print("|4| - Disparar")
    print("|5| - Insertar potencia")
    print("|0| - Salir")
    print("---")

    opt = input(colores.WARNING+"Escriba su opcion:"+colores.NORMAL)
    opt = convertAInt(opt)
    
    clear()
    if opt == 1:
        menuCambiarEstado()
    elif opt == 2:
        menuComprarMisiles()
    elif opt == 3:
        menuConsultas(mapa)
    elif opt == 4:
        return
        #menuDispar()
    elif opt == 5:
        menuInsertarPotencias()
    elif opt == 0:
        exitLogo()
        return
    else:
        print(colores.FAIL,"Inserte una opcion valida...", colores.NORMAL)
        seleccionMenu(mapa)
    clear()
    seleccionMenu(mapa)

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
