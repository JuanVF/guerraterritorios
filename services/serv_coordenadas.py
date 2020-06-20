# E: Dos posiciones
# S: Una posicion
# D: Retorna la posicion que es mayor
def compararPosicion(posicion1, posicion2):
    grados1 = posicion1[0]
    grados2 = posicion2[0]

    minutos1 = posicion1[1]
    minutos2 = posicion2[1]

    segundos1 = posicion1[2]
    segundos2 = posicion2[2]

    if grados1 > grados2:
        return posicion1
    elif grados1 == grados2:
        if minutos1 > minutos2:
            return posicion1
        elif minutos1 == minutos2:
            if segundos1 >= segundos2:
                return posicion1
            return posicion2
    return posicion2 

# E/S: Una lista de dos posiciones
# D: Ordena la lista de menor a mayor
def obtenerListaOrdenada(posiciones):
    posicionMayor = compararPosicion(posiciones[0], posiciones[1])

    if posicionMayor == posiciones[0]:
        return [posiciones[1], posiciones[0]]
    
    return [posiciones[0], posiciones[1]]

# E: Una posicion
# S: Un int
# D: Convierte la posicion en un solo numero
def crearUnidad(posicion):
    grados = posicion[0]
    minutos = posicion[1]
    segundos = posicion[2]
    SF = 1

    if grados < 0:
        SF = -1

    unidad = SF*(abs(grados)*10000 + minutos*100 + segundos)

    return unidad
    
# E: Una lista del modelo coordenada
# S: Una lista del modelo posicion
# D: Retorna la latitud de la coordenada
def obtenerLatitud(coordenada):
    return coordenada[0]

# E: Una lista del modelo coordenada
# S: Una lista del modelo posicion
# D: Retorna la longitud de la coordenada
def obtenerLongitud(coordenada):
    return coordenada[1]
