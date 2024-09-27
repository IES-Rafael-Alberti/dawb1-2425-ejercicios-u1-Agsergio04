importe_producto =float(input("Introduce el precio de un producto sin iva: "))

importe_con_iva = importe_producto * 1.10
importe_producto = str(importe_producto)
importe_con_iva = str(importe_con_iva)

print("El importe de iva aplicado es " + importe_con_iva + " y el importe sin iva es de: " + importe_producto)

