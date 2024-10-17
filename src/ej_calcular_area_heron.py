from math import sqrt


def calcular_area_heron(lado_a,lado_b,numero3):
    
    semi_area = (lado_a + lado_b + numero3) / 2
    area = sqrt(semi_area * (semi_area - lado_a) * semi_area * (semi_area - lado_b) * semi_area * (semi_area - numero3))
    
    return area


def introduce_float(msj: str) -> float:
    valor = input("\n" + msj).strip().replace(",",".")
    
    while not comprobar_float(valor):
        print("***ERROR*** Número Invalidod!\n")
        valor = input("\n" + msj).strip().replace(",",".")
        
    return float(valor)


def comprobar_float(valor : str) -> bool:
    if valor.startswith("-"): # "-88.67" -> "88.67"
        valor =valor[1:]
    
    posicion_punto = valor.find(".")
    
    if posicion_punto >= 0: # "88.67" -> "8867"
        valor = valor[:posicion_punto] + valor[posicion_punto + 1:]
    
    return valor.isdigit()


def comprovar_triangulo_valido(a,b,c) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)


def main():
    print("Dame los 3 lados del triángulo...")
    
    lado_a = introduce_float("Lado 1: ")
    lado_b = introduce_float("Lado 2: ")
    lado_c = introduce_float("Lado 3: ")
    
    if comprovar_triangulo_valido(lado_a,lado_b,lado_c):
        print(f"\nEl área del triangulo  con los lados ({lado_a:.2f},{lado_b:.2f},{lado_c:.2f}) es de {calcular_area_heron(lado_a,lado_b,lado_c):.2f}.")
    else:
        print(f"El triangulo con los lados ({lado_a:.2f},{lado_b:.2f},{lado_c:.2f}) no es valido ")
    
    
if  __name__ == "__main__":
    main()