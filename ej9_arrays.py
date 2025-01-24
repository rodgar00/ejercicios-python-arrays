numero = input("Introduce un número entero: ")
array = []
for digito in numero:
    array.append(int(digito))
print(*array)
#con el * se imprimen con un espacio