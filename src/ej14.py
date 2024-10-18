cantidad_payasos = int(input("Introduce la cantidad de pallasos que hay: "))
cantidad_muniecas = int(input("Introduce la cantidad de muñecas que hay: "))

peso_total = ((cantidad_payasos * 112) + (cantidad_muniecas * 75))/1000

print("El peso total es de: ",peso_total, " en kg")