import sys

sys.path.append("..")

from guerraterritorios.services.serv_potencias import *
from guerraterritorios.controller.registros import guardarRegistroCambio
from guerraterritorios.utils import constantes as colores
from guerraterritorios.utils.utils import convertAInt, clear

def menuCambiarEstado():
    potencias = buscarPotencias()
    print(colores.WARNING, "Cambiar estado de las potencias:", colores.NORMAL)

    opt = obtenerPotenciaACambiar(potencias)

    length = len(potencias) - 1

    if opt > length:
        clear()
        print(colores.FAIL, "Seleccione una opcion correcta", colores.NORMAL)
        menuCambiarEstado()
    elif opt == -1:
        return
    else:
        if cambiarEstado(potencias[opt][0]):
            clear()
            guardarRegistroCambio(potencias[opt])
            menuCambiarEstado()
        else:
            clear()
            print(colores.FAIL, "Ocurrio un error al cambiar el estado, intentelo de nuevo...", colores.NORMAL)
            menuCambiarEstado()

    return

# E: Una lista de potencias:
# S: Un numero
# D: Funcion de menu para seleccionar potencias
def obtenerPotenciaACambiar(potencias):
    print("___")
    print("|s|   Escriba s para salir")
    print("---")
    print("____")
    for i in range(0, len(potencias)):
        nombre = potencias[i][0]
        estado = ""

        if potencias[i][1]:
            estado = "Activo"
        else:
            estado = "Inactivo"

        print("|",i,"|", nombre," esta: ",colores.WARNING, estado, colores.NORMAL)
    print("----")

    print("Seleccione la potencia a la que quiere cambiarle el estado:")
    opt = input("")
    opt = convertAInt(opt)

    return opt