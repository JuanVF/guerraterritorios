import sys

sys.path.append("..")

from guerraterritorios.utils.utils import cumpleEstructura
from guerraterritorios.models.paises import esUnPais

potencias = [
    str,  # nombre
    bool,  # estado
    int,  # cantMisiles
    int,  # cantDisparos
    int,  # cantImpRec,
    float,  # vida
    bool,  # estadoVida
    list  # lista de paises o territorios
]

# E: Una lista
# S: Un booleano
# D: Dada una lista retorna True si cumple la estructura de potencias
def esUnaPotencia(lista):
    if not cumpleEstructura(lista, potencias):
        return False

    for pais in lista[7]:
        if not esUnPais(pais):
            return False
            
    return True

# E: Una lista del modelo potencia
# S: Un booleano
# D: Dada una potencia, la funcion evaluara si los datos son aptos para ser insertados
def cumpleRequisitosPotencia(potencia):
    nombre = potencia[0]
    cantMisiles = potencia[2]
    
    if nombre.strip() == "":
        return False

    if cantMisiles < 0:
        return False

    return True