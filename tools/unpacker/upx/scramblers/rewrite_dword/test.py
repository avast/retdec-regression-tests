from regression_tests import *

class TestRewriteDword(Test):
    settings = TestSettings(
        tool='unpacker',
        input='f68cc05a3d0454e2f3dc541caf32832dcaa5971dbfe48a0730d53b95eda03ca5'
    )

    def test_rewrite_dword(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2D')
