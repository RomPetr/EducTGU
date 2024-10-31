import calculator_logic as c


def test_add():
    assert c.add(10, 5) == 15
    assert c.add(-1, 1) == 0
    assert c.add(-2, -2) == -4

def test_subtruct():
    assert c.subtruct(10, 5) == 5
    assert c.subtruct(-1, 1) == -2
    assert c.subtruct(-2, -2) == 0


def test_multiply():
    assert c.multiply(10, 5) == 50
    assert c.multiply(-5, 6) == -30
    assert c.multiply(-1, -5) == 5


def test_divide():
    assert c.divide(10, 2) == 5
    assert c.divide(-10, 2) == -5
    assert c.divide(-10, -2) == 5


test_add()
test_subtruct()
test_multiply()
test_divide()
print("Тесты пройдены успешно")