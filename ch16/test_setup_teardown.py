

def setup_module():
    print("@@@@@@@@@@ setup_module @@@@@@@@@@")


def setup_function():
    print("~~~~~ setup_function ~~~~~")


def teardown_module():
    print("@@@@@@@@@@ teardown_module @@@@@@@@@@")


def teardown_function():
    print("~~~~~ teardown_function ~~~~~")


def test_some_func():
    print("start test_some_func()")
    assert True

class TestsSomeClass:
    def setup_class():
        print("********* setup_class *********")

    def setup_method(self):
        print("##### setup_method #####")

    def test_case1(self):
        print("start TestsForSetupTeardown.test_case1()")
        assert True

    def test_case2(self):
        print("start TestsForSetupTeardown.test_case2()")
        assert True

    def teardown_method(self):
        print("##### teardown_method #####")

    def teardown_class():
        print("********** teardown_class **********")




#class TestsForSetupTeardownPrettier:
#    @classmethod
#    def setup_class(cls):
#        print("***** setup_class *****")
#
#    def test_case1(self):
#        print("start TestsForSetupTeardown.test_case1()")
#        assert True
#
#    def test_case2(self):
#        print("start TestsForSetupTeardown.test_case2()")
#        assert True
#
#    @classmethod
#    def teardown_class(cls):
#        print("***** teardown_class *****")
#
