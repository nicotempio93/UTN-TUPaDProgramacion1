def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

input_a = float(input("Ingrese el primer número: "))
input_b = float(input("Ingrese el segundo número: "))
input_c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(input_a, input_b, input_c)
print(f"El promedio de los tres números es: {promedio}")