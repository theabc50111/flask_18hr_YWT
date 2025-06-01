import time


# Code that will be replaced by the mocker
def slow_function():
    time.sleep(5)
    return "done"


# Code to test
def process():
    result = slow_function()
    return f"Result: {result}"


def test_process():
    result = process()
    print(f"Without mocker, the result of process(): {result}")
    assert result == "Result: done"


# Test using mocker
def test_process_with_mock(mocker):
    # Patch the __name__.slow_function  that is invoked in process()
    mocker.patch(target=f"{__name__}.slow_function", return_value="mocked")
    result = process()
    print(f"With mocker, the result of process(): {result}")
    assert result == "Result: mocked"
