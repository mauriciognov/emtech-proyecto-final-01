# ARCHIVO DE FUNCIONES EXPORTADAS AL ARCHIVO DEL CÓDIGO FUENTE

# Función para seleccionar mes para el análisis
def elegir_mes():
    opcion_mes = input('\nMes a analizar (FORMATO: /mm/):\n > ')
    return opcion_mes

# Función para copiar una lista
def copiar_lista(lista):
    copia_lista = lista
    return copia_lista

# Función para crear la lista de ventas del mes seleccionado: ventas_mes = [id_sale, id_product, score, date, refund]
def ventas_mes(lista_ventas, mes):
    lista_ventas_mes = []

    for venta in lista_ventas:
        fecha_venta = venta[3]
        if mes in fecha_venta:
            lista_ventas_mes.append(venta)
    return lista_ventas_mes

# Función para crear la lista de ventas al mes/año contabilizadas: conteo_ventas = [id_prod, núm. de ventas, score_prom]
def contar_ventas(lista_ventas):
    conteo_ventas = []
    renglon = [0, 0, 0]
    suma = 0
    cont_ren = 0
    cont_venta = 0

    for venta in lista_ventas:
        id_prod = venta[1]
        score = venta[2]
        if renglon[0] == 0:
            cont_venta = cont_venta + 1
            suma = suma + score
            score_prom = suma/cont_venta
            renglon = [id_prod, cont_venta, score_prom]
            conteo_ventas.append(renglon)
            cont_ren = cont_ren + 1
        elif conteo_ventas[cont_ren - 1][0] == id_prod:
            cont_venta = cont_venta + 1
            suma = suma + score
            score_prom = suma/cont_venta
            conteo_ventas[cont_ren - 1][1] = cont_venta
            conteo_ventas[cont_ren - 1][2] = score_prom
        elif conteo_ventas[cont_ren - 1][0] != id_prod:
            cont_venta = 1
            suma = score
            score_prom = suma/cont_venta
            renglon = [id_prod, cont_venta, score_prom]
            conteo_ventas.append(renglon)
            cont_ren = cont_ren + 1
    return conteo_ventas

# Función para crear la lista de los 5 productos con mayores ventas al mes: mayor_ventas = [id_prod, núm. de ventas]
def mayor5_ventas(lista_ventas):
    lista_temporal = lista_ventas
    mayor_ventas = []
    i = 0
    indice = 0
    if len(lista_temporal) <= 5:
        mayor_ventas = lista_temporal
    else:
        while i < 5:    
            cont = 0
            mayor = [0,0]
            if indice == 0:   
                for elemento in lista_temporal:
                    if mayor[1] == 0 and elemento[1] > mayor[1]:
                        mayor = elemento
                        indice = cont
                    elif mayor[1] != 0 and elemento[1] > mayor[1]:
                        mayor = elemento
                        cont = cont + 1
                        indice = cont
                    elif mayor[1] != 0 and elemento[1] < mayor[1]:
                        cont = cont + 1
                    elif mayor[1] != 0 and elemento[1] == mayor[1]:
                        cont = cont + 1
                mayor_ventas.append(mayor)
                del lista_temporal[indice]
            elif indice != 0:
                for elemento in lista_temporal:
                    if mayor[1] == 0 and elemento[1] > mayor[1]:
                        mayor = elemento
                        indice = cont
                    elif mayor[1] != 0 and elemento[1] > mayor[1]:
                        mayor = elemento
                        cont = cont + 1
                        indice = cont
                    elif mayor[1] != 0 and elemento[1] < mayor[1]:
                        cont = cont + 1
                    elif mayor[1] != 0 and elemento[1] == mayor[1]:
                        cont = cont + 1
                mayor_ventas.append(mayor)
                del lista_temporal[indice]
            i = i + 1
    return mayor_ventas

