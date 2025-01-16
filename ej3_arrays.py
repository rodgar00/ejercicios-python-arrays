numeros = [2, 14, 16, 28, 34, 42, 56, 68, 71, 82]

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(f"El número {numeros[i]} es par y está en {i+1}")