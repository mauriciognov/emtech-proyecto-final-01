
# SE CREA EL MENÚ PARA PREGUNTAR AL USUARIO QUE QUIERE HACER

def menu():
    menu = """\nACCIONES PARA ANALIZAR LOS DATOS DE LA TIENDA LIFESTORE:
    
    1.- Obtener productos con mayores y menores ventas al mes.
    2.- Obtener productos con mejores y peores reseñas al mes.
    3.- Obtener productos con mayores y menores busquedas al año.
    4.- Obtener el total de ingresos y número de ventas al mes.
    5.- Obtener el total de ingresos y meses con más ventas al año. 
    6.- Salir.
    """
    print(menu)

def opcion_menu():
    respuesta = input('Selecciona una opción del menú:\n > ')
    return respuesta

if __name__ == "__main__":
    menu()
    opcion_menu()