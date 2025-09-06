num = int(input("Ingrese un nuemero: "))

largo = len(str(num))
invertido = ""

for i in range(largo):
    invertido += str(num)[largo -1 - i]
print(invertido)