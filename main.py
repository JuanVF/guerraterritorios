#Mapas
from client.mainMenu import *
from client.menuMapa import menuCargarMapa

from utils.utils import clear
from services.serv_potencias import calcularVidaPotencias

#D: Menu inicial
def menuInicial():
    calcularVidaPotencias()
    logoJuego()
    print("Presione enter para ingresar!!!")
    input("")
    clear()
    menuCargarMapa()

menuInicial()