# 1)
print("Hola mundo!")

# 2)
nombre = input("Ingrese su nombre:")
print(f"Hola " + nombre + "!")

#3)
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = int(input("Ingrese su edad:"))
residencia = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4)

radio = float(input("Enter radio: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es {area} y el perímetro es {perimetro}.")

# 5)

segundos = int(input("Ingrese la cantidad de segundos: "))
hora = segundos // 3600
print(f"{segundos} son {hora} horas")

# 6)

num = int(input("Ingrese un número: "))
print(f"{num}*1 = {num*1}\n{num}*2 = {num*2}\n{num}*3 = {num*3}\n{num}*4 = {num*4}\n{num}*5 = {num*5}\n{num}*6 = {num*6}\n{num}*7 = {num*7}\n{num}*8 = {num*8}\n{num}*9 = {num*9}\n{num}*10 = {num*10}")

# 7)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}") 

# 8)

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc}")

# 9)

celsius = float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

# 10)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print(f"El promedio de los tres numeros es {(num1 + num2 + num3) / 3}")