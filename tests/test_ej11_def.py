from src.ej11_def import factorial

def test_factorial():
    assert factorial(1) == "1.0"   
    assert factorial(5) == "15.0"  
    assert factorial(10) == "55.0"  
    assert factorial(0) is None  
    assert factorial(-5) is None  