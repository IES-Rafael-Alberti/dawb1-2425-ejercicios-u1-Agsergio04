def introducir_numero(msg):
    resultado = None
    condicion = False

    entrada = input(msg).strip().lower()
   
    if comprobar_numero(entrada):
       resultado =  int(entrada)
    else:
        if entrada.lower() == "fin":
            condicion == True
    return condicion,resultado


def comprobar_numero(numero):
    if numero.startswith("-"):
        numero = numero[1:]
        
    return  numero.isdigit()


def main():
    cont = 0
    suma = 0
    media = 0
    
    salir = True
    
    while salir:
        entrada_correcta,numero = introducir_numero("Introduzca un numero")
        
        if entrada_correcta and numero is not None:
            cont += 1
            suma += numero
        elif entrada_correcta and numero is None:
            salir = False
        else:
            print("Entrada Invalidad")

    if cont > 0:
        media = suma / cont
    print(f" suma {suma}, cont {cont}, media {media}")
            
        
if __name__ == "__main__":
    main()