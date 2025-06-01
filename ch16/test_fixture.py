import pytest


# Define a fixture that provides value for `sample_input` of `test_some_func()`
@pytest.fixture
def sample_input():
    return (2, 3)

def test_some_func(sample_input):
    a, b = sample_input
    print(f"a: {a}, b: {b}")
    assert True
