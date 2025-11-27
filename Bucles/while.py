"""
Ejercicio 1

contraseña = "password"
respuesta = input("Introduce la contraseña: ")

while respuesta != contraseña:
    respuesta = input("Contraseña incorrecta. Vuelve a intentar: ")

print("Acceso concedido")
"""

"""
Ejercicio 2

contador = 50

while contador >= 10:
    print(contador)
    contador -= 1
"""

"""
Ejercicio 3

contador = 0

while contador <= 99:
    if (contador % 10 != 0):
        print(contador)
    contador += 1
"""

"""
Ejercicio 4

numero = int(input("Introduce un numero positivo: "))

while numero <= 0:
    numero = int(input("El numero tiene que ser positivo, repite: "))

print("Eskerrik Asko!")
"""

"""
Ejercicio 5

asterisco = "*"
contador = 0
finCiclo = int(input("Introduce un numero positivo: "))

while contador <= finCiclo:
    print(asterisco)
    asterisco = asterisco + "*"
    contador += 1
"""

"""
Ejercicio 6

asterisco = "*"
contador = 0
finCiclo = int(input("Introduce un numero positivo: "))

while contador <= finCiclo * 2 + 1:
    if contador <= finCiclo:
        print(asterisco)
        asterisco = asterisco + "*"
    if contador >= finCiclo:
        print(asterisco)
        asterisco = asterisco[:-1]
    contador += 1
"""