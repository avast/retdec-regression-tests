from regression_tests import *

class Test1(Test):

    settings = TestSettings(
        input='ack-x86-pe-little-gcc-O0.bin.exe-fnc.raw',
        mode='raw',
        arch='x86',
        args='--endian little --raw-entry-point 0x401560 --raw-section-vma 0x401560'
    )

    def test_check_dsm(self):
        assert self.out_dsm.contains('function: entry_point at 0x401560 -- 0x4015d4')
        assert self.out_dsm.contains('0x401560:\s*55\s*push ebp')
        assert self.out_dsm.contains('0x40158f:\s*83 c0 01\s*add eax, 1')
        assert self.out_dsm.contains('0x4015d3:\s*c3\s*ret')
