def cambio_temperatura_celsius():
    pedir_temperatura = int(input("Introduce una temperatura en grados Celsuis: "))
    fahrenheit = pedir_temperatura * 9/5 + 32
    return f"La temperatura en grados Farenheit es de {fahrenheit:.2f} ºF ({pedir_temperatura:.2f} ºC)"


def main():
    print(cambio_temperatura_celsius())


if __name__ == "__main__":
    main()