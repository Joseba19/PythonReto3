# Termninar este programa para la gestión de la configuración de un servidor
import json

config = { }

configFile = "config.json"

with open(configFile, "r") as f:
    pass

def gestion_configuracion():
    print("Elija una opción:")
    print("1. Obtener configuración")
    print("2. Actualizar configuración")
    print("3. Listar todas las configuraciones")
    
    opcion = int(input("Introducur el número de la opción: "))

    match opcion:
        case 1:
            clave = input("Introducur la clave que desea obtener: ")
            # mostrar la clave deseada
            for key, value in config.items():
                if key == clave:
                    print(f"El valor de {key} es: {value}")
            
        case 2:
            clave = input("Ingrese la clave que desea actualizar: ")
            valor = input("Ingrese el nuevo valor: ")
            # Actualizar el valor de uno de las opciones de configuración
            for key, value in config.items():
                if key == clave:
                    config.update({clave: valor})
                    print(f"El valor de {key} es: {valor}")
        case 3:
            # imprimir la configuración
            for key, value in config.items():
                print(f"La clave es: {key}, y el valor {value}")
        case _:
            print("Opción no válida. Intente nuevamente.")

# Llamar a la función de gestión
gestion_configuracion()