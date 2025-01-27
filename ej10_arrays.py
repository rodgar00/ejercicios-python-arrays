def es_capicua():
    numero_valido = False

    while not numero_valido:
        numero = input("Introduce un número entero positivo de 10 cifras: ")

        if len(numero) == 10 and numero.isdigit():
            numero_valido = True
        else:
            print("El número debe ser un entero positivo de exactamente 10 cifras. Inténtalo de nuevo.")

    lista = list(numero)

    if lista == lista[::-1]:
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} no es capicúa.")

es_capicua()
