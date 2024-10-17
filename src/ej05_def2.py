def calculo_iva_porcentaje_dado(importe: float, iva: float) -> str:
    if iva < 0 or iva > 100:
        iva = 21
        
    return f"El importe sin iva es de {importe:.2f} y el importe de iva aplicado es {importe + importe * (iva/100):.2f}"

def main():
    importe =float(input("Introduce el precio de un producto sin iva: "))
    iva = float(input("De cuanto va a ser el iva a aplicar al producto(escribalo sin el porcentaje): "))
    print(calculo_iva_porcentaje_dado(importe,iva))

if __name__ == "__main__":
    main()
