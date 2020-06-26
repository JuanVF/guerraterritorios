#Mapas
from client.mainMenu import *
from client.menuMapa import menuCargarMapa

from utils.utils import clear
from services.serv_potencias import calcularVidaPotencias, verificarListaDePotencias

#D: Menu inicial
def menuInicial():
    if verificarListaDePotencias():
        calcularVidaPotencias()
        logoJuego()
        print("Presione enter para ingresar!!!")
        input("")
        clear()
        menuCargarMapa()
    else:
        print("Hay un error en la lista de potencias del juego...")
        input("")

menuInicial()