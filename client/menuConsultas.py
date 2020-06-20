import sys

sys.path.append("..")

from guerraterritorios.controller.consultas import *
from guerraterritorios.services.serv_paises import imprimirPaises
from guerraterritorios.utils import constantes as colores
from guerraterritorios.utils.utils import convertAInt, clear

def menuConsultas(mapa):
    print(colores.WARNING, "Menu de consultas", colores.NORMAL)
    print("___")
    print("|1| Ver paises por vida...")
    print("|2| Ver paises por extension...")
    print("|3| Ver los datos de un pais...")
    print("|s| Salir...")
    print("---")

    opt = input("Elija una opcion:")
    opt = convertAInt(opt)

    clear()
    if opt == 1:
        imprimirPorVida(mapa)
    elif opt == 2:
        imprimirPorExtension(mapa)
    elif opt == 3:
        imprimirPaisStatus(mapa)
    elif opt > 3:
        clear()
        print("Elija una opcion valida")
    else:
        return
    input("Presione cualquier tecla para volver...")
    clear()
    return menuConsultas(mapa)

def imprimirPorVida(mapa):
    paises = obtenerPaisSegunVida(mapa)
    imprimirPaises(paises)

def imprimirPorExtension(mapa):
    paises = obtenerPaisSegunExtension(mapa)
    imprimirPaises(paises)

def imprimirPaisStatus(mapa):
    nombre = input("Escriba el nombre del pais que quiere buscar:  ")
    imprimirStatusPais(mapa, nombre)