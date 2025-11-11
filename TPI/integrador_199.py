# Resolucion del Trabajo Práctico Integrador Grupo 199.

# --------------------------------------------------------------------
# Validación
# --------------------------------------------------------------------

from pathlib import Path
import os

def pedir_int(mensaje: str, permitir_vacio: bool = False):
  while True:
    valor = input(mensaje).strip()
    if permitir_vacio and valor == "":
      return None
    if valor.isdigit():
      return int(valor)
    print("Valor inválido. Ingrese un número entero." + (" (o Enter)" if permitir_vacio else ""))

def mostrar_paises(paises: list[dict]):
  if not paises:
    print("No hay datos para mostrar...")
    return
  print("\nItem. País — Continente — Pob: Población — Sup: Superficie")
  for i, pais in enumerate(paises, start=1):
    # separadores de miles “.” para que se entienda mejor si el numero es muy grande.
    poblacion = f"{pais['poblacion']:,}".replace(",", ".")
    superficie = f"{pais['superficie']:,}".replace(",", ".")
    print(f"{i}. {pais['nombre']} — {pais['continente']} — pob: {poblacion} — sup: {superficie}")
  print("\n -- Volviendo al menu --")

def print_error(mensaje="Opción inválida. Vuelva a intentarlo..."): # Mensaje de error genérico pero reutilizable.
  return print(mensaje)

def pais_existe(paises: list[dict], nombre: str):
  nombre = nombre.strip().lower()
  for pais in paises:
    if pais["nombre"].lower() == nombre:
      return True
  return False

def primer_mayuscula(texto: str):
 return texto.strip().lower().title()

arr_conttinentes =["America", "Europa", "Asia", "Africa", "Oceania", "Antartida"] #Defino los continentes aca porque no van a cambiar
# ---------------------------------------------------------------------
# Carga de CSV
# ---------------------------------------------------------------------
def cargar_csv(rutaArchivo: str):
  paises = []
  try:
    with open(rutaArchivo, "r", encoding="utf-8", newline="") as archivo:
      header = archivo.readline().strip().split(",")
      esperado = ["nombre", "poblacion", "superficie", "continente"]
      if [palabra.lower() for palabra in header] != esperado:
        print("ERROR: Encabezado CSV inválido. Se esperaba:", ", ".join(esperado))
        return []
      linea_n = 1
      for linea in archivo:
        linea_n += 1
        linea = linea.strip()
        if not linea:
          continue
        cols = linea.split(",")
        if len(cols) != 4:
          print_error(f"Advertencia: columnas inválidas en línea {linea_n}.")
          # print(f"Advertencia: columnas inválidas en línea {linea_n}.") # Otra forma de mostrar el error.
          continue
        nombre, poblacion, superficie, continente = (c.strip() for c in cols)
        if not (poblacion.isdigit() and superficie.isdigit()):
          print_error(f"Advertencia: tipos inválidos en línea {linea_n}.")
          # print(f"Advertencia: tipos inválidos en línea {linea_n}.") # Otra forma de mostrar el error.
          continue
        paises.append({
          "nombre": nombre,
          "poblacion": int(poblacion),
          "superficie": int(superficie),
          "continente": continente
        })
  except FileNotFoundError:
    print_error(f"ERROR: No se encontró el archivo: {rutaArchivo}")
    # print(f"ERROR: No se encontró el archivo: {rutaArchivo}") # Otra forma de mostrar el error.
  return paises

# ---------------------------------------------------------------------
# Búsquedas, Filtros, Ordenamiento
# ---------------------------------------------------------------------
def buscar_por_nombre(paises: list[dict], termino: str):
  t = termino.strip().lower()
  return [pais for pais in paises if t in pais["nombre"].lower()]

def filtrar_por_continente(paises: list[dict], continente: str):
  c = continente.strip().lower()
  return [pais for pais in paises if pais["continente"].lower() == c]

def filtrar_por_poblacion(paises: list[dict], minimo: int | None, maximo: int | None):
  res = []
  for pais in paises:
    ok_min = (minimo is None) or (pais["poblacion"] >= minimo)
    ok_max = (maximo is None) or (pais["poblacion"] <= maximo)
    if ok_min and ok_max:
      res.append(pais)
  return res

def filtrar_por_superficie(paises: list[dict], minimo: int | None, maximo: int | None):
  res = []
  for pais in paises:
    ok_min = (minimo is None) or (pais["superficie"] >= minimo)
    ok_max = (maximo is None) or (pais["superficie"] <= maximo)
    if ok_min and ok_max:
      res.append(pais)
  return res

