import pytest


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# ========== practice start ==========
def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    print(type(exc_info), exc_info)
    print(type(exc_info.value), exc_info.value)
    assert (not isinstance(exc_info.value, ZeroDivisionError)) and "Division by zero" in str(exc_info.value)

# ========== practice end ==========
