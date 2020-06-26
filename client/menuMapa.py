import sys

sys.path.append("..")

from guerraterritorios.controller.mapa import *
from guerraterritorios.utils.utils import *
from guerraterritorios.client.mainMenu import seleccionMenu
from guerraterritorios.utils import constantes as colores

def menuCargarMapa():
    print(colores.WARNING,"Hola! Bienvenido a guerra de territorios!", colores.NORMAL,end="\n\n")
    print("Por favor, coloque su mapa en la",colores.WARNING,"carpeta del juego", colores.NORMAL)
    path = input("Y escriba el nombre del mapa, con la extension del archivo:")
    
    mapa = obtenerMapa(path)
    
    if mapa == []:
        clear()
        print("El archivo no existe! intentelo de nuevo", end="\n\n")
        menuCargarMapa()
    else:
        datosMapa = verificarEstructuraMapa(mapa)
        if datosMapa[0] == 2:
            print(colores.FAIL, datosMapa[1], colores.NORMAL, datosMapa[2], end="\n\n")
        elif datosMapa[0] != 0:
            clear()
            print(colores.FAIL, datosMapa[1], colores.NORMAL, end="\n\n")
            menuCargarMapa()
        else:
            calcularExtensionesMapa(mapa)
            
            seleccionMenu(mapa, path)