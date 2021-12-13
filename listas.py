"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

# Se crea la lista ventas_validas (ventas sin devolución)
ventas_validas = []

for sale in lifestore_sales:
    refund = sale[4]
    if refund == 1:
        continue
    else:
        ventas_validas.append(sale)

lista_meses = [['/01/', 0], ['/02/', 0], ['/03/', 0], ['/04/', 0], ['/05/', 0], ['/06/', 0], ['/07/', 0], ['/08/', 0], ['/09/', 0], ['/10/', 0], ['/11/', 0], ['/12/', 0]]