# Función para crear la lista de los 5 productos con menores ventas al mes: menor_ventas = [id_prod, núm. de ventas]
def menor5_ventas(lista_ventas):
    lista_temporal = lista_ventas
    menor_ventas = []
    i = 0
    indice = 0
    if len(lista_temporal) <= 5:
        menor_ventas = lista_temporal
    else:
        while i < 5:    
            cont = 0
            menor = [0,0]
            if indice == 0:   
                for elemento in lista_temporal:
                    if menor[1] == 0 and elemento[1] > menor[1]:
                        menor = elemento
                        indice = cont
                    elif menor[1] != 0 and elemento[1] < menor[1]:
                        menor = elemento
                        cont = cont + 1
                        indice = cont
                    elif menor[1] != 0 and elemento[1] > menor[1]:
                        cont = cont + 1
                    elif menor[1] != 0 and elemento[1] == menor[1]:
                        cont = cont + 1
                menor_ventas.append(menor)
                del lista_temporal[indice]
            elif indice != 0:
                for elemento in lista_temporal:
                    if menor[1] == 0 and elemento[1] > menor[1]:
                        menor = elemento
                        indice = cont
                    elif menor[1] != 0 and elemento[1] < menor[1]:
                        menor = elemento
                        cont = cont + 1
                        indice = cont
                    elif menor[1] != 0 and elemento[1] > menor[1]:
                        cont = cont + 1
                    elif menor[1] != 0 and elemento[1] == menor[1]:
                        cont = cont + 1
                menor_ventas.append(menor)
                del lista_temporal[indice]
            i = i + 1
    return menor_ventas

# Función para crear la lista de los 5 productos con mejores reseñas al mes: mayor_score = [id_prod, score_prom]
def mayor5_score(lista_ventas):
    lista_temporal = lista_ventas
    mayor_score = []
    i = 0
    indice = 0
    if len(lista_temporal) <= 5:
        mayor_score = lista_temporal
    else:
        while i < 5:    
            cont = 0
            mayor = [0,0]
            if indice == 0:   
                for elemento in lista_temporal:
                    if mayor[1] == 0 and elemento[2] > mayor[1]:
                        mayor[0] = elemento[0]
                        mayor[1] = elemento[2]
                        indice = cont
                    elif mayor[1] != 0 and elemento[2] > mayor[1]:
                        mayor[0] = elemento[0]
                        mayor[1] = elemento[2]
                        cont = cont + 1
                        indice = cont
                    elif mayor[1] != 0 and elemento[2] < mayor[1]:
                        cont = cont + 1
                    elif mayor[1] != 0 and elemento[2] == mayor[1]:
                        cont = cont + 1
                mayor_score.append(mayor)
                del lista_temporal[indice]
            elif indice != 0:
                for elemento in lista_temporal:
                    if mayor[1] == 0 and elemento[2] > mayor[1]:
                        mayor[0] = elemento[0]
                        mayor[1] = elemento[2]
                        indice = cont
                    elif mayor[1] != 0 and elemento[2] > mayor[1]:
                        mayor[0] = elemento[0]
                        mayor[1] = elemento[2]
                        cont = cont + 1
                        indice = cont
                    elif mayor[1] != 0 and elemento[2] < mayor[1]:
                        cont = cont + 1
                    elif mayor[1] != 0 and elemento[2] == mayor[1]:
                        cont = cont + 1
                mayor_score.append(mayor)
                del lista_temporal[indice]
            i = i + 1
    return mayor_score

