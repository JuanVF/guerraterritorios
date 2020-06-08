from os import path

# E: Dos strings
# S: Booleano
# D: Guarda los datos de un string sobre un archivo
def guardar(path, string):
    try:
        file = open(path, 'w')
        file.write(string)
        file.close()
    except:
        return False
    return True

# E/S: Un string
# D: Dada la ubicacion de un archivo, lo lee y retorna sus datos
def leer(path):
    datos = ""
    try:
        file = open(path, 'r')

        datos = file.read()

        file.close()
        return datos
    except:
        return datos