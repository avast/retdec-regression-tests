from regression_tests import *

class TestAddedPush(Test):
    settings = TestSettings(
        tool='unpacker',
        input='d64cacaacfa790dc0f9b268e4ff3406e.ex'
    )

    def test_added_push(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2B')
