import pytest


def square(x):
    return x * x

@pytest.mark.parametrize(
    argnames="x, expected",
    argvalues=[
        (2, 4),
        (3, 9),
        (4, 16),
    ],
    ids=["2 squared", "3 squared", "4 squared"]
)
def test_square(x, expected):
    assert square(x) == expected

