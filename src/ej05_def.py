def calculo_iva_porcentaje_dado(importe_producto,importe_solicitado):
    resultado = importe_producto + importe_producto * (importe_solicitado/100)
    
    print(f"El importe de iva aplicado es {resultado:.2f} y el importe sin iva es de {importe_producto:.2f}")

def main():
    importe_producto =float(input("Introduce el precio de un producto sin iva: "))
    importe_solicitado = float(input("De cuanto va a ser el iva a aplicar al producto(escribalo sin el porcentaje): "))
    calculo_iva_porcentaje_dado(importe_producto,importe_solicitado)

if __name__ == "__main__":
    main()