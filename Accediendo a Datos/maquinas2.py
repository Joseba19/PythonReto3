temperaturas = []

with open("Archivos/maquinas.txt", "r") as f:
    for line in f:
        partes = line.split("!")
        for n in partes:
            if "TEMP" in n:
                # extraer valor numérico
                valor = int(n.split("=")[1])
                
                # insertar ordenado
                pos = 0
                while pos < len(temperaturas) and temperaturas[pos] < valor:
                    pos += 1
                temperaturas.insert(pos, valor)

print(temperaturas)
