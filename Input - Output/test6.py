print("Bienvenido al transformador de temperatura: ")
entrada = input("Pulsa 'f' para pasar de celsius a farenheit, o pusa 'c' para hacerlo al reves: ")

while entrada != "c" and entrada != "f":
    entrada = input("Entrada invalida, debe seleccionar una letra entre 'c' y 'f': ")

if entrada == "f":

    celcius = int(input("Introduce la temperadura en grados Celcius: "))
    farenheit = int((celcius * 9/5) + 32)
    print(f"La temperatura en Farenheit es: {farenheit}°F")
    
elif entrada == "c":

    farenheit = int(input("Introduce la temperadura en grados Farenheit: "))
    celcius = int((farenheit - 32) *  5/9)
    print(f"La temperatura en Farenheit es: {celcius}°C")

else:
    
    print("Debes introoducir una letra entre c y f")