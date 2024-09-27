peso = float(input("Introduce tu peso en kg: "))
altura = int(input("Introduce tu altura en cm: "))

altura = altura / 100
icm = peso / altura**2

print("El ICM es de ",icm)