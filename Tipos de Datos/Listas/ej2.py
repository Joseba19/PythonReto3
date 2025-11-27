notas = [6, 4, 1, 10, 10, 7, 4]
suma = 0

for n in notas:
    suma += n

media = suma/len(notas)
alta = max(notas)
baja = min(notas)

print(f"Media de notas: {media}")
print(f"Nota mas alta: {alta}")
print(f"Nota mas baja: {baja}")