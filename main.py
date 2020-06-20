from client.mainMenu import *
from client.menuMapa import menuCargarMapa
from utils.utils import clear

#D: Menu inicial
def menuInicial():
    logoJuego()
    print("Presione enter para ingresar!!!")
    input("")
    clear()
    menuCargarMapa()

menuInicial()