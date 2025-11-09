

# Segundo Parcial - Programación 1

# ---------------- Funciones ----------------
# --------------- Validaciones  ----------------

def normalizar_titulo(t):
    t = t.strip()
    limpio = ""
    i = 0
    anterior_espacio = False
    while i < len(t):
        c = t[i]
        if c == " ":
            if not anterior_espacio:
                limpio = limpio + " "
            anterior_espacio = True
        else:
            limpio = limpio + c
            anterior_espacio = False
        i = i + 1
    return limpio

def es_entero_no_negativo(s):
    s = s.strip()
    return s.isdigit()

# ---------------- Persistencia  ----------------

def asegurar_archivo(ruta):
    # a+) crea si no existe, luego coloca encabezado si está vacío
    f = open(ruta, "a+")
    f.seek(0)
    primera = f.readline()
    if primera == "":
        f.write("TITULO,CANTIDAD\n")
    f.close()

def cargar_catalogo(ruta):
    asegurar_archivo(ruta)
    catalogo = []
    f = open(ruta, "r")
    _ = f.readline()  # saltar encabezado
    linea = f.readline()
    while linea != "":
        linea = linea.strip()
        if linea != "":
            partes = linea.split(",")
            if len(partes) == 2:
                titulo_raw = normalizar_titulo(partes[0])
                cant_raw = partes[1].strip()
                if titulo_raw != "" and es_entero_no_negativo(cant_raw):
                    idx = buscar_indice_por_titulo(catalogo, titulo_raw)
                    if idx == -1:
                        catalogo.append({"TITULO": titulo_raw, "CANTIDAD": int(cant_raw)})
        linea = f.readline()
    f.close()
    return catalogo

def guardar_catalogo(ruta, catalogo):
    f = open(ruta, "w")
    f.write("TITULO,CANTIDAD\n")
    i = 0
    while i < len(catalogo):
        fila = catalogo[i]
        f.write(f"{fila['TITULO']},{fila['CANTIDAD']}\n")
        i = i + 1
    f.close()

# ---------------- Operaciones ----------------

def buscar_indice_por_titulo(catalogo, titulo_busqueda):
    buscado = normalizar_titulo(titulo_busqueda).lower()
    i = 0
    while i < len(catalogo):
        if normalizar_titulo(catalogo[i]["TITULO"]).lower() == buscado:
            return i
        i = i + 1
    return -1

def ingresar_titulos(ruta, catalogo):
    cant = input("¿Cuántos títulos desea cargar? ").strip()
    if not es_entero_no_negativo(cant):
        print("Cantidad inválida.")
        return
    cant = int(cant)
    cargados = 0
    while cargados < cant:
        t = input("TÍTULO: ")
        t = normalizar_titulo(t)
        if t == "":
            print("Título inválido.")
            continue
        if buscar_indice_por_titulo(catalogo, t) != -1:
            print("Título duplicado.")
            continue
        c = input("CANTIDAD (>=0): ").strip()
        if not es_entero_no_negativo(c):
            print("Cantidad inválida.")
            continue
        catalogo.append({"TITULO": t, "CANTIDAD": int(c)})
        cargados = cargados + 1
    guardar_catalogo(ruta, catalogo)
    print("✓ Títulos cargados y guardados.")

def ingresar_ejemplares(ruta, catalogo):
    t = input("Título a incrementar ejemplares: ")
    idx = buscar_indice_por_titulo(catalogo, t)
    if idx == -1:
        print("Título no encontrado.")
        return
    inc = input("Cantidad a sumar (>=0): ").strip()
    if not es_entero_no_negativo(inc):
        print("Cantidad inválida.")
        return
    catalogo[idx]["CANTIDAD"] = catalogo[idx]["CANTIDAD"] + int(inc)
    guardar_catalogo(ruta, catalogo)
    print("✓ Stock actualizado y guardado.")

def mostrar_catalogo(catalogo):
    if len(catalogo) == 0:
        print("Catálogo vacío.")
        return
    print("Catálogo:")
    i = 0
    while i < len(catalogo):
        print(f"- {catalogo[i]['TITULO']} | {catalogo[i]['CANTIDAD']} ejemplares")
        i = i + 1

def consultar_disponibilidad(catalogo):
    t = input("Título a consultar: ")
    idx = buscar_indice_por_titulo(catalogo, t)
    if idx == -1:
        print("Título no encontrado.")
    else:
        print(f"'{catalogo[idx]['TITULO']}' → {catalogo[idx]['CANTIDAD']} ejemplares.")

def listar_agotados(catalogo):
    hay = False
    i = 0
    mientras = True
    while i < len(catalogo):
        if catalogo[i]["CANTIDAD"] == 0:
            if not hay:
                print("Agotados:")
                hay = True
            print(f"- {catalogo[i]['TITULO']}")
        i = i + 1
    if not hay:
        print("No hay títulos agotados.")

def agregar_titulo(ruta, catalogo):
    t = input("Nuevo TÍTULO: ")
    t = normalizar_titulo(t)
    if t == "":
        print("Título inválido.")
        return
    if buscar_indice_por_titulo(catalogo, t) != -1:
        print("Título duplicado.")
        return
    c = input("Cantidad inicial (>=0): ").strip()
    if not es_entero_no_negativo(c):
        print("Cantidad inválida.")
        return
    catalogo.append({"TITULO": t, "CANTIDAD": int(c)})
    guardar_catalogo(ruta, catalogo)
    print("✓ Título agregado y guardado.")

def actualizar_ejemplares(ruta, catalogo):
    t = input("Título (préstamo/devolución): ")
    idx = buscar_indice_por_titulo(catalogo, t)
    if idx == -1:
        print("Título no encontrado.")
        return
    op = input("Ingrese 'P' para préstamo o 'D' para devolución: ").strip().upper()
    if op == "P":
        if catalogo[idx]["CANTIDAD"] > 0:
            catalogo[idx]["CANTIDAD"] = catalogo[idx]["CANTIDAD"] - 1
            guardar_catalogo(ruta, catalogo)
            print("✓ Préstamo registrado y guardado.")
        else:
            print("No hay ejemplares disponibles para prestar.")
    elif op == "D":
        catalogo[idx]["CANTIDAD"] = catalogo[idx]["CANTIDAD"] + 1
        guardar_catalogo(ruta, catalogo)
        print("✓ Devolución registrada y guardada.")
    else:
        print("Opción inválida.")

# ---------------- Programa principal ----------------

def main():
    ruta = "catalogo.txt"
    catalogo = cargar_catalogo(ruta)
    opcion = 0
    while opcion != 8:
        print("-----------------------")
        print("Gestión de libros - Segundo Parcial")
        print("1. Ingresar títulos")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catálogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar título")
        print("7. Actualizar ejemplares (préstamo/devolución)")
        print("8. Salir")
        print("-----------------------")
        op_str = input("Seleccione una opción (1-8): ").strip()
        if not op_str.isdigit():
            print("Opción inválida.")
            continue
        opcion = int(op_str)
        if opcion < 1 or opcion > 8:
            print("Opción inválida.")
            continue
        match opcion:
            case 1:
                ingresar_titulos(ruta, catalogo)
            case 2:
                ingresar_ejemplares(ruta, catalogo)
            case 3:
                mostrar_catalogo(catalogo)
            case 4:
                consultar_disponibilidad(catalogo)
            case 5:
                listar_agotados(catalogo)
            case 6:
                agregar_titulo(ruta, catalogo)
            case 7:
                actualizar_ejemplares(ruta, catalogo)
            case 8:
                print("Programa finalizado correctamente.")


main()