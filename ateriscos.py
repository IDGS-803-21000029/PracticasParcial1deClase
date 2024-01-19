
cantAsteriscos = int(input("Ingresa la cantidad de asteriscos \n5"))

res = ""
for canty in range(cantAsteriscos):
    if canty == 0:
        res += "*\n"
    else:
        for cantx in range(canty + 1):
            res += "*"
        res += "\n"
    
print(res)