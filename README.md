# Apuntes de Python basados en los ejercicios de clase

## Índice
1. [Variables y Tipos de Datos](#variables-y-tipos-de-datos)
2. [Entrada y Salida (Input/Output)](#entrada-y-salida-inputoutput)
3. [Operadores](#operadores)
4. [Control de Flujo](#control-de-flujo)
5. [Manipulación de Cadenas (Strings)](#manipulación-de-cadenas-strings)
6. [Estructuras de Datos](#estructuras-de-datos)
7. [Manejo de Archivos](#manejo-de-archivos)
8. [Notas y Buenas Prácticas](#notas-y-buenas-prácticas)

---

## Variables y Tipos de Datos

En los ejercicios hemos trabajado con los tipos de datos fundamentales en Python. Python es un lenguaje de tipado dinámico, lo que significa que no necesitamos declarar el tipo de variable explícitamente.

### Tipos Básicos
*   **Enteros (`int`)**: Números sin decimales (ej. `50`, `0`, `-1`).
*   **Flotantes (`float`)**: Números con decimales (ej. `433.24`, `0.234`).
*   **Cadenas de texto (`str`)**: Texto entre comillas dobles o simples (ej. `"Jon"`, `'Hola'`).
*   **Booleanos (`bool`)**: Valores de verdad (`True`, `False`).
*   **None**: Representa la ausencia de valor.

### Convenciones de Nombres
Hemos visto diferentes formas de nombrar variables:
*   **snake_case**: `nombre_alumno` (Recomendado en Python para variables y funciones).
*   **camelCase**: `nombreAlumno`.
*   **PascalCase**: `NombreAlumno` (Usualmente para Clases).

### Conversión de Tipos (Casting)
A veces es necesario convertir un tipo de dato a otro, especialmente al leer datos del usuario.
```python
# Convertir a entero
numero = int("10")

# Convertir a flotante
decimal = float("5.5")

# Convertir a string
texto = str(123)
```

---

## Entrada y Salida (Input/Output)

### Mostrar datos (`print`)
Usamos la función `print()` para mostrar información en la consola. Una forma muy potente y legible que hemos usado frecuentemente son los **f-strings** (formatted strings), que permiten incrustar variables directamente en el texto.

```python
nombre = "Maria"
edad = 20
print(f"La alumna {nombre} tiene {edad} años.")
```

También hemos visto el redondeo de números al imprimir:
```python
precio = 19.999
print(f"Precio: {round(precio, 2)}")
```

### Leer datos (`input`)
La función `input()` detiene el programa y espera a que el usuario escriba algo. **Importante**: `input()` siempre devuelve un texto (`str`). Si necesitamos un número, debemos convertirlo.

```python
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: ")) # Convertimos a entero inmediatamente
```

---

## Operadores

### Aritméticos
Para realizar cálculos matemáticos básicos:
*   Suma: `+`
*   Resta: `-`
*   Multiplicación: `*`
*   División: `/`
*   **Módulo (Resto)**: `%` (Devuelve el resto de la división. Muy útil para saber si un número es par o impar).
    ```python
    if numero % 2 == 0:
        print("Es par")
    ```

### Comparación
Devuelven un valor booleano (`True` o `False`).
*   Igualdad: `==`
*   Desigualdad: `!=`
*   Mayor que: `>`
*   Menor que: `<`

### Lógicos
Para combinar condiciones.
*   `and`: Ambas condiciones deben ser verdaderas.
*   `or`: Al menos una condición debe ser verdadera.
*   `not`: Invierte el valor de verdad.

---

## Control de Flujo

### Condicionales (`if`, `elif`, `else`)
Permiten ejecutar bloques de código solo si se cumple una condición.

```python
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

### Bucles (`Loops`)

#### Bucle `while`
Repite un bloque de código mientras una condición sea verdadera. Es útil cuando no sabemos cuántas veces se repetirá el código (por ejemplo, validación de entrada).

```python
respuesta = ""
while respuesta != "s":
    respuesta = input("Introduce 's' para salir: ")
```

#### Bucle `for`
Se utiliza para iterar sobre una secuencia (como una lista o un rango de números).

**Iterar un número fijo de veces con `range()`:**
```python
for i in range(5):
    print(f"Iteración número {i}")
```

**Iterar sobre elementos de una colección:**
```python
alumnos = ["Ana", "Luis", "Pepe"]
for alumno in alumnos:
    print(alumno)
```

---

## Ejemplos de Lógica (FlowCharts)

Hemos practicado la lógica de programación con ejercicios de diagramas de flujo traducidos a Python.

### Cálculo de Media (Bucle While)
Este ejercicio (`FlowCharts1.py`) pide números al usuario hasta que decide parar, y calcula la suma y la media.

```python
count = 0
sum = 0
num = input("Introduce un numero: ")

while num.isnumeric():
    sum = sum + int(num)
    count += 1
    num = input("Introduce mas numeros, o pulsa 'q' para salir: ")
    
average = sum / count
print(f"La suma de los numeros es {sum}, y la media es {average}")
```

### Mayor de 3 números
Este ejercicio (`FlowCharts2.py`) determina cuál es el mayor de tres números introducidos.

```python
A = input("Introduce un numero: ")
B = input("Introduce un numero: ")
C = input("Introduce un numero: ")

BIG = A

if B > BIG:
    BIG = B

if C > BIG:
    BIG = C

print(f"El numero mas alto es {BIG}")
```

---
## Manipulación de Cadenas (Strings)

Las cadenas de texto son muy versátiles en Python. Hemos visto varias formas avanzadas de trabajar con ellas.

### Slicing (Rebanado)
Podemos extraer partes de una cadena usando índices `[inicio:fin]`.
```python
texto = "programazioa gustatzen zait"
subtexto = texto[13:22] # Extrae desde el índice 13 hasta el 21
```

### Métodos Útiles
*   `.strip()`: Elimina espacios en blanco al principio y al final. También `lstrip()` (izquierda) y `rstrip()` (derecha).
*   `.split(separador)`: Divide una cadena en una lista de subcadenas basándose en un separador.
*   `.join(lista)`: Une una lista de cadenas en una sola cadena.
*   `.replace(viejo, nuevo)`: Reemplaza partes del texto.
*   `.lower()`, `.upper()`, `.capitalize()`: Transforman a minúsculas, mayúsculas o primera letra mayúscula.

### Verificación de Contenido
*   `.isnumeric()`: Devuelve `True` si la cadena contiene solo números.
*   `.islower()`: Devuelve `True` si está en minúsculas.
*   `in`: Verifica si una subcadena existe dentro de otra.
    ```python
    if 'python' in mensaje:
        print('python existe')
    ```

### Desempaquetado de Variables
Podemos asignar valores a múltiples variables en una sola línea al dividir una cadena.
```python
nombre_completo = "Jon#Smith"
nombre, apellido = nombre_completo.split('#')
```

---

## Estructuras de Datos

### Listas
Son colecciones ordenadas y **mutables** (se pueden modificar). Se definen con corchetes `[]`.

```python
frutas = ["Manzana", "Pera", "Kiwi"]

# Acceder a elementos (índice empieza en 0)
print(frutas[0]) # Manzana

# Añadir elementos
frutas.append("Sandia")

# Insertar en posición específica
frutas.insert(1, "Melon")

# Eliminar elementos
frutas.remove("Manzana")

# Longitud de la lista
cantidad = len(frutas)
```

#### Filtrado de Listas
Un patrón común es crear una nueva lista con elementos que cumplen cierta condición (filtrar).

```python
numeros = [1, 5, 3, 2, 8]
numeros_impares = []

for n in numeros:
    if n % 2 != 0: # Si es impar
        numeros_impares.append(n)
```

### Tuplas
Son colecciones ordenadas pero **inmutables** (no se pueden modificar una vez creadas). Se definen con paréntesis `()`.

```python
colores = ("Rojo", "Verde", "Azul")
# colores[0] = "Amarillo" # Esto daría error
```

---

## Manejo de Archivos

Hemos trabajado intensamente en la lectura y escritura de archivos de texto, lo cual es fundamental para guardar datos persistentes.

### Estructura `with open()`
Es la forma recomendada de trabajar con archivos, ya que se encarga de cerrar el archivo automáticamente, incluso si ocurre un error.

**Modos de apertura:**
*   `"r"`: Lectura (Read).
*   `"w"`: Escritura (Write). Sobrescribe el archivo si existe.
*   `"a"`: Añadir (Append). Escribe al final sin borrar lo anterior.

### Lectura línea a línea
Un patrón muy común en los ejercicios ha sido leer un archivo línea por línea para procesar datos.

```python
datos_procesados = []

with open("datos.txt", "r") as archivo:
    for linea in archivo:
        # Limpiamos espacios en blanco y saltos de línea
        linea_limpia = linea.strip()
        
        # Si la línea tiene datos separados por comas
        if "," in linea_limpia:
            partes = linea_limpia.split(",")
            datos_procesados.append(partes)
```

### Escritura
```python
with open("informe.txt", "w") as f:
    f.write("Este es el resultado del análisis.\n")
```

---

## Manejo de JSON

JSON (JavaScript Object Notation) es un formato muy común para intercambiar datos. En Python usamos la librería `json`.

### Lectura de JSON
En el ejercicio `jsonReader.py` leemos un archivo de configuración.

```python
import json

with open("config.json", "r") as f:
    config = json.load(f)

print(config['database']['host'])         # localhost
print(config['features']['enable_logging'])  # True
```

---

## Métodos

A continuación, una referencia de todos los métodos y funciones que hemos visto en los ejercicios.

### Funciones Integradas (Built-in)
| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `print()` | Muestra información en consola. | `print("Hola")` |
| `input()` | Lee texto del usuario. | `nombre = input("Nombre: ")` |
| `int()` | Convierte a entero. | `int("5")` -> `5` |
| `float()` | Convierte a decimal. | `float("5.5")` -> `5.5` |
| `str()` | Convierte a texto. | `str(10)` -> `"10"` |
| `len()` | Devuelve la longitud (de lista o string). | `len([1,2])` -> `2` |
| `range()` | Genera una secuencia de números. | `range(5)` -> `0, 1, 2, 3, 4` |
| `round()` | Redondea un número. | `round(3.14159, 2)` -> `3.14` |
| `open()` | Abre un archivo. | `open("archivo.txt", "r")` |

### Métodos de Strings
| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.strip()` | Elimina espacios al inicio y final. | `" hola ".strip()` -> `"hola"` |
| `.split(sep)` | Divide el string en una lista. | `"a,b".split(",")` -> `['a', 'b']` |
| `.join(lista)` | Une una lista en un string. | `",".join(['a', 'b'])` -> `"a,b"` |
| `.replace(old, new)` | Reemplaza texto. | `"hola".replace("o", "a")` -> `"hala"` |
| `.lower()` | Convierte a minúsculas. | `"HOLA".lower()` -> `"hola"` |
| `.upper()` | Convierte a mayúsculas. | `"hola".upper()` -> `"HOLA"` |
| `.capitalize()` | Pone la primera letra en mayúscula. | `"hola".capitalize()` -> `"Hola"` |
| `.isnumeric()` | `True` si solo contiene números. | `"123".isnumeric()` -> `True` |
| `.islower()` | `True` si está en minúsculas. | `"abc".islower()` -> `True` |

### Métodos de Listas
| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.append(x)` | Añade `x` al final de la lista. | `lista.append(5)` |
| `.insert(i, x)` | Inserta `x` en la posición `i`. | `lista.insert(0, 5)` |
| `.remove(x)` | Elimina la primera aparición de `x`. | `lista.remove(5)` |

### Métodos de JSON
| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `json.load(f)` | Carga datos JSON desde un archivo. | `datos = json.load(archivo)` |

---
## Notas y Buenas Prácticas

Analizando los ejercicios, he notado algunos patrones y puntos importantes:

1.  **Validación de Entradas**: Es muy buena práctica usar bucles `while` para asegurar que el usuario introduce datos válidos (por ejemplo, una nota entre 0 y 10).
    ```python
    nota = -1
    while nota < 0 or nota > 10:
        nota = int(input("Introduce una nota válida (0-10): "))
    ```

2.  **Limpieza de Strings**: Al leer de archivos o inputs, métodos como `.strip()` (quitar espacios sobrantes), `.upper()` (convertir a mayúsculas) o `.replace()` son esenciales para normalizar los datos antes de procesarlos.

3.  **Acumuladores y Contadores**: Hemos usado frecuentemente variables inicializadas en 0 (`suma = 0`, `contador = 0`) dentro de bucles para calcular totales o contar ocurrencias.

4.  **Modularidad**: Aunque la mayoría de scripts son lineales, el uso de bloques separados para "Entrada", "Procesamiento" y "Salida" hace el código más legible.

---