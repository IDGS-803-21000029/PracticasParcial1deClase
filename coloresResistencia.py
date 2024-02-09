
def calcularResistencia(banda1, banda2, banda3, tolerancia):
    cad = str(localizarBanda(banda1)) + str(localizarBanda(banda2))
    valor = float(cad) * float(localizarMultiplicador(banda3))
    valorMaximo = valor + calcularTolerancia(valor, str(tolerancia))
    valorMinimo = valor - calcularTolerancia(valor, str(tolerancia))

    return [valor, valorMaximo, valorMinimo]
    

def localizarBanda(banda):
    if banda == "Negro":
        return 0
    elif banda == "Cafe":
        return 1
    elif banda == "Rojo":
        return 2
    elif banda == "Naranja":
        return 3
    elif banda == "Amarillo":
        return 4
    elif banda == "Verde":
        return 5
    elif banda == "Azul":
        return 6
    elif banda == "Violeta":
        return 7
    elif banda == "Gris":
        return 8
    elif banda == "Blanco":
        return 9
    else:
        return "X"
    
def localizarMultiplicador(banda3):
    if banda3 == "Negro":
        return 1
    elif banda3 == "Cafe":
        return 10
    elif banda3 == "Rojo":
        return 100
    elif banda3 == "Naranja":
        return 1000
    elif banda3 == "Amarillo":
        return 10000
    elif banda3 == "Verde":
        return 100000
    elif banda3 == "Azul":
        return 1000000
    elif banda3 == "Violeta":
        return 10000000
    elif banda3 == "Gris":
        return 100000000
    elif banda3 == "Blanco":
        return 1000000000
    else:
        return "X"
    
def calcularTolerancia(valor, tolerancia):
    if tolerancia == "Dorado":
        return valor * 0.05
    elif tolerancia == "Plata":
        return valor * 0.10
    elif tolerancia == "Rojo":
        return valor * 0.02
    
def obtenerColores(banda):
    if banda == "Negro":
        return "#000000"
    elif banda == "Cafe":
        return "#4E342E"
    elif banda == "Rojo":
        return "#F44336"
    elif banda == "Naranja":
        return "#FFB300"
    elif banda == "Amarillo":
        return "#FFB300"
    elif banda == "Verde":
        return "#4CAF50"
    elif banda == "Azul":
        return "#4CAF50"
    elif banda == "Violeta":
        return "#AB47BC"
    elif banda == "Gris":
        return "#AB47BC"
    elif banda == "Blanco":
        return "#FFFFFF"
    elif banda == "Dorado":
        return "#B7950B"
    elif banda == "Plata":
        return "#BDBDBD"
    else:
        return "X"