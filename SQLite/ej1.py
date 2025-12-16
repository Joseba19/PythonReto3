import sqlite3

print(sqlite3.sqlite_version)

conn = sqlite3.connect("db1.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS comidas(id INT PRIMARY KEY, name TEXT, cuantity INT)")

#cursor.execute("INSERT INTO comidas (id, name, cuantity) VALUES (1, 'Cake', 55), (2, 'Biscuit', 44), (3, 'Soft Drinks', 10)")

introducir = input("Quieres introducir datos? ")

if introducir == "Si":
    comida = input("Comida: ")
    cantidad = int(input("Cantidad: "))

    cursor.execute("SELECT * FROM comidas")

    lista = cursor.fetchall()

    contador = 1

    for l in lista:
        contador += 1
        
    cursor.execute(f"INSERT INTO comidas (id, name, cuantity) VALUES ({contador}, '{comida}', {cantidad})")

cursor.execute("SELECT * FROM comidas")

salida = cursor.fetchall()

print("\n")
print("--- Cantidades ---")

for s in salida:
    print(f"{s[1]}: {s[2]}")

conn.commit()
conn.close()