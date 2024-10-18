from src.ej01_def import saludo

def test_saludo():
    assert saludo("Juan") == "Hola Juan"
    assert saludo("Mario") == "Hola Mario"
    assert saludo("Carlos") == "Hola Carlos"
    assert saludo("") == "Hola "
