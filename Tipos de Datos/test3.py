# Media, maximo y minimo de notas
suma = 0
maximo = 0
minimo = 10
i = 1

for i in range(5):
    nota = int(input("Introduzca la nota del alumno: "))

    while nota < 0 or nota > 10:
        nota = input("Nota no valida, debe ser entre 0 y 10: ")

    suma = nota + suma
    
    if nota > maximo:
        maximo = nota

    if nota < minimo:
        minimo = nota

media = suma / 5

print(f"La media de las notas es: {media}")
print(f"La nota mas alta ha sido: {maximo}")
print(f"La nota mas baja ha sido: {minimo}")