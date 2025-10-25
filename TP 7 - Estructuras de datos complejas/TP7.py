#1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#2

#Actualizar precios

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#3 - Obtener frutas

frutas = list(precios_frutas.keys())

#4 

contactos = {}

for i in range(3):
    nombre = input(f"Ingrese en nombre del primer contacto {i + 1}: ")
    telefono = input(f"Ingrese el telefono del primer contacto {i + 1}: ")
    contactos[nombre] = telefono

consula = input("Ingrese el nombre del contacto a buscar: ")

if consula in contactos:
    print(f"El telefono de {consula} es {contactos[consula]}")

#5

def palabras_unicas(frase):
    list = frase.split()
    list_unicas = set(list)
    return list_unicas

def conteo_palabras(frase):
    list = frase.split()
    conteo = {}
    for palabra in list:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

input_frase = input("Ingrese una frase: ")

conteo_palabras(input_frase)
palabras_unicas(input_frase)

print("Palabras únicas:", palabras_unicas(input_frase))
print("Conteo de palabras:", conteo_palabras(input_frase))

#6

alumnos = {}

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

for i in range(3):
    alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nota1 = float(input(f"Ingrese primer nota del alumno {i + 1}: "))
    nota2 = float(input(f"Ingrese segunda nota del alumno {i + 1}: "))
    nota3 = float(input(f"Ingrese tercera nota del alumno {i + 1}: "))
    if alumno not in alumnos:
        alumnos[alumno] = (nota1, nota2, nota3)

for alumno in alumnos:
    notas = alumnos[alumno]
    promedio = calcular_promedio(notas[0], notas[1], notas[2])
    print(f"El promedio de {alumno} es: {promedio}")


#7

parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {1, 4, 5, 7, 8}

ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
por_lo_menos_uno = parcial_1 | parcial_2

print("Alumnos que aprobaron ambos parciales:", ambos)
print("Alumnos que aprobaron solo uno de los parciales:", solo_uno)
print("Alumnos que aprobaron por lo menos uno de los parciales:", por_lo_menos_uno)

#8

prodcutos = {'tv': 10, 'celular': 20, 'tablet': 15, 'computadora': 5}

print("Menu:")
print("1. Consultar stock")
print("2. Actializar stock de producto")
print("3. Agregar nuevo producto")

opcion = int(input("Elegi una opcion: "))


match opcion:
    case 1:
        consultar_producto = input("Ingrese el nombre del producto a consultar: ")
        if consultar_producto in prodcutos:
            print(f"El stock de {consultar_producto} es: {prodcutos[consultar_producto]}")
        else:
            print("El producto no existe en el inventario.")

    case 2:
        actualizar_producto = input("Ingrese el nombre del producto a actualizar: ")
        if actualizar_producto in prodcutos:
            print("El stock actual es:", prodcutos[actualizar_producto])
            nuevo_stock = int(input("Ingrese cantidad actualizada en stock: "))
            prodcutos[actualizar_producto] = nuevo_stock
        else:
            print("El producto no existe en el inventario.")

    case 3:
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
        if nuevo_producto not in prodcutos:
            cantidad_stock = int(input("Ingrese la cantidad en stock del nuevo producto: "))
            prodcutos[nuevo_producto] = cantidad_stock
        else:
            print("El producto ya existe en el inventario.")


#9

agenda = {
    ('lunes', '09:00'): 'Reunión con el equipo',
    ('martes', '14:00'): 'Cita con el médico',
    ('miércoles', '11:00'): 'Reunion con el board',
    ('jueves', '20:00'): 'Partido de futbol',
    ('viernes', '10:00'): 'Llamada con el cliente' 
}

buscar_dia = input("Ingrese el día de la semana para buscar actividades: ").lower()
buscar_hora = input("Ingrese la hora (formato HH:MM) para buscar actividades: ")
clave_busqueda = (buscar_dia, buscar_hora)

if clave_busqueda in agenda:
    print(f"Actividad programada: {agenda[clave_busqueda]}")
else:
    print("No hay actividades programadas para ese día y hora.")

#10

pais_capital = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasília', 'Colombia': 'Bogotá', 
                'Chile': 'Santiago', 'Perú': 'Lima'}

capital_pais = {}

for pais in pais_capital:
    capital = pais_capital[pais]
    capital_pais[capital] = pais

print(f"Diccionario original (país: capital):{pais_capital}")
print(f"Diccionario invertido (capital: país): {capital_pais}")