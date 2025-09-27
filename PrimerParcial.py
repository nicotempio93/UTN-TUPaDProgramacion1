#Parcual Programacion 1

#Defino algunas variables
opcion = 0
titulos = []
ejemplares = []

#Menu de opciones, pongo como condicion que la opcion sea distinta de 8 para que el menu se repita hasta que el usuario quiera salir
while opcion != 8:
    print("-----------------------")
    print("Gestion de libros")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    print("-----------------------")
    #Pido la opcion al usuario
    opcion = input("Seleccione una opción (1-8): ")

    #Confirmno que la opcion sea un digito y la convierto a entero para evitar errores
    if opcion.isdigit():
        opcion = int(opcion)
        #Compruebo que la opcion este dentro del rango y uso match case para ejecutar la opcion seleccionada
        if opcion >= 1 and opcion <= 8:
            match opcion:

                #Ingresar titulos
                case 1:
                    #Verifico si ya hay titulos cargados para no permitir ingresar mas de una vez
                    if titulos != []:
                        print("Ya hay títulos en el catálogo. Para agregar un nuevo titulo utilice la opción 6.")
                    else:
                        #Pido la cantidad de titulos a cargar
                        cantidadLibros = int(input("Ingrese cantidad de títulos a cargar: "))
                        #inicializo el contador
                        i = 0
                        #Bucle para ingresar titulos, verificando que no se repitan y que no sean cadenas vacias
                        while i < cantidadLibros:
                        #Pido el titulo y lo convierto a mayusculas para evitar errores
                            titulo = input("Ingrese título: ").upper()
                            #Verifico que el titulo no este repetido y que no sea una cadena vacia
                            if titulo not in titulos and titulo != "": 
                                    #Si el titulo es valido lo agrego a la lista y agrego 0 ejemplares asegurandome que sean listas paralelas
                                    titulos.append(titulo)
                                    ejemplares.append(0)
                                    #Actaulizo el contador
                                    i += 1
                            else:
                                    print("Título inválido o repetido. Intente nuevamente.")
                        #Mensaje de confirmacion        
                        print(f"Se ingresaron {cantidadLibros} títulos correctamente.")

                #Ingresar ejemplares a un titulo ya existente
                case 2:
                    print("Ingresar cantidad de ejemplares: ")
                    #Verifico que haya titulos cargados
                    if titulos == []:
                        print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
                        continue
                    else:
                        #Muestro los titulos disponibles
                        for i in titulos:
                            print(f"Para modificar '{i}'  - presione {titulos.index(i)+1}")
                        #Pido la opcion y la cantidad de ejemplares a agregar
                        opcion2 = int(input("Seleccione una titulo: "))
                        unidadesDeLibro = int(input(f"Ingrese cantidad de ejemplares de  '{titulos[opcion2 - 1]}' a agregar: "))
                        ejemplares[opcion2 - 1] += unidadesDeLibro

                #Mostrar catalogo  
                case 3:
                    #Verifico si hay titulos y ejemplares cargados
                    if titulos == [] or ejemplares == []:
                        print("No hay títulos en el catálogo.")
                    else:
                        #Itero el array mostrando los titulos y sus ejemplares
                        print("Catálogo de libros:")
                        for i in titulos:
                            print(f"Titulo: {i} - Ejemplares: {ejemplares[titulos.index(i)]}")

                #Consultar disponibilidad
                case 4:
                    #Pido el titulo a buscar
                    buscar = input("Buscar disponibilidad de un título: ").upper()
                    #Verifico que el titulo esta o no en la lista
                    if buscar not in titulos:
                        print("Título no encontrado.")
                    else:
                        #Busco el indice del titulo y muestro la cantidad de ejemplares disponibles
                        index = titulos.index(buscar)
                        print(f"El título '{buscar}' tiene {ejemplares[index]} ejemplares disponibles.")

                #Listar agotados
                case 5:
                    #Inicializo una variable bandera
                    print("Libros agotados:")
                    hayAgotados = False
                    
                    #Itero el array buscando los titulos con 0 ejemplares
                    for i in titulos:
                        if ejemplares[titulos.index(i)] > 0:
                            continue
                        elif ejemplares[titulos.index(i)] == 0:
                            print(f"Titulo: {i} - Ejemplares: {ejemplares[titulos.index(i)]}")
                            #Si encuentro alguno cambio la variable bandera
                            hayAgotados = True
                        
                    #Si la variable bandera sigue siendo falsa es porque no hay titulos agotados, muestro un mensaje por pantalla
                    if not hayAgotados:
                        print("No hay libros agotados.")

                #Agregar 1 titulo
                case 6:
                    #Pido el titulo
                    print("Agregar título")
                    titulo = input("Ingrese título: ").upper()
                    #Verifico si esta repetido o que sea una cadena vacia
                    if titulo in titulos or titulo == "":
                        print("Título ya existe o es inválido.")
                    else:
                        #Si es valido lo agrego a la lista y pido la cantidad de ejemplares asegurandome que sean listas paralelas
                        titulos.append(titulo)
                        cantidadEjemplares = int(input(f"Ingrese cantidad de ejemplares de  '{titulo}': "))
                        ejemplares.append(cantidadEjemplares)
                        print(f"El titulo '{titulo}' se agrego correctamente. Hay {cantidadEjemplares} ejemplares.")

                #Actualizar ejemplares (prestamo/devolucion)
                case 7:
                    #Pido el titulo y la operacion a realizar
                    print("Actualizar ejemplares (prestamos/devoluciones)")
                    titulo = input("Ingrese título: ").upper()
                    #Verifico que el titulo este en la lista
                    if titulo not in titulos:
                        print("Título no encontrado.")
                    else:
                        #Busco el indice del titulo y pido la operacion a realizar
                        index = titulos.index(titulo)
                        modificar = input("Presiones 'P' para préstamo o 'D' para devolución: ").upper()
                        #Verifico que la operacion sea valida
                        if modificar != 'P' and modificar != 'D':
                            print("Opción inválida.")
                        #Si es valida realizo la operacion correspondiente
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
                #Salir
                case 8:
                    #Mensaje de despedida aqui el programa termina porque la condicion del while deja de cumplirse ya que Opcion != 8 es False
                    print("Programa finalizado correctamente.")
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")