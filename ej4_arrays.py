vector = [int(input(f"Número {i}: ")) for i in range(10)]

sumaPares = 0
sumaImpares = 0
cuentaPares = 0
cuentaImpares = 0

for i in range(10):
    if i % 2 == 0:
        sumaPares += vector[i]
        cuentaPares += 1
    else:
        sumaImpares += vector[i]
        cuentaImpares += 1

mediaPares = sumaPares / cuentaPares
mediaImpares = sumaImpares / cuentaImpares

print(f"Media de posiciones pares: {mediaPares}")
print(f"Media de posiciones impares: {mediaImpares}")
