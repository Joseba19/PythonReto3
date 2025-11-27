respuesta = input("Introduce 's' para empzar y 'q' para quitar: ")

while respuesta != "s" and respuesta != "q":
    respuesta = input("Introduce 's' o 'q': ")

if respuesta == "s":
    print("\n --- Factory initialised --- Factory configuration loaded:\n")
    with open("Archivos/config.txt", "r") as f:
        for line in f:
            dato, number = line.split("=")
            if dato == "production_lines":
                print(f"Production Lines: {number}")
            elif dato == "max_robots_per_line":
                print(f"Maximum robots per line: {number}")
else:
    print("Saliendo del programa")