def convertir_a_binario(valor):
    base = 2
    cociente = valor
    resultado = ""
    
    while(cociente >= base):
        resto = cociente % base
        resultado += str(resto)
        cociente = cociente // base 
        
    resultado += str(cociente)
    resultado = resultado[::-1]
          
    return resultado

def main():
    valor = int(input("Introduce un valor: "))
    numero_binario = convertir_a_binario(valor)
    print(numero_binario)
    
if __name__ == "__main__":
    main()