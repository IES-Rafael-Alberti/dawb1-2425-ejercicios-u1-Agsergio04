def factorial(numero_introducido):

    if (numero_introducido > 0):
        suma = (numero_introducido * (numero_introducido + 1))/2
        return str(suma)


def main():
    numero_introducido = int(input("Introduce un numero: "))
    print(f"La suma de todos los numeros hasta {numero_introducido} es de " + factorial(numero_introducido))
    
    
if __name__ == "__main__":
    main()