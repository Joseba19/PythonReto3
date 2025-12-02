tempOrdenado = []
temp = []
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
                        temp.append(i)
                        tempOrdenado.append(i)

tempOrdenado.sort()

longitud = int(len(tempOrdenado))

for t in range(5):
    top5t.append(tempOrdenado[longitud - contador])
    contador += 1

with open("Archivos/resultado.txt", "w") as f:
    f.write("== INFORME DE TEMPERATURAS HELIOS FACTORY ==\n")
    f.write("\n")
    f.write("Top 5 Maquinas por Temperatura:\n")
    f.write("\n")
    for i in range(5):
        f.write(f"{i + 1}. Temp = {top5t[i]}\n")
    f.write(f"\n")
    f.write(f"Temperatura de las maquinas por nombre:\n")
    f.write("\n")
    for i in range(longitud):
        f.write(f"{maquina[i]}: {temp[i]}\n")
