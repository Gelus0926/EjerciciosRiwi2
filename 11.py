""" #1. Imprimir números del 1 al n.
numero = int(input("Digite un numero: "))

for i in range(numero):
    print(f'{i + 1} ') """

""" #2.Sumar números del 1 al n
numero = int(input("Ingrese un número: "))

suma = 0
for i in range(1, numero + 1):
    suma += i

print("La suma de los números hasta", numero, "es:", suma) """

""" #3.Imprimir la tabla de multiplicar del 53.
numero = 53

for j in range(10,11):
    print(f'La tabla de: {numero}')
    for i in range(1, j + 1):
        print(int(numero), "*", i, "=", numero*i) """

""" #4. Contar cuantas veces aparece una letra en una cadena.
letra = "Reconocer"
cont= 0

for i in letra:
    if (i == "a"):
        cont = cont + 1

print(cont) """

""" #5. Imprimir números pares del 1 al 20.
for num in range(1, 21):
    # Comprobamos si el número es par utilizando el operador % (módulo)
    if num % 2 == 0:
        print(num) """

""" #6.Escribir un programa que muestre cuente las vocales de una palabra
vocales = "Reconocer"
cont= 0

for i in vocales:
    if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
        cont = cont + 1
print(cont)
 """

""" #7.Escribe un programa que muestre cuantos números pares hay de 4 al 200
for num in range(4, 201):
    # Comprobamos si el número es par utilizando el operador % (módulo)
    if num % 2 == 0:
        print(num) """

""" #8. Escribe un programa que muestre cuantas letras tiene una palabra ingresada por el usuario
letra = input("Ingrese una palabra: ")
cont= 0

for i in letra:
    if (i == "r"):
        cont = cont + 1

print(cont) """

""" #9.Escribe un programa donde el usuario pueda ver un menú, seleccionar una opción,
#si la opción es 1 el usuario podra sumar dos numeros que el desee,
#si es dos multiplicar, si es 3 dividir, si es 4 restar.
def s(n1, n2):
    suma = n1 + n2
    print(f'La suma de los dos numeros es: {suma}')
def m(n1,n2):
    multi = n1 * n2
    print(multi)
def d(n1,n2):
    divi = n1 / n2
    print(divi)
def r(n1,n2):
    resta = n1 - n2
    print(resta)

n1=int(input("ingresar primer numero: "))
n2=int(input("ingresar segundo numero: "))


while True:
    print("*** Menu Principal ***")
    print("0 salida")
    print("1.La suma de dos numeros")
    print("2.multiplicación de dos numeros")
    print("3.división de dos numeros")
    print("4.RResta de dos numeros")
    opc = input("Ingrese una opcion: ")
    if opc=="0":
        break
    elif opc=="1":
        print(s(n1,n2))
    elif opc=="2":
        print(m(n1,n2))
    elif opc=="3":
        print(d(n1,n2))
    elif opc=="4":
        print(r(n1,n2))
    else:
        print("Opción invalida") """

""" #10. Escribe un programa que muestre las tablas de multiplicar del 0 al 10, hasta el rango de 10
tabla_desde = 0
tabla_hasta = 10

for i in range(tabla_desde,tabla_hasta + 1):
    print(f'La tabla de: {i}: ')
    for j in range(tabla_desde,11):
        print(int(i), "*", j, "=", j*i)
    print("\n") """