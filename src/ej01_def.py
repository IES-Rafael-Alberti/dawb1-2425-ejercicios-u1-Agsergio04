def saludo(nombre):
    return f"Hola {nombre}"


def main():
    nombre = input("Introduce tu nombre: ")
    print(saludo(nombre))
    
    
if __name__ == "__main__":
    main()