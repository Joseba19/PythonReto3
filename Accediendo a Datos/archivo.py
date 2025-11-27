result = []

#with open("server.log", "r") as f:
#   lineas = f.readlines()

with open("server.log", "r") as f:
    for line in f:
        if "ERROR" in line.upper():
            result.append(line)
            
with open("error.txt", "w") as f:
    f.write("\n".join(result))