import pytest


# ========== practice start ==========
@pytest.fixture(name="num1")
def set_num1():
    return 2

@pytest.fixture(name="num2")
def set_num2():
    return 3

# ========== practice end ==========
