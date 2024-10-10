correo = input("Introduce tu correo: ")

if '@' in correo:
    correo = correo.split('@')
    nombre_correo = correo[0]
    educa_correo = nombre_correo + "@ceu.es"
    print(educa_correo)
