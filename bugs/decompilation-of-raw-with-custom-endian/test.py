from regression_tests import *

class TestArmLittleGccElf(Test):
    settings = TestSettings(
        input='ack-arm-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='arm',
        args='-k --endian little --raw-section-vma 0x8470 --raw-entry-point 0x8470'
    )

    unk_name='unknown_844c'
    ack_name='function_85a4'

    def test_has_little_endian_functions(self):
        assert self.out_c.has_funcs('function_8658', 'function_85a4')

        main = self.out_c.funcs['function_8658']
        main.calls('unknown_8458') # scanf
        main.calls('function_85a4') # ack
        main.calls('unknown_8428') # printf

        ack = self.out_c.funcs['function_85a4']
        ack.calls('function_85a4') # ack

    def test_has_not_big_endian_functions(self):
        assert not self.out_c.has_funcs('function_8574')

class TestArmBigGccElf(Test):
    settings = TestSettings(
        input='ack-arm-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='arm',
        args='-k --endian big --raw-section-vma 0x8470 --raw-entry-point 0x8470'
    )

    def test_has_not_little_endian_functions(self):
        assert not self.out_c.has_funcs('function_8658', 'function_85a4')

    def test_has_big_endian_functions(self):
        assert self.out_c.has_funcs('entry_point')

class TestPic32LittleGccElf(Test):
    settings = TestSettings(
        input='ack-pic32-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='pic32',
        args='-k --endian little --raw-section-vma 0x9d002d74 --raw-entry-point 0x9d002d74'
    )

    def test_has_little_endian_functions(self):
        assert self.out_c.has_funcs('function_9d0036f0', 'entry_point')

    def test_has_not_big_endian_functions(self):
        assert not self.out_c.has_funcs('function_9d0038b0')

class TestPic32BigGccElf(Test):
    settings = TestSettings(
        input='ack-pic32-elf-little-gcc-O0.bin.elf-sec.raw',
        mode='raw',
        arch='pic32',
        args='-k --endian big --raw-section-vma 0x9d002d74 --raw-entry-point 0x9d002d74'
    )

    def test_has_not_little_endian_functions(self):
        assert not self.out_c.has_funcs('function_9d003614', 'function_9d0036f0', 'function_9d003790')
