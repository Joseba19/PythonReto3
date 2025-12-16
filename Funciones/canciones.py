def crear_playlist(*canciones):
    if len(canciones) > 0:
        print("Tu playlist tiene las siguientes canciones: ", end="")    
        for cancion in canciones:
            print(cancion, end=", ")
    else:
        print("No añadiste ninguna cancion a la playlist")

if __name__ == "__main__":
    
    crear_playlist("Amsterdam", "It's Time", "Tokyo")