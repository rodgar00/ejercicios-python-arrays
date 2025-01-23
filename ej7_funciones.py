numeros = []
for i in range(1, 101):
    numeros.append(i)
print("Lista original:")
print(numeros)

nuevoValor = int(input("Introduce el valor a insertar en el vector: "))

posicionInsercion = len(numeros) - 1
while posicionInsercion >= 0 and numeros[posicionInsercion] > nuevoValor:
    posicionInsercion -= 1

numeros[posicionInsercion + 1] = nuevoValor

print("El vector resultante con el valor intercalado es:")
print(numeros)
