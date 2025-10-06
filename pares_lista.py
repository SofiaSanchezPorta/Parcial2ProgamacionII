def cantPares(lista: list):
    cont = 0
    for e in lista:
        if e % 2 == 0:
            cont +=1
    return cont

print(cantPares([0, 1, 2, 3, 4, 5, 6, 7]))
print(cantPares([0, 2, 4, 6]))
print(cantPares([1, 3, 5, 7]))


