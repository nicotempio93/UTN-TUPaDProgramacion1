#1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2

#2
def saludar_usuario(nom):
    print(f"Hola, {nom}!")

nombre = input("Por favor, ingresa tu nombre: ")
saludar_usuario(nombre)

#3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"“Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}]")


input_nombre = input("Ingresa tu nombre: ")
input_apellido = input("Ingresa tu apellido: ")
input_edad = input("Ingresa tu edad: ")
input_residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(input_nombre, input_apellido, input_edad, input_residencia)

#4 

pi = 3.1416

def calcular_area_circulo(radio):
    area = pi * radio**2
    return area
    

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro
    

input_radio = float(input("Ingrese el radio del círculo: "))


print(f"El área del círculo es: {calcular_area_circulo(input_radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(input_radio)}")

#5

def segundos_a_horas(segundos):
    hora = segundos / 3600
    return hora

input_segundos = int(input("Ingrese la cantidad de segundos: "))

segundos_a_horas(input_segundos)
print(f"{input_segundos} segundos son {segundos_a_horas(input_segundos)} horas.")

#6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

input_numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(input_numero)

#7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    
    return (suma, resta, multiplicacion, division)

input_a = float(input("Ingrese el primer número: "))
input_b = float(input("Ingrese el segundo número: "))

print(f"Suma: {operaciones_basicas(input_a, input_b)[0]}, Resta: {operaciones_basicas(input_a, input_b)[1]}, Multiplicación: {operaciones_basicas(input_a, input_b)[2]}, División: {operaciones_basicas(input_a, input_b)[3]}")

#8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

input_peso = float(input("Ingrese su peso en kilogramos: "))
input_altura = float(input("Ingrese su altura en metros: "))

imc_resultado = calcular_imc(input_peso, input_altura)

print(f"Su Índice de Masa Corporal (IMC) es: {imc_resultado}")

#9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

input_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(input_celsius)

#10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

input_a = float(input("Ingrese el primer número: "))
input_b = float(input("Ingrese el segundo número: "))
input_c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(input_a, input_b, input_c)
print(f"El promedio de los tres números es: {promedio}")