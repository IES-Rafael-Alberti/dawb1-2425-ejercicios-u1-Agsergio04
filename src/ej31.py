def main():
    numero = int(input("Introduce un numero: "))
    
    
    for i in range(numero + 1):
        if i != 0: 
            if numero % i == 0:
                print(i)
                
                
if __name__ == "__main__":
    main()