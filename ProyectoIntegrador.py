#Proyecto integrados Programacion 1 - Matematicas
#Aqui haremos una herramientas capaz de convertir de Hexadecimal a Decimal o binario
#Lo que pense fue usar 3 listas paralelas, una para los numeros y otra para los caracteres

#Comienzo definiendo las listas paraleras con sus respectivas equivalencias

hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
binarios = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

#Defino una variable para el menu
menu = 0

#Usare match/case para el menu



while menu != 5:
        print("\nMenu de opciones:")
        print("1. Convertir de Hexadecimal a Decimal")
        print("2. Convertir de Hexadecimal a Binario")
        print("3. Convertir de Binario a Decimal")
        print("4. Convertir de Binario a Hexadecimal")
        print("5. Salir")
        menu = input("Seleccione una opción (1-5): ")
        #validamos la opcion
        if menu.isdigit():
            menu = int(menu)

            if menu >= 1 and menu <= 5:
                 match menu:
                      case 1:
                            #Pido el numero al usuario
                            numero = input("Ingrese un número hexadecimal: ").upper()
                            #Verifico que el numero sea valido
                            correcto = True
                            resultado = 0
                            for n in numero:
                                    if n not in hexadecimal:
                                        correcto = False
                                        break

                            if not correcto or numero == "":
                                print("Número inválido")
                            else:
                                print("Número válido")
                                  #Recorro el numero de derecha a izquierda
                                resultado = 0
                                for i in range(len(numero), 0, -1):   # ahora llega hasta 1 -> i-1 puede ser 0
                                    # Obtengo el valor decimal del caracter
                                    valor = hexadecimal.index(numero[i-1])
                                    # Calculo el valor ponderado por posición
                                    resultado += valor * (16 ** (len(numero) - i))
                                    print(f"Valor decimal de {numero[i-1]}: {valor * (16 ** (len(numero) - i))}")

                                print(f"El número hexadecimal {numero} en decimal es: {resultado}")
                      case 2:
                            #Pido el numero al usuario
                            numero = input("Ingrese un número hexadecimal: ").upper()
                            #Verifico que el numero sea valido
                            correcto = True
                            resultado = ""
                            for n in numero:
                                    if n not in hexadecimal:
                                        correcto = False
                                        break

                            if not correcto or numero == "":
                                print("Número inválido")
                            else:
                                print("Número válido")
                                  #Recorro el numero de derecha a izquierda
                                resultado = ""
                                for i in range(len(numero)):   
                                    # Obtengo el valor binario del caracter
                                    valor = binarios[hexadecimal.index(numero[i])]
                                    resultado += valor 
                                    print(f"Valor binario de {numero[i]}: {valor}")

                                print(f"El número hexadecimal {numero} en binario es: {resultado}")
                      case 3:
                               #Pido el numero al usuario
                                numero = input("Ingrese un número binario: ")
                                #Verifico que el numero sea valido
                                correcto = True
                                resultado = 0
                                #Verifico que el numero solo contenga 0 y 1
                                for i in numero:
                                    if i not in ['0', '1']:
                                        correcto = False

                                #Verifico que la longitud del numero sea multiplo de 4, si no lo es le agrego 0 al principio hasta que lo sea.
                                if len(numero) % 4 != 0:
                                    numero = list(numero)
                                    while len(numero) % 4 != 0:
                                        numero.insert(0, '0')
                                    numero = ''.join(numero)
                                    print(f"El número binario ajustado es: {numero}")

                                #Ahora que se que tengo el numero binario completo y valido busco la equivalencia
                                if correcto:
                                    resultado = ""
                                    #Recorro el numero de 4 en 4
                                    for i in range(0, len(numero), 4):
                                        #Tomo un segmento de 4 digitos, que busco en la lista de binarios y obtengo su valor decimal
                                        segmento = numero[i:i+4]
                                        valor = binarios.index(segmento)
                                        resultado += decimal[valor]
                                        print(f"Valor decimal de {segmento}: {decimal[valor]}")
                                    print(f"El número binario {numero} en decimal es: {resultado}")
                                
                                     
                                if not correcto or numero == "":
                                    print("Número inválido")
                      case 4:
                           #Pido el numero al usuario
                                numero = input("Ingrese un número binario: ")
                                #Verifico que el numero sea valido
                                correcto = True
                                resultado = 0
                                #Verifico que el numero solo contenga 0 y 1
                                for i in numero:
                                    if i not in ['0', '1']:
                                        correcto = False

                                #Verifico que la longitud del numero sea multiplo de 4, si no lo es le agrego 0 al principio hasta que lo sea.
                                if len(numero) % 4 != 0:
                                    numero = list(numero)
                                    while len(numero) % 4 != 0:
                                        numero.insert(0, '0')
                                    numero = ''.join(numero)
                                    print(f"El número binario ajustado es: {numero}")

                                #Ahora que se que tengo el numero binario completo y valido busco la equivalencia
                                if correcto:
                                    resultado = ""
                                    #Recorro el numero de 4 en 4
                                    for i in range(0, len(numero), 4):
                                        #Tomo un segmento de 4 digitos, que busco en la lista de binarios y obtengo su valor decimal
                                        segmento = numero[i:i+4]
                                        valor = binarios.index(segmento)
                                        resultado += hexadecimal[valor]
                                        print(f"Valor hexadecimal de {segmento}: {hexadecimal[valor]}")
                                    print(f"El número binario {numero} en hexadecimal es: {resultado}")
                           
                      case 5:
                               print("Saliendo del programa.")   
        else:
            print("Opción inválida. Intente nuevamente.")
            continue
        