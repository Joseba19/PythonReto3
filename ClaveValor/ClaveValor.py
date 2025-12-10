dict = {"nombre": "Juan",
        "edad": 22,
        "profesion": "Carpintero"}

print(type(dict))

#Items, keys, Values

for key, value in dict.items():
    print(f"Key is {key}, and value is {value}")
    
for key in dict.keys():
    print(f"The key is {key}")
    
for value in dict.values():
    print(f"The value is {value}")

print(dict["nombre"])   # dict.get("nombre") en caso de error, esta opcion muetsra "None" en vez de error

dict["edad"] = 99   # Si introduces una clave no establecida se agrega al final del diccionario 
print(dict["edad"])

dict.update({"Activo": "Si"}) #Añade al final del disccionario o sobreescribe
