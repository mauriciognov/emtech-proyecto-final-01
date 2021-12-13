# ARCHIVO DEL LOGIN DE USUARIO/ADMINISTRADOR AL SISTEMA

def login():
    usuario = 'mauricio'
    contrasena = 'emtech'
    intentos = 3

    while True:
        if intentos == 0:
            exit()
        username = input('Ingresa tu nombre de usuario:\n> ')
        if username == usuario:
            password = input('Ingresa tu contraseña:\n> ')
            if password == contrasena:
                break
            else:
                intentos = intentos - 1
                if intentos != 1:
                    print(f'\nContraseña incorrecta, ¡{intentos} intentos restantes!\n')
                else:
                    print(f'\nContraseña incorrecta, ¡{intentos} intento restante!\n')
        else:
            intentos = intentos - 1
            if intentos != 1:
                print(f'\nUsuario incorrecto, ¡{intentos} intentos restantes!\n')
            else:
                print(f'\nUsuario incorrecto, ¡{intentos} intento restante!\n')
    
    print(f'\n\n¡Bienvenido a LifeStore, {usuario}!\n\n')

if __name__ == "__main__":
    login()