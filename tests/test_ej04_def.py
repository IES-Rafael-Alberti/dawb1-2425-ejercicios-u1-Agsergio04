from src.ej04_def import cambio_temperatura_celsius

def test_cambio_temperatura_celsius():
    assert cambio_temperatura_celsius(15) == "59.00"
    assert cambio_temperatura_celsius(77) == "168.00"
    assert cambio_temperatura_celsius(0) == "0.00"
    assert cambio_temperatura_celsius(82) == "179.60"
    assert cambio_temperatura_celsius(-11) == "12.20"