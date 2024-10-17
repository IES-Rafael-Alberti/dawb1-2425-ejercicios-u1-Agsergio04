from src.ej05_def2 import calculo_iva_porcentaje_dado

def test_def_calculo_iva_porcentaje_dado():
    assert calculo_iva_porcentaje_dado(100, 15) == "El importe sin iva es de 100.00 y el importe de iva aplicado es 115.00"
    assert calculo_iva_porcentaje_dado(16, 100) == "El importe sin iva es de 16.00 y el importe de iva aplicado es 32.00"
    assert calculo_iva_porcentaje_dado(80, -11) == "El importe sin iva es de 80.00 y el importe de iva aplicado es 96.80"
    assert calculo_iva_porcentaje_dado(10, 0) == "El importe sin iva es de 10.00 y el importe de iva aplicado es 10.00"
    assert calculo_iva_porcentaje_dado(0,100) == "El importe sin iva es de 0.00 y el importe de iva aplicado es 0.00"
