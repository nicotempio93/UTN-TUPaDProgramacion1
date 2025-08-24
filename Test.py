dia = int(input("Ingrese el día (1-31): "))
mes = int(input("Ingrese el mes (1-12): "))
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()

mesInvierno = [ 1, 2]
mesPrimavera = [ 4, 5]
mesVerano = [7, 8]
mesOtono = [10, 11]
estacion = ""

if (mes == 1 or mes == 2) or (mes == 12 and dia >= 21 or mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 4 or mes == 5) or (mes == 3 and dia >= 21 or mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 7 or mes == 7) or (mes == 6 and dia >= 21 or mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 10 or mes == 11) or (mes == 9 and dia >= 21 or mes == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
print("La estacion es: ", estacion)