""" Input file raw.bin created as follows:
$ offset=18
$ dd if=/dev/zero bs=$offset count=1 >raw.bin
$ printf "\x31\xc0\xc3" >>raw.bin # xor eax, eax; ret
"""
from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='raw.bin',
        mode='raw',
        arch='x86',
        args='--endian little --raw-section-vma 0x0 --raw-entry-point 0x12'
    )

    def test_check_output(self):
        assert self.out_c.has_just_funcs('entry_point')
        assert self.out_c.has_comment_matching('// Address range: 0x12 - 0x15')
