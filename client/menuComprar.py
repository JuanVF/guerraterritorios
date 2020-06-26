import sys

sys.path.append("..")

from guerraterritorios.services.serv_potencias import comprarMisiles, buscarPotencias
from guerraterritorios.controller.registros import guardarRegistroCompra

from guerraterritorios.utils import constantes as colores
from guerraterritorios.utils.utils import convertAInt, clear

def menuComprarMisiles(PATH):
    print(colores.WARNING, "Comprar misiles:", colores.NORMAL)
    potencias = buscarPotencias()
    length = len(potencias) - 1

    opt = seleccionarPotencia(potencias)

    if opt == -1:
        clear()
        return
    elif opt > length:
        print(colores.FAIL, "La opcion es incorrecta, elija otra opcion:", colores.NORMAL)
        menuComprarMisiles(PATH)
    else:
        clear()
        menuDeCompra(potencias[opt], PATH)
    return

# E: Una potencia y un string
def menuDeCompra(potencia, PATH):
    print(colores.WARNING, "Cuantos misiles desea comprar para: ", colores.NORMAL, potencia[0])
    print("El numero debe estar entre 100 y 1000 (solo multiplos de 100)")
    cantMisiles = input("")
    cantMisiles = convertAInt(cantMisiles)

    if 100 <= cantMisiles and cantMisiles <= 1000 and cantMisiles % 100 == 0:
        if comprarMisiles(potencia[0], cantMisiles, PATH):
            guardarRegistroCompra(potencia[0], cantMisiles)
            print("Se pudieron comprar", cantMisiles, "misiles!")
            input("")
            return
        else:
            print("La potencia no puede pagar esa cantidad de misiles!")
            print("Desea seleccionar otra cantidad?","1-si","n-no", sep="\n")
            opt = input("")
            opt = convertAInt(opt)

            if opt == 1:
                clear()
                menuDeCompra(potencia, PATH)
            else:
                return
    else:
        clear()
        print(colores.WARNING, "Ingrese una cantidad correcta!", colores.NORMAL)
        menuDeCompra(potencia, PATH)
    return

# E: Una lista de potencias:
# S: Un numero
# D: Funcion de menu para seleccionar potencias
def seleccionarPotencia(potencias):
    print("___")
    print("|s|   Escriba s para salir")
    print("---")
    print("____")
    for i in range(0, len(potencias)):
        nombre = potencias[i][0]

        print("|",i,"|", nombre)
    print("----")

    print("Seleccione la potencia que quiere comprar misiles:")
    opt = input("")
    opt = convertAInt(opt)

    return opt