notas = []

for i in range(40):
    notas.append(float(input(f"Introduce la nota del alumno {i + 1}: ")))

sumaNotas = sum(notas)
mediaNotas = sumaNotas / len(notas)

aprobados = []
suspensos = []
superioresAMedia = 0

for nota in notas:
    if nota >= 5:
        aprobados.append(nota)
    else:
        suspensos.append(nota)

    if nota > mediaNotas:
        superioresAMedia += 1

print(f"Número de aprobados: {len(aprobados)}")
print(f"Número de suspensos: {len(suspensos)}")
print(f"Nota media de la clase: {mediaNotas}")
print(f"Número de calificaciones superiores a la media: {superioresAMedia}")
