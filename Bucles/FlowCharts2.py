A = input("Introduce un numero: ")
B = input("Introduce un numero: ")
C = input("Introduce un numero: ")

BIG = A

if B > BIG:
    BIG = B

if C > BIG:
    BIG = C

print(f"El numero mas alto es {BIG}")