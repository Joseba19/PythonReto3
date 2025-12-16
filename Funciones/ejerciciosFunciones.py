def repetirKaixo(x):
    """Si pones un comentario aqui, aparece cuando dejas el raton encima de la llamada a la funcion"""
    for i in range(x):
        print(f"Kaixo {i + 1}")

def calcular_area(base, altura):
    return f"El area del rectangulo son {base * altura} cm2"

def coste_coche(motor = "preguntar", carroceria = "preguntar", pintura = "preguntar"):
    """ Poner el valor 'preguntar' para que se le pida por consola al usuario la cantidad de cada cosa """
    if motor == "preguntar":
        motor = float(input("Introduce la cantidad de motores: "))
    if carroceria == "preguntar":
        carroceria = float(input("Introduce la cantidad de carrocerias: "))
    if pintura == "preguntar":
        pintura = float(input("Introduce la cantidad de pintura en litros: "))

    return f"El coste del cohce son {motor * 3200 + carroceria * 4500 + pintura * 35}€"

def imprimir(*args):
    for i in args:
        print(i)

def CalculadoraIMC(peso, altura):
    IMC = float(peso / (altura ** 2))
    
    if IMC < 18.5:
        return f"Tu IMC es: {IMC}. Estas en infrapeso"
    elif IMC >= 18.5 and IMC < 25:
        return f"Tu IMC es: {IMC}. Estas en un buen peso"
    elif IMC >= 25 and IMC < 30:
        return f"Tu IMC es: {IMC}. Estas en sobrepeso"
    elif IMC >= 30:
        return f"Tu IMC es: {IMC}. Estas obeso"
    
 
if __name__ == "__main__":
    repetirKaixo(3)
    
    print(calcular_area(5, 7))
    
   # print(coste_coche())
    
    imprimir(1, 4, 6, "Joseba")
    
    print(CalculadoraIMC(120, 1.60))