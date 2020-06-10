from datetime import datetime

# E:
# S: Un string
# D: Retorna la fecha en formato: yyyy-mm-dd hh:mm:ss
def obtenerFecha():
    fecha = datetime.now()

    formato = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day) + " " + str(fecha.hour) + ":" + str(fecha.minute) + ":" + str(fecha.second)
 
    return formato 
# E: Un string
# S: Un int mayor o igual que 0
# D: Convierte un string a un entero positivo o 0, retorna -1 si hay error
def convertAInt(string):
    num = -1

    try:
        num = eval(string)

        if num < 0:
            return -1
    except:
        return num

    return num

# E: Una lista, Una lista cuyos elementos son el tipo de dato
# S: Un booleano
# D: Retorna True si ambas listas poseen la misma estructura
def cumpleEstructura(lista, estructura):
    length = len(lista)

    if length != len(estructura):
        return False

    for index in range(0, length):
        if type(lista[index]) != estructura[index]:
            return False

    return True

# E/S: Una lista que cumple el modelo de Potencias
# D: Ordena un modelo de paises, segun la extension de terreno que tengan
#   de mayor a menor
def ordenarPaisSegunTerreno(lista):
    listaOrdenada = []

    return listaOrdenada

# E/S: Una lista que cumple el modelo de Potencias
# D: Ordena un modelo de paises, segun la cantidad de vida que tengan
#   de mayor a menor
def ordenarPaisSegunVida(lista):
    listaOrdenada = []

    return listaOrdenada
# E: Un string
# S: Un booleano
# D: Retorna true si el string no es vacio
def validacionString(string):
    return string.lower().strip() == ""