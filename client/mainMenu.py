import sys

sys.path.append("..")

from guerraterritorios.utils import constantes as colores
from guerraterritorios.utils.utils import clear, convertAInt

#Menus
from guerraterritorios.client.menuEstado import menuCambiarEstado

#D: Menu inicial
def menuInicial():
    logoJuego()

    print("Presione enter para ingresar!!!")
    input("")
    clear()
    print(colores.WARNING, "Seleccione una opcion:", colores.NORMAL)
    print("___")
    print("|1| - Cambiar estado")
    print("|2| - Comprar misiles")
    print("|3| - Consultas")
    print("|4| - Disparar")
    print("|5| - Insertar potencia")
    print("|6| - Cargar mapa")
    print("|0| - Salir")
    print("---")

    opt = input(colores.WARNING+"Escriba su opcion:"+colores.NORMAL)
    opt = convertAInt(opt)

    if opt == 1:
        menuCambiarEstado()
    elif opt == 2:
        return
        #menuComprarMisiles()
    elif opt == 3:
        return
        #menuConsultas()
    elif opt == 4:
        return
        #menuDispar()
    elif opt == 5:
        return
        #menuInsertarPotencia()
    elif opt == 6:
        return
        #menuCargarMapa()
    elif opt == 0:
        exitLogo()
        return
    else:
        print(colores.FAIL,"Inserte una opcion valida...", colores.NORMAL)
        menuInicial()

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
