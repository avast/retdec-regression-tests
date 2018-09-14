from regression_tests import *

class CustomUpxStubsPsyb0t(Test):
    settings = TestSettings(
        tool='unpacker',
        input='psyb0t.elf'
    )

    def test_psyb0t(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2B')

class CustomUpxStubsCrackme2015(Test):
    settings = TestSettings(
        tool='unpacker',
        input='crackme2015.ex'
    )

    def test_crackme2015(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('DIRECT JUMP')
        assert self.unpacker.output.contains('NRV2B')
