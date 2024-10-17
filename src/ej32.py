def fibonacci(numero):
    num = 1
    num_minus = 0

    serie = str(num_minus) + " " + str(num)
    
    fibonacci = num + num_minus
    
    while fibonacci <= numero:
        
        num = num_minus 
        num_minus = fibonacci
        
        fibonacci = num + num_minus
        serie +=" " + str(fibonacci)
        
    return serie

def main():
    numero = int(input("Introduce hasta que numero quieres ver de la serie de Fibonacci : "))
    print(fibonacci(numero))
    
if  __name__ == "__main__":
    main()
    