def ordenar_por_nombre(paises: list[dict], sentidoOrden: bool = True):
  return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=not sentidoOrden)

def ordenar_por_poblacion(paises: list[dict], sentidoOrden: bool = True):
  return sorted(paises, key=lambda p: p["poblacion"], reverse=not sentidoOrden)

def ordenar_por_superficie(paises: list[dict], sentidoOrden: bool = True):
  return sorted(paises, key=lambda p: p["superficie"], reverse=not sentidoOrden)

# ---------------------------------------------------------------------
# Estadísticas
# ---------------------------------------------------------------------
def max_min_poblacion(paises: list[dict]):
    if not paises:
      return None, None
    mx = paises[0] # Utilizo el nombre mx para el país con la población máxima.
    mn = paises[0] # Utilizo el nombre mn para el país con la población mínima.
    for pais in paises[1:]: # Recorro la lista desde el segundo elemento en adelante porque el primero se utiliza como base.
      if pais["poblacion"] > mx["poblacion"]:
        mx = pais
      if pais["poblacion"] < mn["poblacion"]:
        mn = pais
    return mx, mn

def promedio_poblacion(paises: list[dict]):
  if not paises:
    return None
  return sum(pais["poblacion"] for pais in paises) / len(paises)

def promedio_superficie(paises: list[dict]):
  if not paises:
    return None
  return sum(pais["superficie"] for pais in paises) / len(paises)

def cantidad_por_continente(paises: list[dict]):
  cuenta = {}
  for pais in paises:
    continente = pais["continente"]
    cuenta[continente] = cuenta.get(continente, 0) + 1
  return cuenta

# ---------------------------------------------------------------------
# Menú UI
# ---------------------------------------------------------------------
def menu_principal():
  print("\n----- Gestión de Países -----")
  print("1) Buscar país por nombre")
  print("2) Filtrar países")
  print("3) Ordenar países")
  print("4) Estadísticas")
  print("5) Agregar Pais")
  print("6) Actualizar Pais")
  print("7) Salir")
  return input("Opción: ").strip()

def menu_filtros():
  print("\n----- Filtros -----")
  print("1) Por continente")
  print("2) Por rango de población")
  print("3) Por rango de superficie")
  return input("Opción: ").strip()

def menu_orden():
  print("\n----- Ordenar -----")
  print("1) Por nombre")
  print("2) Por población")
  print("3) Por superficie")
  opcionInput = input("Opción: ").strip()
  while opcionInput not in ("1", "2", "3"):
    print_error("Opción inválida. Vuelva a intentarlo...")
    opcionInput = input("Opción: ").strip() 
  while True:
    sentidoInput = input("Ascendente (A) o Descendente (D): ").strip().lower()
    sentidoOrden = (sentidoInput != "d") # True = Ascendente, False = Descendente
    if sentidoInput in ("a", "d"):
      break
    else:
      print_error("Opción inválida. Vuelva a intentarlo...")
      continue
  return opcionInput, sentidoOrden

# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    # Resolver ruta al CSV relativa al archivo .py (Windows/Linux/macOS)
    base_dir = Path(__file__).resolve().parent
    archivoCSV = str(base_dir / "paises.csv")
    if not Path(archivoCSV).exists():
        print_error(f"ERROR: No se encontró el archivo CSV en: {archivoCSV}")
        print("Sugerencias: coloque 'paises.csv' en la misma carpeta que este .py o actualice la ruta.")
        return
    paises = cargar_csv(archivoCSV)
    if not paises:
      print_error("No hay datos. Revisá el CSV.")
      # print("No hay datos. Revisá el CSV.") # Otra forma de mostrar el error.
      return
    actuales = paises[:]  # devuelve una nueva lista con todos los elementos de la lista "paises"
    while True: # Bucle principal del menú persistente.
      opcion = menu_principal()
      if opcion == "1":
        print("Puede ingresar el nombre completo o parcial del país.")
        print("O presione enter para ver la lista compelta.")
        inputNombre = input("Nombre país: ")
        res = buscar_por_nombre(actuales, inputNombre)
        mostrar_paises(res)
      elif opcion == "2":
        opcionFiltros = menu_filtros()
        if opcionFiltros == "1":
          cont = input("Continente: ")
          res = filtrar_por_continente(actuales, cont)
          mostrar_paises(res)
        elif opcionFiltros == "2":
          mn = pedir_int("Mín (Enter = sin mín): ", permitir_vacio=True)
          mx = pedir_int("Máx (Enter = sin máx): ", permitir_vacio=True)
          res = filtrar_por_poblacion(actuales, mn, mx)
          mostrar_paises(res)
        elif opcionFiltros == "3":
          mn = pedir_int("Mín (Enter = sin mín): ", permitir_vacio=True)
          mx = pedir_int("Máx (Enter = sin máx): ", permitir_vacio=True)
          res = filtrar_por_superficie(actuales, mn, mx)
          mostrar_paises(res)
        else:
          print_error("\nOpción inválida. Volviendo al menu principal...")
      elif opcion == "3":
        opcionOrden, sentidoOrden = menu_orden()
        if opcionOrden == "1":
          actuales = ordenar_por_nombre(actuales, sentidoOrden)
        elif opcionOrden == "2":
          actuales = ordenar_por_poblacion(actuales, sentidoOrden)
        elif opcionOrden == "3":
          actuales = ordenar_por_superficie(actuales, sentidoOrden)
        else:
          print_error("\nOpción inválida. Volviendo al menu principal...")
          continue
        mostrar_paises(actuales)
      elif opcion == "4":
        mx, mn = max_min_poblacion(actuales)
        prom_pob = promedio_poblacion(actuales)
        prom_sup = promedio_superficie(actuales)
        cuenta = cantidad_por_continente(actuales)
        if mx: print(f"\nMayor población: {mx['nombre']} ({mx['poblacion']:,})".replace(",", "."))
        if mn: print(f"Menor población: {mn['nombre']} ({mn['poblacion']:,})".replace(",", "."))
        if prom_pob is not None: print(f"Promedio de población: {prom_pob:,.2f}".replace(",", "."))
        if prom_sup is not None: print(f"Promedio de superficie: {prom_sup:,.2f}".replace(",", "."))
        print("Países por continente:")
        for continente, cantidadPaises in cuenta.items():
          print(f" - {continente}: {cantidadPaises}")
      elif opcion == "5":
        print("\n-- Agregar País --")
        nombre = primer_mayuscula(input("Nombre: "))
        if nombre == "":
          print("El nombre no puede estar vacío. Operación cancelada.")
          continue
        elif pais_existe(paises, nombre):
          print_error(f"El país '{nombre}' ya existe. Operación cancelada.")
          continue
        else:
          poblacion = pedir_int("Población: ")
          superficie = pedir_int("Superficie: ")
          continente = primer_mayuscula(input("Continente: "))
          while True:
            if continente not in arr_conttinentes:
              print_error(f"Continente inválido. Los continentes válidos son: {', '.join(arr_conttinentes)}. Intente nuevamente.")
              continente = primer_mayuscula(input("Continente: "))
            else:
              break
          paises.append({
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
          })
          actuales = paises[:]
          #Ahora guardamos el nuevo pais en el CSV
          with open(archivoCSV, "a", encoding="utf-8", newline="") as archivo:
            archivo.write(f"\n{nombre},{poblacion},{superficie},{continente}")
          print(f"País '{nombre}' agregado exitosamente.")
      elif opcion == "6":
        print("\n-- Actualizar País --")
        nombre = primer_mayuscula(input("Nombre del país a actualizar: "))
        if not pais_existe(paises, nombre):
          print_error(f"El país '{nombre}' no existe. Operación cancelada.")
          continue
        for pais in paises:
          if pais["nombre"].lower() == nombre.lower():
            print("Que valor desea actualizar?")
            print("1) Población")
            print("2) Superficie")
            print("3) Continente")
            opcionActualizar = input("Opción: ").strip()
            if opcionActualizar == "1":
              nueva_poblacion = pedir_int("Nueva Población: ")
              pais["poblacion"] = nueva_poblacion
            elif opcionActualizar == "2":
              nueva_superficie = pedir_int("Nueva Superficie: ")
              pais["superficie"] = nueva_superficie
            elif opcionActualizar == "3":
              nuevo_continente = primer_mayuscula(input("Cambiar Continente: "))
              while True:
                if nuevo_continente not in arr_conttinentes:
                  print_error(f"Continente inválido. Los continentes válidos son: {', '.join(arr_conttinentes)}. Intente nuevamente.")
                  nuevo_continente = primer_mayuscula(input("Continente: "))
                else:
                  break
              pais["continente"] = nuevo_continente
            break
        # Ahora guardamos los cambios en el CSV sobrescribiendo todo el archivo
        with open(archivoCSV, "w", encoding="utf-8", newline="") as archivo:
          archivo.write("nombre,poblacion,superficie,continente\n")
          for pais in paises:
            archivo.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")
        actuales = paises[:]
        print(f"País '{nombre}' actualizado exitosamente.")
      elif opcion == "7":
        print("¡Saliendo del programa!")
        break
      else:
        print_error()

if __name__ == "__main__":
  main()