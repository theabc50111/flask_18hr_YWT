import pytest


def square(x):
    return x * x

# ========== practice start ==========
# ========== practice end ==========
def test_square(x, expected):
    assert square(x) == expected

