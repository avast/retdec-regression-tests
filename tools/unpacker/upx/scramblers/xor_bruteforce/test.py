from regression_tests import *

class TestLshttpdNonBrute(Test):
    settings = TestSettings(
        tool='unpacker',
        input='lshttpd'
    )

    def test_lshttpd_non_brute(self):
        assert self.unpacker.return_code == 2

class TestLshttpdBrute(Test):
    settings = TestSettings(
        tool='unpacker',
        args='--brute',
        input='lshttpd'
    )

    def test_lshttpd_brute(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('LZMA')
        assert self.unpacker.output.contains('XOR.*0x55')
