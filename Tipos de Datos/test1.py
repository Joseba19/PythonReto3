# INT, FLOAT, STRING, BOOL, NONE
# Nombrando Variables
# camelCase = nombreAlumno, PascalCase = NombreAlumno, snake_case = nombre_alumno

nombreDelAlumno = "Jon"
NombreDelAlumno = "Aaron"
nombre_del_profesor = "Che"

# Numeros
a = 433.24
b = 0.234
#print("Completed in %d %.2f" %(a, b))   # d = int, f = float, s = str
#print(f"Completed in {round(a, 1)}")    # round() sirve para redondear una variable.

a = 50
b = 50
print(a == b)
#print(id(a))
#print(id(b))

x = None
if x:
    print("X no es nulo")
else:
    print("X es nulo")

#print(bool(0))
#print(bool(1))
#print(bool(True))