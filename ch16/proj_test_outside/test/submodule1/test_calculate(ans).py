# ========== practice start ==========
from submodule1.calculate import Multiplicator, add_two_num


# the function name must start with test_xxx
def test_add_two_num():
    num1 = 2
    num2 = 3
    res = add_two_num(num1, num2)
    assert res == 5


# the class name must start with TestXXXX
class TestMultiplicator:

    # test_multiply() improves readability, but test_xxx() still work
    def test_xxx(self):
        num1 = 4
        num2 = 5
        multiplicator_1 = Multiplicator(num1, num2)
        res = multiplicator_1.multiply()
        assert res == 21  # try 20 as answer

# ========== practice end ==========
