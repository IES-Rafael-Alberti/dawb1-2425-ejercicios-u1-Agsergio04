def fibonacci(numero):
    serie_inicial = 0
    serie_secundaria = 1
    linea = "0"

    for _ in range(numero):
        valor = serie_inicial + serie_secundaria
        serie_inicial = serie_secundaria
        serie_secundaria = valor

        linea +=" " + str(serie_inicial)
    
    return linea


def main():
    numero = int(input("Introduce hasta que numero quieres ver de la serie de Fibonacci : "))
    print(fibonacci(numero))
    
    
if  __name__ == "__main__":
    main()
    
