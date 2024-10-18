nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = float(input("Introduce el precio del producto: "))
cantidad_producto = int(input("Introduce la cantidad de productos que posees: "))

coste_total = precio_producto * cantidad_producto

print(f"{nombre_producto} {precio_producto:6.2f} {cantidad_producto:3d} {coste_total:08.2f}")