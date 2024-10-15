def fibonacci(numero):
    aux = 1
    linea_serie = "0"
    
    for b in range(numero):
        linea_serie += " " + str(c)
        
    return linea_serie


def main():
    numero = int(input("Introduce hasta que numero quieres ver de la serie de Fibonacci : "))
    print(fibonacci(numero))
    
    
if  __name__ == "__main__":
    main()
    
