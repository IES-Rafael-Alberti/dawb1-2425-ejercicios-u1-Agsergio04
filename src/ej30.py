def comprobacion_menor_cero(comprobacion):
    bandera = True
    
    while bandera:
        if comprobacion < 0:
            repetir_valor = int(input("Vuelve a introducir el valor porque este no puede ser menor a 0: "))
            if repetir_valor > 0:
                comprobacion = repetir_valor
                bandera = False
        else:
            bandera = False
                
    return comprobacion 

def crear_serie(numero_inicio, incremento, total_serie):
    inicio_serie = "SERIE =>"
    serie_trozo = ""
    
    numero_actual = numero_inicio  

    for i in range(total_serie):
        if i == 0:
            serie_trozo += str(int(numero_actual))  
        elif i == total_serie - 1:
            serie_trozo += "-"  
        else:
            serie_trozo += ".." + str(int(numero_actual))  

        numero_actual += incremento  

    
    serie_trozo += str(int(numero_actual - incremento))  
    serie_final = inicio_serie + " " + serie_trozo  

    print(serie_final)


def main():
    numero_inicio = float(input("Introduce un numero de inicio: "))
    
    incremento = float(input("Introduce con que valor quieres hacer el incremento: "))
    incremento = comprobacion_menor_cero(incremento)
    
    total_serie = int(input("Cuantas veces quieres que se aplique el incremento: "))
    total_serie = comprobacion_menor_cero(total_serie)

    crear_serie(numero_inicio, incremento, total_serie)
        
if __name__ == "__main__":
    main()
