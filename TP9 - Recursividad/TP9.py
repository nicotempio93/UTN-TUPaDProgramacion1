#1

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Ingresá un número: "))

for i in range(1, n + 1):
    print(f"Factorial de {i} = {factorial(i)}")


#2

def fibonacci(pos: int) -> int:
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)


n = int(input("Mostar Fibonacci hasta la posición: "))

for i in range(0, n + 1):
    print(f"F({i}) = {fibonacci(i)}")

#3

def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

#4

def decimal_a_binario(n: int) -> str:
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)


num = int(input("Número decimal: "))
print(f"{num} en binario es {decimal_a_binario(num)}")

#5

def es_palindromo(palabra: str) -> bool:
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    # caso recursivo: comparar el “medio”
    return es_palindromo(palabra[1:-1])


texto = input("Palabra (sin espacios ni tildes): ")
print(es_palindromo(texto))

#6

def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


num = int(input("Número entero positivo: "))
print(f"La suma de los dígitos es {suma_digitos(num)}")

#7

def contar_bloques(n: int) -> int:
    if n <= 1:
        return n
    return n + contar_bloques(n - 1)


niveles = int(input("Bloques en el nivel más bajo: "))
print(f"Bloques totales: {contar_bloques(niveles)}")

#8

def contar_digito(numero: int, digito: int) -> int:
    if numero == 0:
        return 1 if digito == 0 else 0

    def helper(n: int, d: int) -> int:
        if n == 0:
            return 0
        ultimo = n % 10
        resto = n // 10
        cuenta_ultimo = 1 if ultimo == d else 0
        return cuenta_ultimo + helper(resto, d)

    return helper(numero, digito)



num = int(input("Número entero positivo: "))
d = int(input("Dígito a contar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces.")