from datetime import datetime
import os
from guerraterritorios.utils import constantes as colores

# E:
# S: Un string
# D: Retorna la fecha en formato: yyyy-mm-dd hh:mm:ss
def obtenerFecha():
    fecha = datetime.now()

    formato = str(fecha.year) + "-" + str(fecha.month) + "-" + str(fecha.day) + " " + str(fecha.hour) + ":" + str(fecha.minute) + ":" + str(fecha.second)
 
    return formato 
# E: Un string, un booleano
# S: Un int mayor o igual que 0 o Un string si neg=True
# D: Convierte un string a un entero positivo o 0, retorna -1 si hay error
#    Acepta negativos si se envia neg=True
def convertAInt(string, neg=False):
    num = -1

    try:
        num = eval(string)

        if num < 0 and not neg:
            return -1
    except:
        if neg:
            return "Error"
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

# E: Un string
# S: Un booleano
# D: Retorna true si el string no es vacio
def validacionString(string):
    return string.lower().strip() == ""

#D: Limpia la consola
def clear():
    if os.name == 'nt':
        os.system("cls")
    else: 
        os.system("clear")

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

# E: Una lista de paises y un numero natural
# S: La posicion del pais
# D: Busca al pais por elemento, devuelve el mayor
def obtenerPaisPor(paises, elem):
    mayor = paises[0][1]
    pos = 0

    for i in range(1, len(paises)):
        if paises[i][elem] > mayor:
            mayor = paises[i][1]
            pos = i
    
    return pos

# E/S: Una lista
# D: Elimina un elemento de la lista por su posicion
def eliminarPorPosicion(lista, pos):
    nuevaLista = []

    for i in range(0, len(lista)):
        if i != pos:
            nuevaLista += [lista[i]]

    return nuevaLista