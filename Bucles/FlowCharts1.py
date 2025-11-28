count = 0
sum = 0
num = input("Introduce un numero: ")

while num.isnumeric():
    sum = sum + int(num)
    count += 1
    num = input("Introduce mas numeros, o pulsa 'q' para salir: ")
    
average = sum / count
print(f"La suma de los numeros es {sum}, y la media es {average}")