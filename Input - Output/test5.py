print("Bienvenido a Zara. Una camiseta cuesta 10.50€ y un pantalon 3.00€")

numCamisetas = int(input("Cuantas camisetas quieres? "))
numPantalon = int(input("Cuantos pantalones quieres? "))

resultado = str(numCamisetas * 10.50 + numPantalon * 3.00)

print("El total de la compra son: " + resultado + "€")