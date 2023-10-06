edad_perro = int(input("Ingrese la edad de su perro en años humanos: "))

if edad_perro < 0:
    print("La edad no puede ser negativa.")
elif edad_perro <= 2:
    edad_perro_calculada = edad_perro * 10.5
else:
    edad_perro_calculada = 21 + (edad_perro - 2) * 4

print(f"La edad de su perro en años de perro es: {edad_perro_calculada}")