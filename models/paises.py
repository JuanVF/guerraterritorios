import sys

sys.path.append("..")

from guerraterritorios.models.provincias import esUnaProvincia
from guerraterritorios.utils.utils import cumpleEstructura

paises = [
    str,  # nombre
    float,  # vida
    float,  # extensionTotal
    list  # provincias : Lista de provincias
]

# E: Una lista
# S: Un booleano
# D: Retorna True si la lista cumple el modelo de paises
def esUnPais(lista):
    if not cumpleEstructura(lista, paises):
        return False
    
    for provincia in lista[3]:
        if not esUnaProvincia(provincia):
            return False

    return True

# E: Una lista de paises y un int
# S: Una lista de paises
# D: Busca un territorio cuya vida sea apta para pagar los misiles y retorna la lista de paises
#    la retorna igual si no puede pagar
def pagarMisiles(paises, porcentaje):

    for pais in paises:
        precio = pais[2] * porcentaje
        
        disponible = (pais[1]/100) * pais[2]

        if disponible >= precio:

            pais[1] = ((disponible - precio) / pais[2])*100
            break
    
    return paises