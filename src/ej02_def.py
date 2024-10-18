def media(costo_hora_trabajo,costo_hora):
    return costo_hora_trabajo * costo_hora


def main():
    costo_hora_trabajo = float(input("Introduce cuanto ganas por hora: "))
    costo_hora = int(input("Introduce cuantas horas trabajas: "))
    print(f"El importe total es de: {media(costo_hora_trabajo,costo_hora)}")
    

if __name__ == "__main__":
    main()