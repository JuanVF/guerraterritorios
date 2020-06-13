import sys

sys.path.append("..")

from guerraterritorios.models.potencias import esUnaPotencia, cumpleRequisitosPotencia
from guerraterritorios.models.paises import pagarMisiles

from guerraterritorios.controller.operaciones import *
from guerraterritorios.utils.constantes import POTENCIAS_PATH
from guerraterritorios.utils import constantes as colores
# E: 
# S: Una lista de potencias
# D: Retorna todas las potencias del juego
def buscarPotencias():
    potencias = eval(leer(POTENCIAS_PATH))

    return potencias


# E: Un string
# S: Una lista del modelo potencia
# D: Dado el nombre de una potencia, la buscara y la retornara
def buscarPotencia(nombre):
    potencias = buscarPotencias()
    
    for potencia in potencias:
        if potencia[0].strip().lower() == nombre.strip().lower():
            return potencia
    
    return []

# E: Una lista del modelo potencias
# S: Un booleano
# D: Dada una lista del modelo potencia, la busca y la actualiza, retorna False si hay error
def actualizarPotencia(potencia):
    potencias = buscarPotencias()
    posicion = buscarPosicionPotencia(potencia[0])

    if posicion == -1:
        return False

    potencias[posicion] = potencia
    potencias = str(potencias)
    
    return guardar(POTENCIAS_PATH, potencias)

# E: Un string
# S: Un int mayor o igual que -1
# D: Dado el nombre de una potencia, la busca y retorna su posicion en las potencias
def buscarPosicionPotencia(nombre):
    potencias = buscarPotencias()
    length = len(potencias)
    for index in range(0, length):
        if potencias[index][0].strip().lower() == nombre.strip().lower():
            return index
    
    return -1

# E: Dos strings, un flotante, un booleano, dos ints
# S: Un booleano
# D: Guarda una lista si cumple el modelo de potencias, retorna False si no lo cumple
def guardarPotencia(nombre):
    potencia = [nombre, True, 1000, 0, 0, 100.0, True, []]

    if not esUnaPotencia(potencia) or not cumpleRequisitosPotencia(potencia):
        return False

    if buscarPotencia(nombre) != []:
        return False

    potencias = buscarPotencias()
    potencias += [potencia]
    potencias = str(potencias)

    return guardar(POTENCIAS_PATH, potencias)

# E: Dos strings
# S: Un booleano
# D: Busca una potencia por su nombre y cambia su estado, retorna False si la potencia no existe
def cambiarEstado(nombre):
    potencia = buscarPotencia(nombre)

    if potencia == []:
        return False

    potencia[1] = not potencia[1]

    return actualizarPotencia(potencia)

# E: Un string y un int mayor o igual que 100
# S: Un booleano
# D: Se encarga de comprar misiles a la potencia, sino le alcanza retorna False
def comprarMisiles(nombre, cant):
    if cant < 100 or cant > 1000:
        return False

    if cant % 100 != 0:
        return False

    potencia = buscarPotencia(nombre)

    if potencia == []:
        return False

    vidaInicial = potencia[5]
    porcentaje = (cant / 1000) 
    
    pagarMisiles(potencia[7], porcentaje)


    vida = calcularVidaPotencia(potencia)
    potencia[5] = vida

    if vidaInicial != potencia[5]:
        potencia[2] += cant

    return actualizarPotencia(potencia)

# E: Una lista del modelo potencia
# S: Un float
# D: Retorna la nueva vida de la potencia
def calcularVidaPotencia(potencia):
    paises = potencia[7]
    sumVida = 0.0

    for pais in paises:
        sumVida += pais[1]
    
    promVida = sumVida / len(paises)

    return promVida

# E/S:
# D: Devuelve una lista con informacion general de todas las potencias
def consultarPotencias():
    potencias = buscarPotencias()

    for potencia in potencias:
        porcentajeVida = str(potencia[5]) + "%"
        print(colores.WARNING, potencia[0], potencia[2], "misiles", porcentajeVida, potencia[3], "disparos", potencia[4], "impactos", colores.NORMAL, end="\n\n")
        print(colores.WARNING, "Territorios:", colores.NORMAL)

        for pais in potencia[7]:
            paisVida = str(pais[1]) + "%"

            print("\t",pais[0], paisVida, "de vida", "  Extension:", pais[2],"km2", end="\n\n")
            
            print("\t Mapa:")
            for provincia in pais[3]:
                for canton in provincia[1]:
                    print("\t",canton[1])