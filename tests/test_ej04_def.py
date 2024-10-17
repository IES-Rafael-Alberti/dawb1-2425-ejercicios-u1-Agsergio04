from src.ej04_def2 import cambio_temperatura_celsius

def test_cambio_temperatura_celsius():
    assert cambio_temperatura_celsius(15) == 59.00
    assert cambio_temperatura_celsius(20) == 68.00
    assert cambio_temperatura_celsius(-11) == 12.20
   
