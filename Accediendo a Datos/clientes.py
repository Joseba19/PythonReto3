with open("Archivos/clientes_local.txt", "r") as f:
    for line in f:
        x, y, z = line.split(", ")
        y = y.replace("@", "*").replace("j", "*").replace("a", "*").replace("i", "*")
        print(f"{x}, {y}, {z}")