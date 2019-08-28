def imprimir_factura(productos_totales,productos_a_comprar):
    """recibe una lista de productos totales, una lista de productos productos_a_comprar,
    y se imprime una factura que contiene la cantidad, la descripción, el precio
    unitario y el precio total de cada producto comprado y el total general"""

    productos_comprados = [[cantidad, descripcion, precio] for codigo, descripcion, precio in productos_totales
    for codigo_compra, cantidad in productos_a_comprar
    if codigo_compra == codigo]
    
    precios_subtotales = [cantidad*precio for cantidad, descripcion, precio in productos_comprados]

    [productos_comprados[i].append(precios_subtotales[i]) for i in range(len(productos_comprados))]

    [print(f'cantidad: {producto[0]}, {producto[1]}, precio unitario: {producto[2]}, subtotal: {producto[3]}') for producto in productos_comprados]
    print(f'TOTAL A ABONAR: {sum([producto[3] for producto in productos_comprados])}')
    
productos_totales = [
    (1,'banana',50),(2,'tomate',60),(3,'arroz',30),
    (4,'fideos',40),(5,'churrasco',190),(6,'manzana',60)
    ]
productos_a_comprar = [(4,5),(1,3),(2,4),(6,1)]

imprimir_factura(productos_totales,productos_a_comprar)