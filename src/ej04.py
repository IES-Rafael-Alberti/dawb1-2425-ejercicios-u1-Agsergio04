"""

Relacion 1 de ejercicios

pedir_temperatura = int(input("Introduce una temperatura en grados Celsuis: "))
fahrenheit = pedir_temperatura * 9/5 + 32

print("La temperatura en Fahrenheit es de: ",fahrenheit)
"""

pedir_temperatura = int(input("Introduce una temperatura en grados Celsuis: "))
fahrenheit = pedir_temperatura * 9/5 + 32

print(f"La temperatura en grados Farenheit es de {fahrenheit:.2f} ºF ({pedir_temperatura:.2f}ºC)")