# Función para crear la lista de los 5 productos con peores reseñas al mes: menor_score = [id_prod, score_prom]
def menor5_score(lista_ventas):
    lista_temporal = lista_ventas
    menor_score = []
    i = 0
    indice = 0
    if len(lista_temporal) <= 5:
        menor_score = lista_temporal
    else:
        while i < 5:    
            cont = 0
            menor = [0,0]
            if indice == 0:   
                for elemento in lista_temporal:
                    if menor[1] == 0 and elemento[2] > menor[1]:
                        menor[0] = elemento[0]
                        menor[1] = elemento[2]
                        indice = cont
                    elif menor[1] != 0 and elemento[2] < menor[1]:
                        menor[0] = elemento[0]
                        menor[1] = elemento[2]
                        cont = cont + 1
                        indice = cont
                    elif menor[1] != 0 and elemento[2] > menor[1]:
                        cont = cont + 1
                    elif menor[1] != 0 and elemento[2] == menor[1]:
                        cont = cont + 1
                menor_score.append(menor)
                del lista_temporal[indice]
            elif indice != 0:
                for elemento in lista_temporal:
                    if menor[1] == 0 and elemento[2] > menor[1]:
                        menor[0] = elemento[0]
                        menor[1] = elemento[2]
                        indice = cont
                    elif menor[1] != 0 and elemento[2] < menor[1]:
                        menor[0] = elemento[0]
                        menor[1] = elemento[2]
                        cont = cont + 1
                        indice = cont
                    elif menor[1] != 0 and elemento[2] > menor[1]:
                        cont = cont + 1
                    elif menor[1] != 0 and elemento[2] == menor[1]:
                        cont = cont + 1
                menor_score.append(menor)
                del lista_temporal[indice]
            i = i + 1
    return menor_score

# Función para crear la lista de ventas por categoría: categoria_ventas_mes = [id_categoria, categoria, núm. de ventas]
def categoria_ventas(lista_ventas):
    categoria_ventas = [[1, 'Procesadores', 0], [2, 'Tarjetas de video', 0], [3, 'Tarjetas madre', 0], [4, 'Discos duros', 0], [5, 'Memorias usb', 0], [6, 'Pantallas', 0], [7, 'Bocinas', 0], [8, 'Audifonos', 0]]

    for elemento in lista_ventas:
        id_prod = elemento[0]
        ventas = elemento[1]
        if id_prod >= 1 and id_prod <= 9:
            categoria = 1 # procesadores
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas
        elif id_prod >= 10 and id_prod <= 28:
            categoria = 2 # tarjetas de video
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas
        elif id_prod >= 29 and id_prod <= 46:
            categoria = 3 # tarjetas madre
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas
        elif id_prod >= 47 and id_prod <= 59:
            categoria = 4 # discos duros
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas
        elif id_prod >= 60 and id_prod <= 61:
            categoria = 5 # memorias usb
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas
        elif id_prod >= 62 and id_prod <= 73:
            categoria = 6 # pantallas
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas
        elif id_prod >= 74 and id_prod <= 83:
            categoria = 7 # bocinas
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas
        elif id_prod >= 84 and id_prod <= 96:
            categoria = 8 # audifonos
            indice = categoria - 1
            if categoria_ventas[indice][2] == 0:
                categoria_ventas[indice][2] = ventas
            else:
                categoria_ventas[indice][2] = categoria_ventas[indice][2] + ventas  
    return categoria_ventas

# Función para imprimir en consola lista de los 5 productos con mayores ventas del mes
def imprimir_mayor_ventas(lista_ventas, lista_productos, mes):
    if lista_ventas == []:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON MAYORES VENTAS DEL MES {mes} <-\n')
        print('No hubo ventas en este mes.')
    else:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON MAYORES VENTAS DEL MES {mes} <-\n')
        cont = 1

        for elemento in lista_ventas:
            id_prod = elemento[0]
            num_ventas = elemento[1]
            for producto in lista_productos:
                nombre_producto = producto[1]
                if id_prod == producto[0]:
                    print(f'{cont}.-PRODUCTO: {nombre_producto}\n   NÚM. DE VENTAS: {num_ventas}')
                else:
                    continue
            cont = cont + 1

