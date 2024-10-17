def cambio_temperatura_celsius(fahrenheit: float) -> float:
    return round(fahrenheit * 9/5 + 32,2)


def main():
    fahrenheit = int(input("Introduce una temperatura en grados Fahrenheit: "))
    celius = cambio_temperatura_celsius(fahrenheit)
    print(f"La temperatura en grados fahrenheit es de {fahrenheit} ºF ({celius:.2f} ºC)")


if __name__ == "__main__":
    main()
