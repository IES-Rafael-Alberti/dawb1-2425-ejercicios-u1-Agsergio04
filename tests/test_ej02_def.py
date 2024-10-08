from src.ej02_def import media

def test_media():
    assert media(15.5,8) == 124.0
    assert media(9.77,32) == 312.64
    assert media(24, 17) == 408.0
    assert media(132, -11) == -1452.0
    assert media(11.25,0) == 0