# Función para imprimir en consola lista de los 5 productos con menores ventas del mes
def imprimir_menor_ventas(lista_ventas, lista_productos, mes):
    if lista_ventas == []:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON MENORES VENTAS DEL MES {mes} <-\n')
        print('No hubo ventas en este mes.')
    else:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON MENORES VENTAS DEL MES {mes} <-\n')
        cont = 1

        for elemento in lista_ventas:
            id_prod = elemento[0]
            num_ventas = elemento[1]
            for producto in lista_productos:
                nombre_producto = producto[1]
                if id_prod == producto[0]:
                    print(f'{cont}.-PRODUCTO: {nombre_producto}\n   NÚM. DE VENTAS: {num_ventas}')
                else:
                    continue
            cont = cont + 1

# Función para imprimir en consola lista de los 5 productos con mejores reseñas del mes
def imprimir_mayor_score(lista_score, lista_productos, mes):
    if lista_score == []:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON MEJORES RESEÑAS DEL MES {mes} <-\n')
        print('No hubo ventas en este mes.')
    else:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON MEJORES RESEÑAS DEL MES {mes} <-\n')
        cont = 1

        for elemento in lista_score:
            id_prod = elemento[0]
            score_producto = elemento[1]
            for producto in lista_productos:
                nombre_producto = producto[1]
                if id_prod == producto[0]:
                    print(f'{cont}.-PRODUCTO: {nombre_producto}\n   RESEÑA PROMEDIO: {score_producto}')
                else:
                    continue
            cont = cont + 1

# Función para imprimir en consola lista de los 5 productos con peores reseñas del mes
def imprimir_menor_score(lista_score, lista_productos, mes):
    if lista_score == []:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON PEORES RESEÑAS DEL MES {mes} <-\n')
        print('No hubo ventas en este mes.')
    else:
        print(f'\n-> LISTA DE LOS 5 PRODUCTOS CON PEORES RESEÑAS DEL MES {mes} <-\n')
        cont = 1

        for elemento in lista_score:
            id_prod = elemento[0]
            score_producto = elemento[1]
            for producto in lista_productos:
                nombre_producto = producto[1]
                if id_prod == producto[0]:
                    print(f'{cont}.-PRODUCTO: {nombre_producto}\n   RESEÑA PROMEDIO: {score_producto}')
                else:
                    continue
            cont = cont + 1

# Función para imprimir en consola las ventas por categoría del mes
def imprimir_categoria_ventas(lista_categoria, mes):
    print(f'\n-> VENTAS POR CATEGORÍA DEL MES {mes} <-\n')
    for elemento in lista_categoria:
        id_categoria = elemento[0]
        nombre_categoria = elemento[1]
        ventas_categoria = elemento[2]
        print(f'{id_categoria}.-{nombre_categoria}: {ventas_categoria}')

# Función para crear la lista de busquedas anuales contabilizadas: busquedas = [id_prod, núm. de búsquedas]
def busquedas(lista_busquedas):
    busquedas = []
    renglon = [0, 0]
    cont1 = 0
    cont2 = 0

    for busqueda in lista_busquedas:
        id_prod = busqueda[1]
        if renglon[0] == 0:
            cont2 = cont2 + 1
            renglon = [id_prod, cont2]
            busquedas.append(renglon)
        elif busquedas[cont1][0] == id_prod:
            cont2 = cont2 + 1
            busquedas[cont1][1] = cont2 
        elif busquedas[cont1][0] != id_prod:
            cont2 = 1
            renglon = [id_prod, cont2]
            busquedas.append(renglon)
            cont1 = cont1 + 1
    return busquedas

