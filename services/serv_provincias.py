# E: Una lista de paises
# S: Una lista de provincias
# D: Dada una lista de paises, retorna sus provincias sin importar de su pais
def obtenerProvincias(paises):
    provincias = []

    for pais in paises:
        provincias += pais[3]
    
    return provincias
    