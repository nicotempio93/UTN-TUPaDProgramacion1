#Menu interactivo

opcion = 0
titulos = ["RAMBO", "TERMINATOR", "ROCKY"]
ejemplares = [3, 2, 0]

while opcion != 8:
    print("-----------------------")
    print("Gestion de libros")
    print("1. Ingresar título")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    print("-----------------------")
    opcion = input("Seleccione una opción (1-8): ")
    
    if opcion.isdigit():
        opcion = int(opcion)
        
        if opcion >= 1 and opcion <= 8:
            match opcion:

                case 1:

                    titulo = input("Ingrese título: ").upper()

                    while titulo in titulos or titulo == "":
                        print("Título ya existe o es inválido.")
                        titulo = input("Ingrese título: ").upper()

                    print(f"Título '{titulo}' ingresado correctamente.")
                    titulos.append(titulo)
                    posicion = titulos.index(titulo)
                    ejemplares.insert(posicion, 0)

                case 2:

                    print("Ingresar cantidad de ejemplares")

                    for i in titulos:
                        print(f"Para modificar '{i}'  - presione {titulos.index(i)+1}")

                    opcion2 = int(input("Seleccione una titulo: "))
                    unidadesDeLibro = int(input(f"Ingrese cantidad de ejemplares de  '{titulos[opcion2 - 1]}' a agregar: "))
                    ejemplares[opcion2 - 1] += unidadesDeLibro
                        
                case 3:

                    if titulos == []:
                        print("No hay títulos en el catálogo.")
                    else:
                        print("Catálogo de libros:")
                        for i in titulos:
                            print(f"Titulo: {i} - Ejemplares: {ejemplares[titulos.index(i)]}")

                case 4:

                    buscar = input("Buscar disponibilidad de un título: ").upper()
                    if buscar not in titulos:
                        print("Título no encontrado.")
                    else:
                        index = titulos.index(buscar)
                        print(f"El título '{buscar}' tiene {ejemplares[index]} ejemplares disponibles.")

                case 5:

                    print("Libros agotados:")
                    hayAgotados = False

                    for i in titulos:
                        if ejemplares[titulos.index(i)] > 0:
                            continue
                        elif ejemplares[titulos.index(i)] == 0:
                            print(f"Titulo: {i} - Ejemplares: {ejemplares[titulos.index(i)]}")
                            hayAgotados = True
                        
                    if not hayAgotados:
                        print("No hay libros agotados.")

                case 6:

                    print("Agregar título")
                    titulo = input("Ingrese título: ").upper()
                    if titulo in titulos or titulo == "":
                        print("Título ya existe o es inválido.")
                    else:
                        titulos.append(titulo)
                        cantidadEjemplares = int(input(f"Ingrese cantidad de ejemplares de  '{titulo}': "))
                        ejemplares.append(cantidadEjemplares)
                        print(f"El titulo '{titulo}' se agrego correctamente. Hay {cantidadEjemplares} ejemplares.")

                case 7:

                    print("Actualizar ejemplares (prestamos/devoluciones)")
                    titulo = input("Ingrese título: ").upper()

                    if titulo not in titulos:
                        print("Título no encontrado.")
                    else:
                        index = titulos.index(titulo)
                        modificar = input("Presiones 'P' para préstamo o 'D' para devolución: ").upper()

                        if modificar != 'P' and modificar != 'D':
                            print("Opción inválida.")

                        elif modificar == 'P':
                            if ejemplares[index] > 0:
                                ejemplares[index] -= 1
                                print(f"Préstamo cargado. Quedan {ejemplares[index]} ejemplares de '{titulo}'.")
                            else:
                                print(f"No hay ejemplares para prestar '{titulo}'.")
                        elif modificar == 'D':
                            if ejemplares[index] >= 0:
                                ejemplares[index] += 1
                                print(f"Devolución cargada. Hay {ejemplares[index]} ejemplares de '{titulo}'.")

                case 8:

                    print("Programa finalizado correctamente.")
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")