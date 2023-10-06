def es_primo(numero):
    # Un número menor o igual a 1 no es primo
    if numero <= 1:
        return False
    
    # Verificar si el número es divisible por algún número menor que él
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    # Si no fue divisible por ningún número menor que él, es primo
    return True

# Pedir al usuario un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es primo o no
if es_primo(numero):
    print(numero, "es un número primo")
else:
    print(numero, "no es un número primo")