# Función para crear la lista con los 10 productos con mayores búsquedas: mayor_busquedas = [id_prod, núm. de búsquedas]
def mayor_busquedas(busquedas):
    mayor_busquedas = []
    i = 0
    indice = 0

    while i < 10:    
        cont = 0
        mayor = [0,0]
        if indice == 0:   
            for elemento in busquedas:
                if mayor[1] == 0 and elemento[1] > mayor[1]:
                    mayor = elemento
                    indice = cont
                elif mayor[1] != 0 and elemento[1] > mayor[1]:
                    mayor = elemento
                    cont = cont + 1
                    indice = cont
                elif mayor[1] != 0 and elemento[1] < mayor[1]:
                    cont = cont + 1
                elif mayor[1] != 0 and elemento[1] == mayor[1]:
                    cont = cont + 1
            mayor_busquedas.append(mayor)
            del busquedas[indice]
        elif indice != 0:
            for elemento in busquedas:
                if mayor[1] == 0 and elemento[1] > mayor[1]:
                    mayor = elemento
                    indice = cont
                elif mayor[1] != 0 and elemento[1] > mayor[1]:
                    mayor = elemento
                    cont = cont + 1
                    indice = cont
                elif mayor[1] != 0 and elemento[1] < mayor[1]:
                    cont = cont + 1
                elif mayor[1] != 0 and elemento[1] == mayor[1]:
                    cont = cont + 1
            mayor_busquedas.append(mayor)
            del busquedas[indice]
        i = i + 1
    return mayor_busquedas

# Función para crear la lista con los 10 productos con menores búsquedas: menor_busquedas = [id_prod, núm. de búsquedas]
def menor_busquedas(busquedas):
    menor_busquedas = []
    i = 0
    indice = 0

    while i < 10:    
        cont = 0
        menor = [0,0]
        if indice == 0:   
            for elemento in busquedas:
                if menor[1] == 0 and elemento[1] > menor[1]:
                    menor = elemento
                    indice = cont
                elif menor[1] != 0 and elemento[1] < menor[1]:
                    menor = elemento
                    cont = cont + 1
                    indice = cont
                elif menor[1] != 0 and elemento[1] > menor[1]:
                    cont = cont + 1
                elif menor[1] != 0 and elemento[1] == menor[1]:
                    cont = cont + 1
            menor_busquedas.append(menor)
            del busquedas[indice]
        elif indice != 0:
            for elemento in busquedas:
                if menor[1] == 0 and elemento[1] > menor[1]:
                    menor = elemento
                    indice = cont
                elif menor[1] != 0 and elemento[1] < menor[1]:
                    menor = elemento
                    cont = cont + 1
                    indice = cont
                elif menor[1] != 0 and elemento[1] > menor[1]:
                    cont = cont + 1
                elif menor[1] != 0 and elemento[1] == menor[1]:
                    cont = cont + 1
            menor_busquedas.append(menor)
            del busquedas[indice]
        i = i + 1
    return menor_busquedas

# Función para imprimir en consola lista de los 10 productos con mayores búsquedas
def imprimir_mayor_busquedas(lista_busquedas, lista_productos):
    if lista_busquedas == []:
        print(f'\n-> LISTA DE LOS 10 PRODUCTOS CON MAYORES BÚSQUEDAS DEL AÑO <-\n')
        print('La lista está vacía.')
    else:
        print(f'\n-> LISTA DE LOS 10 PRODUCTOS CON MAYORES BÚSQUEDAS DEL AÑO <-\n')
        cont = 1

        for elemento in lista_busquedas:
            id_prod = elemento[0]
            num_busquedas = elemento[1]
            for producto in lista_productos:
                nombre_producto = producto[1]
                if id_prod == producto[0]:
                    print(f'{cont}.-PRODUCTO: {nombre_producto}\n   NÚM. DE BÚSQUEDAS: {num_busquedas}')
                else:
                    continue
            cont = cont + 1

# Función para imprimir en consola lista de los 10 productos con menores búsquedas
def imprimir_menor_busquedas(lista_busquedas, lista_productos):
    if lista_busquedas == []:
        print(f'\n-> LISTA DE LOS 10 PRODUCTOS CON MENORES BÚSQUEDAS DEL AÑO <-\n')
        print('La lista está vacía.')
    else:
        print(f'\n-> LISTA DE LOS 10 PRODUCTOS CON MENORES BÚSQUEDAS DEL AÑO <-\n')
        cont = 1

        for elemento in lista_busquedas:
            id_prod = elemento[0]
            num_busquedas = elemento[1]
            for producto in lista_productos:
                nombre_producto = producto[1]
                if id_prod == producto[0]:
                    print(f'{cont}.-PRODUCTO: {nombre_producto}\n   NÚM. DE BÚSQUEDAS: {num_busquedas}')
                else:
                    continue
            cont = cont + 1

