ventas = [3, 14, 7, 8, 10, 13, 16]
dia = 0
for venta in ventas:
    dia = dia + 1
    if venta > 10:
        print(f"Dia {dia}: Mas de 10 ventas!!! BONUUUUUUS")

if sum(ventas) < 50:
    print("Menos de 50 ventas, animo, la semana que viene ira mejor")

ventaHoy = int(input("Cuanto has vendido hoy? "))

ventas.append(ventaHoy)

print(ventas)

ventas.remove(ventas[2])

print(ventas)