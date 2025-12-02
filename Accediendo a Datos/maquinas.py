temperaturas = []
temperaturasCopy = []
maquina = []
top5t = []
contador = 1

with open("Archivos/maquinas.txt", "r") as f:
    for line in f:
        line = line.split("!")
        maquina.append(line[0])
        for n in line:
            if "TEMP" in n:
                n = n.split("=")
                for i in n:
                    if i.isnumeric():
                        temperaturas.append(i)

temperaturasCopy = temperaturas
temperaturas.sort()
print(maquina)

print(temperaturas)
longitud = int(len(temperaturas))

for t in range(5):
    top5t.append(temperaturas[longitud - contador])
    contador += 1

print(top5t)

with open("Archivos/resultado.txt", "w") as f:
    f.write("== INFORME DE TEMPERATURAS HELIOS FACTORY ==\n")
    f.write("\n")
    f.write("Top 5 Maquinas por Temperatura:\n")
    f.write("\n")
    f.write(f"1. Temp = {top5t[0]}\n")
    f.write(f"2. Temp = {top5t[1]}\n")
    f.write(f"3. Temp = {top5t[2]}\n")
    f.write(f"4. Temp = {top5t[3]}\n")
    f.write(f"5. Temp = {top5t[4]}\n")
    f.write(f"\n")
    f.write(f"Maquinas por Nombre:\n")
    for i in range(longitud):
        f.write(f"{maquina[i]}: Temp: {temperaturasCopy[i]}\n")