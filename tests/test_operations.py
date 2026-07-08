from src.math_operations import add, substract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1, 0) == 1
    assert add(0, 1) == 1
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1, 0) == 1
    assert add(0, 1) == 1

def test_substract():
    assert substract(1, 2) == -1
    assert substract(-1, -2) == 1
    assert substract(-1, 1) == -2
    assert substract(0, 0) == 0
    assert substract(1, 0) == 1
    assert substract(0, 1) == -1
    assert substract(1, 2) == -1
    assert substract(-1, -2) == 1
    assert substract(-1, 1) == -2
    assert substract(0, 0) == 0
    assert substract(1, 0) == 1
    assert substract(0, 1) == -1

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, -2) == 2
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
    assert multiply(1, 0) == 0
    assert multiply(0, 1) == 0
    assert multiply(1, 2) == 2
    assert multiply(-1, -2) == 2
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
    assert multiply(1, 0) == 0
    assert multiply(0, 1) == 0

def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(-1, -2) == 0.5
    assert divide(-1, 1) == -1
    assert divide(0, 0) == 0
    assert divide(1, 0) == 0
    assert divide(0, 1) == 0
    assert divide(1, 2) == 0.5
    assert divide(-1, -2) == 0.5
    assert divide(-1, 1) == -1
    assert divide(0, 0) == 0
    assert divide(1, 0) == 0
    assert divide(0, 1) == 0
