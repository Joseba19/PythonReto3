temperaturas = [3955]
temperaturasCopy = []
maquina = []
top5t = []
contador = 1
contador2 = 0

with open("Archivos/maquinas.txt", "r") as f:
    for line in f:
        line = line.split("!")
        maquina.append(line[0])
        for n in line:
            if "TEMP" in n:
                n = n.split("=")
                for i in n:
                    if i.isnumeric():
                        i = int(i)
                        for t in temperaturas:
                            if i > t:
                                contador2 += 1
                            else:
                                temperaturas.insert(contador, i)
                                contador = 0
                                break

                            if contador2 >= len(temperaturas):
                                temperaturas.append(i)
                                contador = 0
                                break
                            print(temperaturas)

print(temperaturas)