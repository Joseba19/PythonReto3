# Ejercicios de Python Generados

Estos ejercicios han sido creados analizando tu código actual. Cubren desde conceptos básicos hasta manejo de archivos y bases de datos, ordenados de menor a mayor dificultad.

## 1. Saludo y Cálculos Básicos (Variables e Input/Output)
**Conceptos:** `input`, `print`, f-strings, operaciones matemáticas.
**Objetivo:** Crea un script que pida al usuario su nombre y su año de nacimiento. El script debe saludar al usuario y decirle cuántos años cumplirá este año (asumiendo el año actual es 2025).
**Ejemplo:**
```text
Nombre: Joseba
Año nacimiento: 1990
Hola Joseba, este año cumplirás 35 años.
```

## 2. Par o Impar (Condicionales)
**Conceptos:** `if`, `else`, operador módulo `%`.
**Objetivo:** Pide un número entero al usuario. Si el número es par, imprime "Es par". Si es impar, imprime "Es impar".
**Pista:** Un número es par si el resto de dividirlo entre 2 es 0.

## 3. La Tabla de Multiplicar (Bucles For)
**Conceptos:** `for`, `range`.
**Objetivo:** Pide un número al usuario e imprime su tabla de multiplicar del 1 al 10.
**Ejemplo:**
```text
Numero: 5
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

## 4. Lista de la Compra (Listas y Bucles While)
**Conceptos:** `list`, `append`, `while`, `input`.
**Objetivo:** Crea un programa que permita al usuario añadir artículos a una lista de la compra. El programa debe seguir pidiendo artículos hasta que el usuario escriba "FIN". Al final, imprime la lista completa.

## 5. Calculadora de Funciones (Funciones)
**Conceptos:** `def`, argumentos, `return`.
**Objetivo:** Define una función llamada `calcular_precio_final` que reciba dos parámetros: `precio` y `impuesto` (por defecto 21). La función debe devolver el precio con el impuesto aplicado. Prueba la función con diferentes valores.

## 6. Contador de Frecuencia (Diccionarios)
**Conceptos:** `dict`, iteración de strings.
**Objetivo:** Pide una frase al usuario. Usa un diccionario para contar cuántas veces aparece cada vocal (a, e, i, o, u) en la frase. Imprime el resultado.
**Ejemplo:** "Hola mundo" -> `{'a': 1, 'o': 2, 'u': 1}`

## 7. Lector de Configuración (Manejo de Archivos)
**Conceptos:** `open`, `read`, `split`.
**Objetivo:** Crea un archivo de texto llamado `config.txt` con el contenido `usuario=admin;puerto=8080`. Crea un script de Python que lea este archivo, separe la información y la guarde en un diccionario. Imprime el diccionario.

## 8. Validador de Contraseñas (Lógica y Strings)
**Conceptos:** Métodos de string (`isupper`, `isnumeric`), lógica booleana.
**Objetivo:** Crea una función que valide una contraseña. Debe cumplir:
- Al menos 8 caracteres.
- Contener al menos un número.
- Contener al menos una mayúscula.
El programa debe pedir contraseñas hasta que el usuario introduzca una válida.

## 9. Gestor de Notas JSON (JSON)
**Conceptos:** `json`, `dump`, `load`.
**Objetivo:**
1. Crea una lista de diccionarios, donde cada diccionario es un alumno con "nombre" y "nota".
2. Guarda esta lista en un archivo `notas.json`.
3. Lee el archivo y calcula la nota media de la clase.

## 10. Inventario Simple (SQLite)
**Conceptos:** `sqlite3`, `connect`, `cursor`, `execute`.
**Objetivo:**
1. Conecta a una base de datos `inventario.db`.
2. Crea una tabla `productos` con `id`, `nombre` y `stock`.
3. Pide al usuario un nombre de producto y una cantidad, e insértalo en la base de datos.
4. Muestra todos los productos guardados en la base de datos.
