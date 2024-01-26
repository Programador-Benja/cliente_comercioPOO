usuarios = {}

def bienvenida():
    print("\n¡Bienvenido a Compras.Net!\n")

def registro_de_usuarios(user):
    bienvenida()
    print("\tSign up")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    
    user[usuario] = contraseña
    print("\n \tRegistro existoso!\n")

def leer_registros(user):
    for nombre, contraseña in user.items():
        print(f"{nombre} : {contraseña}")

def guardar_archivo(user):
    file = open("base_de_datos.txt","w")
    file.write("\t Usuarios registrados en la Plataforma\n")

    for nombre, contraseña in user.items():
        file.write(f"{nombre} : {contraseña}\n")
    
    file.close()

def iniciar_sesion(users):
    print("\n \tLogin")
    usuario = input("Ingrese su usuario: ")

    for user, password in users.items():
        if usuario == user:
            contraseña = input("Ingrese su contraseña: ")
            if contraseña == password:
                print(f"\nBienvenido/a {usuario}")
            else:
                print("\nContraseña incorrecta!")
        else:
            print("\nUsuarion no encontrado!")