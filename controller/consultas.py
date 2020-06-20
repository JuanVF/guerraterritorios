import sys

sys.path.append("..")

from guerraterritorios.utils.utils import eliminarPorPosicion, obtenerPaisPor
from guerraterritorios.services.serv_paises import buscarPais, imprimirPais

# E/S: Una lista de paises
# D: Ordena la lista de paises por su cantidad de vida
def obtenerPaisSegunVida(paises):
    paisesOrdenados = []
    vida = 1
    while paises != []:
        pos = obtenerPaisPor(paises, vida)
        paisesOrdenados += [paises[pos]]

        paises = eliminarPorPosicion(paises, pos)        

    return paisesOrdenados

# E/S: Una lista de paises
# D: Ordena la lista de paises por su extension activa de menor a mayor
def obtenerPaisSegunExtension(paises):
    paisesOrdenados = []
    extension = 2
    while paises != []:
        pos = obtenerPaisPor(paises, extension)
        paisesOrdenados += [paises[pos]]

        paises = eliminarPorPosicion(paises, pos)        

    return paisesOrdenados 

# E: Una lista de paises y un string
# S: 
# D: Imprime los datos de una pais en especifico
def imprimirStatusPais(paises, nombre):
    pais = buscarPais(paises, nombre)

    if pais == []:
        print("El pais que busca no existe...")
    else:
        imprimirPais(pais)
