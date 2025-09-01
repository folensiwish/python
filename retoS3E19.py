#Sistema de reserva de hoteles
# Crea un sistema de reserva de hoteles que contenga la siguiente información
# de una reseva:

# Nombre del huésped
# Dias de estadía
# Tarifa diaria
# Indicar si el cuarto tiene vista al mar

#Despues mandar a imprimir los valores de cada variable 

cliente = input("Ingrese el nombre del cliente: ")
dias_estadia = int(input("Ingrese los dias de estadia:"))
tarifa_diaria = float(input("ingrese la tarifa diaria: "))
vista_mar = input("El cuarto tiene vista al mar?, (si/no): ")

def reserva_hotel(cliente, dias_estadia, tarifa_diaria, vista_mar):
    vista_mar = vista_mar.lower()
    if vista_mar == "si" or vista_mar == "sí":
        vista_mar = True
    else:
        vista_mar = False
    print("*** Sistema de reserva de hoteles ***\nCliente:", cliente, "\nDias de estadia:", dias_estadia, "\nTarifa diaria:", tarifa_diaria, "\nVista al mar:", vista_mar)
reserva_hotel(cliente, dias_estadia , tarifa_diaria,vista_mar)

