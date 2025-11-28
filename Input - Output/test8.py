largo = float(input("Introduce el largo de la (En Metros): "))
ancho = float(input("Introduce el ancho de la piscina (En Metros): "))
profundidad = float(input("Introduce la profundidad de la piscina (En Metros): "))

volumen = largo * ancho * profundidad
litros = volumen * 1000

print(f"En la piscina te entran {int(litros)} Litros")