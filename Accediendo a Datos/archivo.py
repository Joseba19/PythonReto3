result = []

#with open("Archivos/server.log", "r") as f:
#   lineas = f.readlines()

with open("Archivos/server.log", "r") as f:
    for line in f:
        if "ERROR" in line.upper():
            result.append(line)
            
with open("Archivos/error.txt", "w") as f:
    f.write("\n".join(result))