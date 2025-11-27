'''
notas = [3, 6, 7, 10, 3, 8, 9, 7] #En una misma array se pueden meter tipos de datos diferentes

#print(notas[0])
#print(len(notas))

notas[3] = "Aprobado" #Se pueden cambiar elementos de la array (Es una lista MUTABLE)

#print(notas)

for n in notas:
    if n == 6:
        print("N es 6")
    else:
        print(n)
'''
'''
frutas = ["Manzana", "Pera", "Kiwi", "Tomate", "Mango", "Kiwi", "Kiwi"]

frutas.append("Sandia") # Añade un objeto al final de la lista
frutas.insert(2, "Melon") # Añade otro objeto, pero en la posicion que quieras (empezando desde 0)
frutas.remove("Manzana") # Elimina ese objeto de la lista, si hay 2 objetos o mas iguales, solo eliminara el primero

print(frutas[len(frutas) - 1]) # Sacar el ultimo objeto de la lista, sea cual sea la longitud
#print(frutas[2])

if "Kiwi" in frutas:
    print("Hay kiwi") # Verifica sin hay un elemento en la array
'''

frutas = ("Kiwi", "Manzana", "Platano") #Esto es una tupla, es una lista inmutable

