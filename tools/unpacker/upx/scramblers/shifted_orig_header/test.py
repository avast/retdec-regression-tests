from regression_tests import *

class TestShiftedOriginalHeader(Test):
    settings = TestSettings(
        tool='unpacker',
        input='e64b7a5a586d7e0820e0303fd87a969d3de222dc6eba3a2ab25f5428303e4b4b'
    )

    def test_shifted_original_header(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('Original header found at address 0x1bef23 in extra data.')
