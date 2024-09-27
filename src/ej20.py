
telefono = input("Introduce un número de teléfono en el formato +34-número-extensión: ")

if telefono.startswith("+34-") and '-' in telefono[4:]:
    numero_partido = telefono.split('-')
    numero = numero_partido[1]
    
print("Número de teléfono sin prefijo y extensión:", numero)