# Función para crear la lista del total de ingresos: total_ingresos = [id_prod, num_ventas, ganancia_prod]
def ganancias_total(lista_ventas, lista_productos):
    total_ingresos = []

    for elemento in lista_ventas:
        id_prod = elemento[0]
        num_ventas = elemento[1]
        for producto in lista_productos:
            precio_prod = producto[2]
            if id_prod == producto[0]:
                ganancia_prod = num_ventas * precio_prod
                renglon = [id_prod, num_ventas, ganancia_prod]
            else:
                continue
        total_ingresos.append(renglon)
    return total_ingresos

# Función para imprimir en consola el total de ingresos por mes, ganancia por producto y núm. ventas al mes
def imprimir_ingresos_mes(lista_ingresos, lista_productos, mes):
    if lista_ingresos == []:
        print(f'\n-> EN EL MES {mes}:\n')
        print('No hubo ventas.')
    else:
        cont = 1
        ganancia_total = 0
        num_ventas_total = 0
        print('\n')
        
        for elemento in lista_ingresos:
            id_prod = elemento[0]
            num_ventas = elemento[1]
            ganancia_prod = elemento[2]
            for producto in lista_productos:
                if id_prod == producto[0]:
                    nombre_prod = producto[1]
                    print(f'{cont}.-PRODUCTO: {nombre_prod}\n   NÚM. DE VENTAS: {num_ventas}\n   GANANCIA: ${ganancia_prod}')
                else:
                    continue
            cont = cont + 1
            ganancia_total = ganancia_total + ganancia_prod
            num_ventas_total = num_ventas_total + num_ventas
        print(f'\n-> EN EL MES {mes}:\nNÚM. DE VENTAS TOTALES: {num_ventas_total}\nINGRESO TOTAL: ${ganancia_total}')

# Función para imprimir en consola el total de ingresos al año
def imprimir_ingresos_anual(lista_ingresos, lista_productos):
    if lista_ingresos == []:
        print('No hubo ventas en el año.')
    else:
        cont = 1
        ganancia_total = 0
        num_ventas_total = 0

        for elemento in lista_ingresos:
            id_prod = elemento[0]
            num_ventas = elemento[1]
            ganancia_prod = elemento[2]
            for producto in lista_productos:
                if id_prod == producto[0]:
                    nombre_prod = producto[1]
                    print(f'{cont}.-PRODUCTO: {nombre_prod}\n   NÚM. DE VENTAS: {num_ventas}\n   GANANCIA: ${ganancia_prod}')
                else:
                    continue
            cont = cont + 1
            ganancia_total = ganancia_total + ganancia_prod
            num_ventas_total = num_ventas_total + num_ventas
        print(f'\n-> EN EL AÑO:\nNÚM. DE VENTAS TOTALES: {num_ventas_total}\nINGRESO TOTAL: ${ganancia_total}')

# Función para crear la lista de ventas contabilizadas por cada mes al año: conteo_ventas = [id_mes, nombre_mes, núm. de ventas]
def meses_ventas(lista_meses, lista_ventas):

    for venta in lista_ventas:
        fecha_venta = venta[3]
        for mes in lista_meses:
            if mes[0] in fecha_venta:
                mes[1] = mes[1] + 1
            else:
                continue
    return lista_meses

# Función para imprimir en consola las ventas en cada mes del año
def imprimir_ventas_por_mes(resultado_meses):
    print('\nLAS VENTAS EN CADA MES SON:\n')
    for elemento in resultado_meses:
        mes = elemento[0]
        ventas = elemento[1]
        print(f'MES: {mes}\nVENTAS: {ventas}\n')
