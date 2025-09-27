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