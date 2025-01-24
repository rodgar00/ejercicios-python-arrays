numero = []
for i in range(1, 101):
    numero.append(i)

print(f"Vector original: {numero}")


posicionEliminar = int(input("Introduce la posición del elemento que deseas eliminar (1 a 100): "))

if 1 <= posicionEliminar <= len(numero):
    nuevoVector = []
    for i in range(len(numero)):
        if i != posicionEliminar - 1:
            nuevoVector.append(numero[i])

    numero = []
    for elemento in nuevoVector:
        numero.append(elemento)

    print(f"Vector después de eliminar el elemento: {numero}")
else:
    print("Posición no válida. Debe estar entre 1 y 100.")
