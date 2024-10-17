def comprobar_entero(cadena):
    cadena = cadena.strip() 
    return (cadena.isdigit()) or (cadena.startswith("-") and cadena[1:].isdigit())


def dame_numero():
    """
    Mi codigo:
    
    numero = 0
    condicion = True
    
    while(condicion):
        cadena = input("Escribe un numero entero : ").strip()
        comprobar =  comprobar_entero(cadena)
        if comprobar == True:
            numero = cadena
            condicion = False
            
    return numero
    """
    #Forma del Profesor:
    cadena = input("Escribe un numero entero : ")
    while not comprobar_entero(cadena):
        cadena = input("**ERROR** Eso no es un entero!!!\n\nEscribe un numero entero otra vez : ")
    return int(cadena)


def main():
    num = dame_numero()
    print(f"Has introducido el numero {num}")
    
    
if __name__  == "__main__":
    main()