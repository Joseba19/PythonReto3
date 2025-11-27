#Inicio de Sesion de Banco
USER = "Joseba"
PASSWD = "2430"
InicioSesion = False

print("Bienvenido a CeBank")
usuario = input("Introduzca su nombre de usuario: ")
contraseña = input("Introduzca su contraseña: ")


if usuario == USER:
    if contraseña == PASSWD:
        #print("Sesion iniciada correctamente")
        InicioSesion = True
    else:
        #print("Contraseña incorrecta")
        InicioSesion = False
else:
    #print("El usuario no existe")
    InicioSesion = False

if InicioSesion:
    print("Sesion iniciada correctamente")
else:
    print("Algo ha fallado")
