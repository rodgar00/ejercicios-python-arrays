#Realizar programa que permita cargar un vector numérico de 10 elementos desde teclado y, posteriormente visualice el valor del elemento mayor y cuántas veces se repite en el vector este valor máximo.
vector = []

for i in range (10):
    numero = float(input(f"Dime un número: "))
    vector.append(numero)

valorMax = max(vector)

repeticion = vector.count(valorMax)

print(f"El número mayor es: {valorMax} y se repite {repeticion} veces")