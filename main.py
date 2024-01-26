from paquete.modulo1 import Cliente
from paquete.modulo2 import *

# Creamos al objeto cliente con los siguientes argumentos    
cliente = Cliente("Benjamin", "Lazarte", 24, "benja@gmail.com", "San nicolas 3557")
#print(cliente)

# Agregar compras al carrito
cliente.agregar_carrito("Lavarropas", "Fravega")
cliente.agregar_carrito("Camisa", "Velo Santo")

# Ver productos agregados al carrito
cliente.ver_carrito()

# Comprar los productos del carrito
cliente.comprar()

# funcion de adios
cliente.exit()




    