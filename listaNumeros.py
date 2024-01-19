
def ingresarCantidadNumeros():
    cant = int(input("Ingrese la cantidad de numeros que desea guardar: "))
    numeros = []

    for x in range(cant):
        numero = int(input("Ingrese el numero {}: ".format(x + 1)))
        numeros.append(numero)

    return numeros

def contarParesYImpares(numeros):
    numPares = 0
    numImpares = 0

    for num in numeros:
        if num % 2 == 0:
            numPares += 1
        else:
            numImpares += 1

    return numPares, numImpares

def contarNumRepetidos (numeros):
    numRepetidos = {}

    for num in numeros:
        if num in numRepetidos:
            numRepetidos[num] += 1
        else:
            numRepetidos[num] = 1

    return numRepetidos

def main():
    numerosRaw = ingresarCantidadNumeros()
    numerosOrdenados = sorted(numerosRaw)

    print("\nNumeros Ingresados: {}".format(numerosRaw))
    print("\nNumeros Ordenados: {}".format(numerosOrdenados))

    pares, impares = contarParesYImpares(numerosOrdenados)
    print("Hay {} numeros pares". format(pares))
    print("Hay {} numeros impares". format(impares))

    repeticiones = contarNumRepetidos(numerosOrdenados)
    print("\nEstos numeros se repiten")

    for num, cantidad in repeticiones.items():
        if cantidad > 1:
            print("{}: {} veces".format(num, cantidad))

if __name__ == "__main__":
    main()