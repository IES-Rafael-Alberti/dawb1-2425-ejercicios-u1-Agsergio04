def main():
    bandera = True
    
    while(bandera):
        primer_numero = int(input("Introduce un numero entero: "))
        segundo_numero = int(input("Introduce otro numero entero: "))
        if(primer_numero == segundo_numero):
            print("Error : Los números no pueden ser iguales")
        elif(primer_numero > segundo_numero):
            print(f"El número menor es el {segundo_numero} y entre ellos existen {primer_numero - segundo_numero} números enteros.")
            bandera = False
        else:
            print(f"El número menor es el {primer_numero} y entre ellos existen {segundo_numero - primer_numero} números enteros.")
            bandera = False
            
if __name__ == "__main__":
    main()