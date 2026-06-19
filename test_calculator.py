import pytest
from calculator import add, subtract, multiply, divide
def test_operations():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)
