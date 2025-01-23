import random
numAlu = int(input("Introduce el número de alumnos en la clase: "))

estaturas = []

for i in range(numAlu):
    estaturas.append(random.randint(150, 200) / 100)

sumaEstaturas = sum(estaturas)
mediaEstaturas = sumaEstaturas / numAlu

masAltos = 0
masBajos = 0

for estatura in estaturas:
    if estatura > mediaEstaturas:
        masAltos += 1
    elif estatura < mediaEstaturas:
        masBajos += 1

print((estaturas))
print(f"Media de estaturas: {mediaEstaturas}")
print(f"Alumnos más altos que la media: {masAltos}")
print(f"Alumnos más bajos que la media: {masBajos}")
