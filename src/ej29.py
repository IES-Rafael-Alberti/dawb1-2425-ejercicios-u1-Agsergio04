def main():
    bandera = True
    
    while(bandera):
        nombre = input("Introduce un nombre: ")
        edad = int(input("Introduce una edad: "))
        if not 0 < edad < 125:
            print("Edad no valida")
        elif(nombre == ""):
            jhon_doe = "Desconocido"
            print(f"Te llamas {jhon_doe} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir")
            bandera = False
        else:
            print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir")
            bandera = False

if __name__ == "__main__":
    main()