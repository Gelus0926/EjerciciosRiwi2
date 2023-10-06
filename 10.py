def calcular_nota_final():
    # Pedir al usuario las notas del parcial y los trabajos
    parcial = float(input("Ingrese la nota del parcial: "))
    trabajos = float(input("Ingrese la nota de los trabajos: "))

    # Calcular la nota final
    nota_final = (parcial * 0.8) + (trabajos * 0.2)

    # Verificar si el estudiante pasa el semestre
    if nota_final >= 3.0:
        print("El estudiante ha pasado el semestre con una nota final de", nota_final)
    else:
        print("El estudiante no ha pasado el semestre con una nota final de", nota_final)

calcular_nota_final()