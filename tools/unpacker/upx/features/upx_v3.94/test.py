from regression_tests import *

class TestLzma(Test):
    settings = TestSettings(
        tool='unpacker',
        input=[
            'packed_amd64_lzma',
            'packed_arm_lzma',
            'packed_armeb_lzma',
            'packed_i386_lzma',
            'packed_mips_lzma',
            'packed_mipsel_lzma',
            'packed_powerpc_lzma'
        ]
    )

    def test_lzma(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('LZMA')

class TestNrv2b(Test):
    settings = TestSettings(
        tool='unpacker',
        input=[
            'packed_amd64_nrv2b',
            'packed_arm_nrv2b',
            'packed_armeb_nrv2b',
            'packed_i386_nrv2b',
            'packed_mips_nrv2b',
            'packed_mipsel_nrv2b',
            'packed_powerpc_nrv2b'
        ]
    )

    def test_nrv2b(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2B')

class TestNrv2d(Test):
    settings = TestSettings(
        tool='unpacker',
        input=[
            'packed_amd64_nrv2d',
            'packed_arm_nrv2d',
            'packed_armeb_nrv2d',
            'packed_i386_nrv2d',
            'packed_mips_nrv2d',
            'packed_mipsel_nrv2d',
            'packed_powerpc_nrv2d'
        ]
    )

    def test_nrv2d(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2D')

class TestNrv2e(Test):
    settings = TestSettings(
        tool='unpacker',
        input=[
            'packed_amd64_nrv2e',
            'packed_arm_nrv2e',
            'packed_armeb_nrv2e',
            'packed_i386_nrv2e',
            'packed_mips_nrv2e',
            'packed_mipsel_nrv2e',
            'packed_powerpc_nrv2e'
        ]
    )

    def test_nrv2e(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2E')
