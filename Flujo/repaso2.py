comida = 45
transporte = 10.99
entretenimiento = 15

gastosTotal = comida + transporte + entretenimiento

print(f"Gastos fijos: {round(gastosTotal, 2)}€")

print(f"Gastos con 5 alumnos: {round(gastosTotal * 5, 2)}€")

alumnos = int(input("Cuantos alumnos hay?"))

gastosTotalAlumnos = gastosTotal * alumnos

print(f"Gastos con tus alumnos actuales {alumnos}: {round(gastosTotalAlumnos, 2)}€")

if gastosTotalAlumnos >= 100 and gastosTotalAlumnos < 200:
    print("Cuidado que estas gastando mucho")
elif gastosTotalAlumnos >= 200:
    print("Te recomiendo encarecidamente abrirte una cuenta de ahorros")
else:
    print("Estas gastando poco, sigue asi")