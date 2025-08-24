#1 
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Eres mayor de edad")

# 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3
num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4
#En este al final podria haber puesto else: print("Adulto/a") sin condicional, verdad? Esta bien? Cual es una buena practica?
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# 5
contraseña = str(input("Introduce la contraseña: "))

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6
from statistics import mode, median, mean

import random

numerosAleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numerosAleatorios)

mediana = median(numerosAleatorios)

media = mean(numerosAleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

# 7
frase = str(input("Ingrese una frase: "))

vola = ["a", "e", "i", "o", "u"]

if frase[len(frase) - 1] in vola:
    frase = frase + "!"
    print(frase)
else:
    print(frase)

# 8
nombre = str(input("Ingrese su nombre: "))

opcion = int(input("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. \n Ingrese numero de la opción: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# 9
magnitudTerremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitudTerremoto < 3:
    print("Muy leve")
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:
    print("Leve")
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:
    print("Moderado")
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
    print("Fuerte")
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
    print("Muy fuerte")
elif magnitudTerremoto >= 7:
    print("Extremo")

# 10
dia = int(input("Ingrese el día (1-31): "))
mes = int(input("Ingrese el mes (1-12): "))
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()

mesInvierno = [ 1, 2]
mesPrimavera = [ 4, 5]
mesVerano = [7, 8]
mesOtono = [10, 11]
estacion = ""

if (mes == 1 or mes == 2) or (mes == 12 and dia >= 21 or mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 4 or mes == 5) or (mes == 3 and dia >= 21 or mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 7 or mes == 7) or (mes == 6 and dia >= 21 or mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 10 or mes == 11) or (mes == 9 and dia >= 21 or mes == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
print("La estacion es: ", estacion)

#Este me costo muchisimo jaja. 
# Cuando crei que tenia la solucion me pasaba que en las fechas limite nada se guardaba en la variable estacion. 
# Despues de mucho le pregunte a chat gpt y me dijo que podia ser porque estaba mesclando tipos de datos al usar los operadores relacionales, me sugirio que lo pase a numero y funciono.  