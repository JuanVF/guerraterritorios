import sys

sys.path.append("..")

from guerraterritorios.services.serv_potencias import guardarPotencia, buscarPotencia, buscarPotencias
from guerraterritorios.utils.utils import clear
from guerraterritorios.utils import constantes as colores

def menuInsertarPotencias():
    print(colores.WARNING, "Menu para insertar potencias:", colores.NORMAL,"\n")

    nombre = input("Escriba el nombre de la nueva potencia:")

    potencia = buscarPotencia(nombre)

    if potencia == []:
        if guardarPotencia(nombre):
            print("La potencia se guardo con exito!")
            return
        else:
            print("Ocurrio un error al tratar de guardar la potencia...")
            print("Intentelo de nuevo")
    else:
        clear()
        print("La potencia que usted quiere agregar ya existe...")
        menuInsertarPotencias()
    return