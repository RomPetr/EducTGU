import calculator_logic as c
import pytest


def test_add():
    assert c.add(10, 5) == 15
    assert c.add(-1, 1) == 0
    assert c.add(-2, -2) == -4

    with pytest.raises(TypeError):
        c.add("text", 5)

    with pytest.raises(TypeError):
        c.add(4, "text")

def test_subtruct():
    assert c.subtruct(10, 5) == 5
    assert c.subtruct(-1, 1) == -2
    assert c.subtruct(-2, -2) == 0

    with pytest.raises(TypeError):
        c.subtruct("text", 5)
    with pytest.raises(TypeError):
        c.subtruct(3, "4")


def test_multiply():
    assert c.multiply(10, 5) == 50
    assert c.multiply(-5, 6) == -30
    assert c.multiply(-1, -5) == 5

    # with pytest.raises(TypeError):
    #     c.multiply("text", 5)
    # with pytest.raises(TypeError):
    #     c.multiply(3, "4")

def test_divide():
    assert c.divide(10, 2) == 5
    assert c.divide(-10, 2) == -5
    assert c.divide(-10, -2) == 5

    with pytest.raises(TypeError):
        c.divide("text", 5)
    with pytest.raises(TypeError):
        c.divide(3, "4")
    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)


test_add()
test_subtruct()
test_multiply()
test_divide()
print("Тесты пройдены успешно")