frase = input("Introduce una frase cualquiera: ")
vocal = input("Introduce una vocal: ").lower()


frase = frase.replace(vocal, vocal.upper())

print(frase)