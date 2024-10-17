precio_producto = float(input("Introduce el precio de un producto con sus centimos: "))


euros_producto = int(precio_producto)
centimos_producto = precio_producto - euros_producto

print("Los euros del producto son ",euros_producto," y los centimos son ",centimos_producto.__round__(2))