acciones = {"MSFT": 91.5, "REP": 7.91, "BBVA": 6.9}
ValorAcciones = []

for valor in acciones.values():
    print(f"Valor de la accion: {valor}")

for clave, valor in acciones.items():
    print(f"{valor}: {clave}")
    
acciones.update({"IBE": 9.99})

PrecioMicrosoft = float(input("introduzca el precio actual de las acciones de Microsoft: "))

acciones.update({"MCF": PrecioMicrosoft})

del acciones["REP"]

NombreAccion = input("Introduzca una nueva accion: ")
PrecioAccion = float(input("introduzca el valor de la accion: "))

acciones.update({NombreAccion: PrecioAccion})

for clave, valor in acciones.items():
    print(f"{clave}: {valor}")

for valor in acciones.values():
    ValorAcciones.append(valor)

ValorAcciones.sort()

print(ValorAcciones)