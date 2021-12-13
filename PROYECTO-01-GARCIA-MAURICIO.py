import login, menu, funciones
from listas import ventas_validas, lista_meses
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

# se importan las funciones para el login y el menú principal
login.login()
menu.menu()
string_menu = menu.opcion_menu()
respuesta_menu = int(string_menu)

while True:
    if respuesta_menu == 1:
        # se pide al usuario el mes a analizar y se almacenan las ventas contabilizadas del mes (sin devolución) en una lista mediante funciones
        mes = funciones.elegir_mes()
        ventas_mes = funciones.ventas_mes(ventas_validas, mes)
        conteo_ventas_mes = funciones.contar_ventas(ventas_mes)    
        # se copia la lista conteo_ventas_mes con la función para generar las demás listas
        copia1_conteo_ventas_mes = funciones.contar_ventas(ventas_mes)
        copia2_conteo_ventas_mes = funciones.contar_ventas(ventas_mes)
        # se crea la lista de los 5 productos con mayores ventas al mes mediante funciones
        mayor_ventas_mes = funciones.mayor5_ventas(conteo_ventas_mes)
        # se crea la lista de los 5 productos con menores ventas al mes mediante funciones
        menor_ventas_mes = funciones.menor5_ventas(copia1_conteo_ventas_mes)
        # se crea la lista de las ventas por categoría al mes
        categoria_ventas_mes = funciones.categoria_ventas(copia2_conteo_ventas_mes)
        # se imprimen los resultados mediante funciones
        funciones.imprimir_mayor_ventas(mayor_ventas_mes, lifestore_products, mes)
        funciones.imprimir_menor_ventas(menor_ventas_mes, lifestore_products, mes)
        funciones.imprimir_categoria_ventas(categoria_ventas_mes, mes)

    elif respuesta_menu == 2:
    # se pide al usuario el mes a analizar y se almacenan las ventas/scores del mes en una lista mediante funciones 
        mes = funciones.elegir_mes()
        ventas_mes = funciones.ventas_mes(lifestore_sales, mes)
        conteo_ventas_mes = funciones.contar_ventas(ventas_mes)
        # se copia la lista conteo_ventas_mes con la función para generar otra lista
        conteo_ventas_mes2 = funciones.contar_ventas(ventas_mes)
        # se crea la lista con los 5 productos con mejores y peores reseñas por mes mediante funciones
        mayor_score_mes = funciones.mayor5_score(conteo_ventas_mes)
        menor_score_mes = funciones.menor5_score(conteo_ventas_mes2)
        # se imprimen los resultados mediante funciones
        funciones.imprimir_mayor_score(mayor_score_mes, lifestore_products, mes)
        funciones.imprimir_menor_score(menor_score_mes, lifestore_products, mes)

    elif respuesta_menu == 3:
        # se almacenan las búsquedas contabilizadas anualmente mediante funciones
        busquedas1 = funciones.busquedas(lifestore_searches)
        busquedas2 = funciones.busquedas(lifestore_searches)
        # se crean las listas con mayores y menores búsquedas mediante funciones
        mayor_busquedas = funciones.mayor_busquedas(busquedas1)
        menor_busquedas = funciones.menor_busquedas(busquedas2)
        # se imprimen en consola las listas de mayores y menores búsquedas mediante funciones
        funciones.imprimir_mayor_busquedas(mayor_busquedas, lifestore_products)
        funciones.imprimir_menor_busquedas(menor_busquedas, lifestore_products)  

    elif respuesta_menu == 4:
        # se pide al usuario el mes a analizar y se almacenan las ventas del mes (sin devolución) en una lista mediante funciones
        mes = funciones.elegir_mes()
        ventas_mes = funciones.ventas_mes(ventas_validas, mes)
        # se contabilizan las ventas de cada producto al mes en una nueva lista
        conteo_ventas_mes = funciones.contar_ventas(ventas_mes)
        # se crea la lista de ingresos totales al mes mediante funciones
        total_ingresos_mes = funciones.ganancias_total(conteo_ventas_mes, lifestore_products)
        # se imprime en consola los ingresos y ventas totales del mes mediante funciones
        funciones.imprimir_ingresos_mes(total_ingresos_mes, lifestore_products, mes)

    elif respuesta_menu == 5:
        # se asignan las ventas validas del año a la lista ventas_validas_anual
        ventas_validas_anual = ventas_validas
        # se crea la lista de las ventas del año contabilizadas mediante funciones
        conteo_ventas_anual = funciones.contar_ventas(ventas_validas_anual)
        # se crea la lista de ingresos totales del año mediante funciones
        total_ingresos_anual = funciones.ganancias_total(conteo_ventas_anual, lifestore_products)
        # se imprime en consola los ingresos y ventas totales del año mediante funciones
        funciones.imprimir_ingresos_anual(total_ingresos_anual, lifestore_products)
        # se crea la lista de las ventas en cada mes del año mediante funciones
        resultado_meses = funciones.meses_ventas(lista_meses, ventas_validas_anual)
        # se imprime en consola las ventas por cada mes mediante funciones
        funciones.imprimir_ventas_por_mes(resultado_meses)
        
    
    elif respuesta_menu == 6:
        # se termina el programa
        print('\nHas salido del sistema. ¡Hasta luego!')
        exit()
    
    menu.menu()
    string_menu = menu.opcion_menu()
    respuesta_menu = int(string_menu)