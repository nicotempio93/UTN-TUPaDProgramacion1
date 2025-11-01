
def crear_archivo_productos(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Producto,Precio,Cantidad\n")
        archivo.write("Heladera,120000,10\n")
        archivo.write("Lavarropas,80000,15\n")
        archivo.write("Televisor,60000,20\n")


crear_archivo_productos('productos.txt')

opcion = 0
prodcutos_en_memoria = None

print("Menú de opciones:")
while True:
    print("1. Mostrar prodcutos")
    print("2. Agregar producto")
    print("3. Carcar productos en una lista de diccionarios")
    print("4. Buscar producto por nombre")
    print("5. Guardar cambios / Sobre escribir archivo")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            with open('productos.txt', 'r') as archivo:
                archivo.readline()  # Saltar primera linea
                for linea in archivo:
                    linea = linea.strip().split(',')
                    print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Cantidad: {linea[2]}")
        case 2:
            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")
            with open('productos.txt', 'a') as archivo:
                archivo.write(f"{nombre},{precio},{cantidad}\n")
        case 3:
            productos = []
            with open('productos.txt', 'r') as archivo:
                archivo.readline()  # Saltar primera linea
                for linea in archivo:
                    nombre, precio, cantidad = linea.strip().split(',')
                    producto = {
                        'nombre': nombre,
                        'precio': float(precio),
                        'cantidad': int(cantidad)
                    }
                    productos.append(producto)
            print(productos)
            #Mantenemos en memoria para guardar despues
            prodcutos_en_memoria = productos
        case 4:
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            encontrado = False
            with open('productos.txt', 'r') as archivo:
                archivo.readline()  # Saltar primera linea
                for linea in archivo:
                    nombre, precio, cantidad = linea.strip().split(',')
                    if nombre.lower() == nombre_buscar.lower():
                        print(f"Producto encontrado: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                        encontrado = True
                        break
            if not encontrado:
                print("Producto no encontrado.")
        case 5:
            if prodcutos_en_memoria is None:
              print("No hay cambios para guardar. Por favor, cargue los productos primero (opción 3).")
            else:
                with open('productos.txt', 'w') as archivo:
                    archivo.write("Producto,Precio,Cantidad\n")
                    for producto in prodcutos_en_memoria:
                        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
                print("Cambios guardados exitosamente.")