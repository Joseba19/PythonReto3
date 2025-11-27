alumnos = ["Maria", "Juan", "Pepe", "Isabel", "Julio"]
contador = 0

for n in alumnos:
    asistencia = input(f"Ha venido {n}? ")
    if asistencia == "y":
        contador += 1
        
print(f"Hoy han venido a clase {contador} alumno(s)")