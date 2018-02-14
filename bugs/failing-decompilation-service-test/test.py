from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='raw-ack-arm-elf-little',
        mode='raw',
        arch='arm',
        args='--endian little --raw-section-vma 0x8470 --raw-entry-point 0x8470'
    )

    def test_for_function_8674(self):
        assert self.out_c.has_funcs('function_8674')
