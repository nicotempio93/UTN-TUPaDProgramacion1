#1

promedio = 0
notaMayor = 0
notaMenor = 10
notas = [8, 2, 4, 6, 10, 3, 7, 9, 5, 1]
print(notas)

for i in range(len(notas)):
    promedio += notas[i]
    if notas[i] >= notaMayor:
        notaMayor = notas[i]
    elif notas[i] <= notaMenor:
        notaMenor = notas[i]

promedio = promedio / len(notas)

print("El promedio es: ", promedio)

print("La nota mayor es: ", notaMayor)
print("La nota menor es: ", notaMenor)




#2
productos = []

for i in range(6):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

productos.sort()

print(productos)

eliminar = input("Ingrese un producto a eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado.")
else:
    print("El producto no se encuentra en la lista.")    
print(productos)




#3

numerosRamdom = []
numerosPares = []
numerosImpares = []

for i in range(15):
    import random
    numerosRamdom.append(random.randint(1, 100))

print(numerosRamdom)

for i in range(len(numerosRamdom)):
    if numerosRamdom[i] % 2 == 0:
        numerosPares.append(numerosRamdom[i])
    else:
        numerosImpares.append(numerosRamdom[i])

print("Números pares: ", numerosPares)
print("Números impares: ", numerosImpares)


#4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datosFiltrados = []

datos.sort()

for i in datos: #Aqui podria usar not in o set()
    if i in datosFiltrados:
        continue
    else:   
        datosFiltrados.append(i)

print(datos)
print(datosFiltrados)


#5

alumnos = ["Nicolas", "Facundo", "Pedro", "Gabriela", "Olivia", "Valentino", "Hernan", "Eli"]
comando = input("Igrese 1 para agregar un nuevo alumno o 2 para eliminar un alumno de la lista: ")

if comando == "1":
    nuevoAlumno = input("Ingrese el nombre del nuevo alumno: ")
    alumnos.append(nuevoAlumno)
    print("Alumno agregado.")
elif comando == "2":
    alumnosEliminar = input("Ingrese el nombre del alumno a eliminar: ")
    if alumnosEliminar in alumnos:
        alumnos.remove(alumnosEliminar)
        print("Alumno eliminado.")
    else:
        print("El alumno no se encuentra en la lista.")

print(alumnos)

#6

numeros =[1,2,3,4,5,6,7]

numerosRotados = []
numerosRotados.append(numeros[len(numeros)-1])

for i in range(0 ,len(numeros) - 1):
    numerosRotados.append(numeros[i])

numeros = numerosRotados
print(numeros) 
# Estos seguro que hay una forma mejor de hacerlo sin gastar memoria 
# creando un nuevo array, pero no se me ocurrio la manera. 
# Asique lo resolvi de esta forma, sabiendo que en un escenario real con 
# grandes volumenes de datos, esto no seria eficiente u optimo!



#7

temperaturasSemana = [[18, 29], [12, 22], [14, 22], [16, 23], [18, 38], [20, 21], [22, 27]]
promedioMinima = 0
promedioMaxima = 0
amplitudTerminca = 0
indiceMayorAmplitud = 0

for i in range (len(temperaturasSemana)):
    promedioMinima += temperaturasSemana[i][0]
    promedioMaxima += temperaturasSemana[i][1]
    if (temperaturasSemana[i][1] - temperaturasSemana[i][0]) > amplitudTerminca:
        indiceMayorAmplitud = i
        amplitudTerminca = temperaturasSemana[i][1] - temperaturasSemana[i][0]

print("El promedio de las temperaturas minimas es: ", promedioMinima/len(temperaturasSemana))
print("El promedio de las temperaturas maximas es: ", promedioMaxima/len(temperaturasSemana))

print("El dia con mayor amplitud termica es el dia ", indiceMayorAmplitud + 1, "con una amplitud de ", amplitudTerminca)

#8
notasCursada = [[6, 9, 7], [8, 5, 10], [9, 6, 8], [7, 8, 9], [10, 9, 8]]

promediosAlumnos = []
promedioMaterias = [0, 0, 0]

for i in range(len(notasCursada)):
    promedioAl = sum(notasCursada[i]) / len(notasCursada[i])
    promediosAlumnos.append(promedioAl)

    for j in range(len(notasCursada[i])):
        promedioMaterias[j] += notasCursada[i][j]

promedioMaterias[0] = promedioMaterias[0] / len(notasCursada)
promedioMaterias[1] = promedioMaterias[1] / len(notasCursada)
promedioMaterias[2] = promedioMaterias[2] / len(notasCursada)

print("Promedios de los alumnos:", promediosAlumnos)
print("Promedios de las materias:", promedioMaterias)



#9

tateti = [["", "", ""], ["", "", ""], ["", "", ""]]
movimiento = [0, 0]

print(tateti[0])
print(tateti[1])
print(tateti[2])


for i in range(9):
    if i % 2 == 0:
        print("Turno del jugador X")
        
        movimiento[0] = int(input("Ingrese Fila (1 - 2 - 3): ")) - 1
        movimiento[1] = int(input("Ingrese Columna (1 - 2 - 3): ")) - 1

        tateti[movimiento[0]][movimiento[1]] = "X"
        print(tateti[0])
        print(tateti[1])
        print(tateti[2])
    else:
        print("Turno del jugador O")

        movimiento[0] = int(input("Ingrese Fila (1 - 2 - 3): ")) - 1
        movimiento[1] = int(input("Ingrese Columna (1 - 2 - 3): ")) - 1

        tateti[movimiento[0]][movimiento[1]] = "O"
        print(tateti[0])
        print(tateti[1])
        print(tateti[2])




#10

ventasSemanales = [[100, 950, 1500, 600], 
                   [200, 880, 1200, 500], 
                   [50, 590, 600, 700], 
                   [300, 260, 1100, 400],
                   [400, 270, 300, 800], 
                   [250, 740, 400, 900], 
                   [150, 430, 1700, 1000]]

totalVentasProductos = [0, 0, 0, 0]
diaMayorVentas = [ 0, 0]
productoMasVendido = [0, 0]

for i in range (len(ventasSemanales)):
    if sum(ventasSemanales[i]) > sum(ventasSemanales[diaMayorVentas[1]]):
        diaMayorVentas[0] = i
        diaMayorVentas[1] = sum(ventasSemanales[i])

    for j in range (len(ventasSemanales[i])):
        totalVentasProductos[j] += ventasSemanales[i][j]


for i in range(len(totalVentasProductos)):
    if totalVentasProductos[i] > productoMasVendido[0]:
        productoMasVendido[0] = i
        productoMasVendido[1] = totalVentasProductos[i]
    else:
        continue


print("Total ventas por producto1: ", totalVentasProductos[0])
print("Total ventas por producto2: ", totalVentasProductos[1])
print("Total ventas por producto3: ", totalVentasProductos[2])
print("Total ventas por producto4: ", totalVentasProductos[3])

print("------------------------------")

print ("El dia con mayor ventas fue el dia ", diaMayorVentas[0]+1, "con un total de ", diaMayorVentas[1], " en ventas")


print("------------------------------")

print("El producto mas vendido fue el producto ", productoMasVendido[0]+1, "con un total de ", productoMasVendido[1], " en ventas")