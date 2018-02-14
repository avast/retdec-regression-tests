from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='test.bin'
    )

    def test_instruction_and_data_alignment(self):
        assert self.out_dsm.contains(r'0x839c:    08 40 2d e9   	push \{r3, lr\}')
        assert self.out_dsm.contains(r'0x83b8:    84 83 00 00                                        |....            |')
        assert self.out_dsm.contains(r'0x85a0:    08 40 2d e9   	push \{r3, lr\}')
        assert self.out_dsm.contains(r'0x8134:    2f 6c 69 62 2f 6c 64 2d  6c 69 6e 75 78 2e 73 6f   |/lib/ld-linux.so|')
        assert self.out_dsm.contains(r'0x8634:    00 00 00 00                                        |....            |')
        assert self.out_dsm.contains(r'0x10638:   04 85 00 00                                        |....            |')
        assert self.out_dsm.contains(r'0x1075c:   00 00 00 00 00 00 00 00                            |........        |')
