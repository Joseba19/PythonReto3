inventario = []

datos = int(input("Quieres introducir datos? En caso de que si, teclee el numero de la cantidad de datos que quieras introducir. En caso de que no, introduzca 0: "))

for i in range(datos):
    print("\n")
    producto = input("Introduzca el producto: ")
    cantidad = input("Introduzca la cantidad: ")
    with open("productos.txt", "a") as f:
        f.write(f"{producto} {cantidad}\n")   
        
with open("productos.txt", "r") as f:
    f.readline()
    for line in f:
        productos = line.strip().split(" ")
        productos[1] = int(productos[1])
        inventario.append({"producto": productos[0], "qty": productos[1]})

for i in inventario:
    print(f"Producto: {i["producto"]}, Cantidad: {i["qty"]}")
