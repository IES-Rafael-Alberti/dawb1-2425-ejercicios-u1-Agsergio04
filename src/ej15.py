cantidad_banco = float(input("Introduce la cantidad de dinero en el banco: "))

for i in range(3):
    anio = i
    calculo_interes = cantidad_banco * (1 + anio)
    print("El interes en primer año es de: ",round(calculo_interes,1))