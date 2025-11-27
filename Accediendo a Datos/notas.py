contador = 0

with open("Archivos/notas.txt", "r") as f:
    for line in f:
        if "aprobado" in line:
            contador += 1
            
print(f"Número de líneas con la palabra 'aprobado': {contador}")