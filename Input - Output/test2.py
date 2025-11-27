nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")

#print("Hola, " + nombre + " " + apellido + "! Bienvenido/a.")

print(f"Hola, {nombre} {apellido}! Bienvenido/a.")

#print(f"Tienes {edad} años.")

print(f"El próximo año tendras {int(edad) + 1} años.")