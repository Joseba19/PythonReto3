from math_common import sumar, restar, multiplicar, dividir

if __name__ == "__main__":

    accion = input("Bienvenido a la calculadora. 's' para sumar, 'r' para restar, 'm' para multiplicar y 'd' para dividir: ")
    numero1 = int(input("Introduzca el primer valor: "))    
    numero2 = int(input("Introduzca el segundo valor: "))

    if accion == "s":
        x = sumar(numero1, numero2)
        print(x)
    elif accion == "r":
        x = restar(numero1, numero2)
        print(x)
    elif accion == "m":
        x = multiplicar(numero1, numero2)
        print(x)
    elif accion == "d":
        x = dividir(numero1, numero2)
        print(x)