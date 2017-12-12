from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='unpacker',
        input='mpress.ex'
    )

    def test_correctly_unpacks_input_file(self):
        assert self.unpacker.succeeded
