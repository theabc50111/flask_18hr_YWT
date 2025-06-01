import sys

import pytest


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def test_add():
    print("start test_add()")
    assert add(2, 3) == 5


def test_multiply():
    print("start test_multiply()")
    assert multiply(3, 4) == 12


@pytest.mark.skip(reason="Skipping this test for operation time is too long time")
def test_add_skip():
    assert add(2000000000000000, 3000000000000000000) == 5


@pytest.mark.skipif(sys.version_info[1] > 10, reason=f"Skip this test for newer version of python({sys.version})")
def test_multiply_skip():
    assert multiply(3, 4) == 12
