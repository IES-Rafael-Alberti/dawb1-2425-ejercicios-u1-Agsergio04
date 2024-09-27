importe_producto =float(input("Introduce el precio de un producto sin iva: "))
importe_solicitado = float(input("De cuanto va a ser el iva a aplicar al producto(escribalo sin el porcentaje): "))

importe_con_iva = importe_producto + importe_producto * (importe_solicitado/100)
importe_producto = str(importe_producto)
importe_con_iva = str(importe_con_iva)

print("El importe de iva aplicado es " + importe_con_iva + " y el importe sin iva es de: " + importe_producto)

