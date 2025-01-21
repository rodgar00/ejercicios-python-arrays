import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1, 20))
print(numeros)
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(f"El número {numeros[i]} es par y está en la posición {i+1}")
