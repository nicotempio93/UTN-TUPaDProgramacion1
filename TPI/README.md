# Resolucion trabajo practico integrador con Python

## Descripción del proyecto

Aplicación de consola que carga un archivo CSV que contiene información de países (nombre, población, superficie y continente) y permite **buscar**, **filtrar**, **ordenar** y obtener **estadísticas** sobre dicha información.

### Datos

TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN (modalidad a distancia) - UNIVERSIDAD TECNOLÓGICA NACIONAL
**Programacion I**
**Comision 9:**

## Docentes

- Coordinador - Alberto Cortez
- Profesor - Sebastian Bruselario
- Tutora - Flor Gubiotti
  **Integrantes**
  -Nadaf, Facundo Federico
  -Tempio, Nicolas

## Requisitos

- Python 3.10+
- Archivo CSV en `Trabajo_practico_integrador-199/paises.csv` con el encabezado:
  `nombre,poblacion,superficie,continente`

## Estructura

- `/integrador_199.py` Programa completo (carga CSV, filtros, ordenamientos, estadistica) donde cada función se encarga de una tarea especifica y que al combinar todas se obtiene el programa final.
- `/paises.csv` Dataset CSV
- `/informe.pdf` Informe final en PDF

## 🔗 Links

- Video de presentación:

- Repositorio GitHub: https://github.com/cufa03/UTN-TUPaDProgramacion1/tree/main/Trabajo_practico_integrador-199

## Instrucciones de ejecución

```bash
py integrador_199.py
```

Una vez ejecutado el programa se mostrara un menu con la siguiente estructura:
----- Gestión de Países -----

1. Buscar país por nombre
2. Filtrar países
3. Ordenar países
4. Estadísticas
5. Salir

Donde el usuario debere elegir la opcion deseada para seguir con la ejecución.

- Si la opción escogida es 1, luego debera ingresar el nombre (completo o parcial) del país a buscar que de forma siguiente se mostrara la información del o los paises que coincidan con la busqueda.

- Si la opción escogida es 2, se mostrara el menu de filtros:

----- Filtros -----

1. Por continente
2. Por rango de población
3. Por rango de superficie
   Donde el usuario debera elegir el metodo para filtrar los paises.

- Si la opción escogida es 3, se mostrara el menu de ordenamiento:

----- Ordenar -----

1. Por nombre
2. Por población
3. Por superficie

Donde el usuario debera elegir el parametro de ordenamiento deseado para mostrar los paises.

- Si la opción escogida es 4, se mostrara información estadistica sobre los datos almacenados en el archivo csv.
  Mostrando el país con mayor población, con menor, el promedio de población, el promedio de superficie y la cantidad de paises por continente.

- Si por ultima la opcion es 5, se termina la ejecución del programa.

## Ejemplo de ejecución

**Primer paso**
Al mostrarse el menu el usuario debera ingresar un numero del 1 al 5, en este caso ingresamos opción 1.
----- Gestión de Países -----

1. Buscar país por nombre
2. Filtrar países
3. Ordenar países
4. Estadísticas
5. Salir

Opción: 1

**Segundo paso**
Al ingresar al menu de "Buscar país por nombre", se le solicita ingresar el nombre del pais que se desea buscar (ya sea parcial o nombre completo). En este caso se ingresa "arg".

Puede ingresar el nombre completo o parcial del país.
O presione enter para ver la lista compelta.
Nombre país: arg

**Tercer paso**
Luego de ingresar "arg" y presionar enter, se muestra el resultado de la busqueda que coincida con la palabra ingresada. En este caso es la siguiente:

Item. País — Continente — Pob: Población — Sup: Superficie

1. Argentina — América — pob: 45.376.763 — sup: 2.780.400

-- Volviendo al menu --

Por ultimo, se vuelve al menu principal donde se vuelve a solicitar el ingreso de la opción deseada.
