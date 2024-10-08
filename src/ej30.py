def comprobacion_menor_cero(comprobacion):
    bandera2 = True
    
    while bandera2:
        if comprobacion < 0:
            repetir_valor = int(input("Vuelve a introducir el valor porque este no puede ser menor a 0: "))
            if repetir_valor > 0:
                comprobacion = repetir_valor
                bandera2 = False
    
    
    return comprobacion 

def crear_serie():
    return 0

def main():
    cadena_numeros = ""
    bandera = True
    
    while bandera :
        numero_inicio = float(input("Introduce un numero de inicio: "))
        
        incremento = float(input("Introduce con que cantidad quieres hacer el incremento"))
        
        if incremento < 0:
            while bandera:
                print("Error: el incremento debe ser mayor a 0,vuelve a introducirlo de nuevo")
                
                repetir_incremento = float(input("Introduce con que cantidad quieres hacer el incremento: "))
                
                if not repetir_incremento < 0:
                    incremento = repetir_incremento
                    bandera = False
                    
        total_serie =  int(input("Cuantas veces quieres que se le aplique el incremento: "))
        
        if  total_serie < 0:
            while bandera:
                print("Error: el incremento debe ser mayor a 0,vuelve a introducirlo de nuevo")
                
                repetir_total_serie = float(input("Introduce con que cantidad quieres hacer el incremento: "))
                
                if not repetir_total_serie < 0:
                    total_serie = repetir_total_serie
                    bandera = False
            
        
if __name__ == "__main__":
    main()