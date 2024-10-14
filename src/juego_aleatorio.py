"Si el numero esta cerca de 10 unidades decirle te acerca shurra"
"Si se aleja de 11 o mas le dice te congela shurra"
"intentos "
"Un numero aleatorio"

import random 

def generar_numero_aleatorio():
    return random.randint(1,100)
def main():
    numero_aleatorio = generar_numero_aleatorio()
    contador = 0
    jugador = ""
    
    print("Vamos a jugar a adivinar el numero :p \nTienes que escribir un numero del 1 al 100 en 5 intentos o menos")
    print(numero_aleatorio)
    while jugador != numero_aleatorio and contador < 6:
        print(f"Llevas {contador} intentos.")
        jugador = int(input("Introduce el numero: "))
        
        if jugador < 1 or jugador > 100:
            print("Numero no valido,por favor mete un numero entre el 1 y el 100")
        contador += 1
    
    if numero_aleatorio == jugador:
        print("Grande lokete has ganado!!!")
    
    else:
        print("Mondongo!!!")    
    
if __name__ == "__main__":
    main()