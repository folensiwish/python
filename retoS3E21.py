'''
Sistema tienda online
Crear el detalle de un producto de una tienda online

El detalle del producto debe tener:

Nombre del producto
Precio del producto
Cantidad en el inventario  
Indicar si esta disponible

'''

nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cant_inventario = int(input("Ingrese la cantidad en inventario: "))
stock = input("El producto esta disponible? (si/no): ")
'''
print("*** Sistema de Tienda Online ***\nProducto:", nombre_producto, "\nPrecio: $ ", precio_producto,
       "\nCantidad inventario:", cant_inventario, "\nDisponible:", stock)
'''

def detalle_producto(nombre_producto, precio_producto, cant_inventario, stock):
    stock = stock.lower()
    if stock == "si" or stock == "sí":
        stock= True
    else:
        stock = False
    print(" *** Sistema de Tienda Online***\nProducto:", nombre_producto, "\nPrecio: $ ", precio_producto,
       "\nCantidad inventario:", cant_inventario, "\nDisponible:", stock)
detalle_producto(nombre_producto,precio_producto, cant_inventario, stock)