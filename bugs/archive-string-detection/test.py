from regression_tests import *

class TestX86COFF(Test):
    settings=TestSettings(
        input='hello-x86-coff.obj'
    )

    def test_relocations_applied(self):
        assert self.out_dsm.contains('0x62:\s*c7 04 24 b8 00 00 00\s*mov dword ptr \[esp\], 0xb8')
        assert self.out_dsm.contains('0x75:\s*e8 bf ff ff ff\s*call 0x39 <_bar>')
        assert self.out_dsm.contains('0x83:\s*e8 78 ff ff ff\s*call 0 <_foo>')
        assert self.out_dsm.contains('0x90:\s*c7 04 24 c5 00 00 00\s*mov dword ptr \[esp\], 0xc5')

class TestArmCOFF(Test):
    settings=TestSettings(
        input='hello-arm-coff.obj'
    )

    def test_relocations_applied(self):
        assert self.out_dsm.contains('0xe8:\s*00 01 00 00 10 01 00 00')

class TestX86Elf(Test):
    settings=TestSettings(
        input='hello-x86-elf.o'
    )

    def test_relocations_applied(self):
        assert self.out_dsm.contains('0x4c:\s*c7 04 24 a0 00 00 00\s*mov dword ptr \[esp\], 0xa0')
        #assert self.out_dsm.contains('0x5f:\s*e8 c4 ff ff ff\s*call 0x28 <bar>')
        #assert self.out_dsm.contains('0x6d:\s*e8 8e ff ff ff\s*call 0 <foo>')
        #assert self.out_dsm.contains('0x7a:\s*c7 04 24 ad 00 00 00\s*mov dword ptr \[esp\], 0xad')

class TestArmElf(Test):
    settings=TestSettings(
        input='hello-arm-elf.o'
    )

    def test_relocations_applied(self):
        pass
        #assert self.out_dsm.contains('0xb4:\s*d1 ff ff eb\s*bl 0x0 <foo>')
        #assert self.out_dsm.contains('0xc0:\s*e7 ff ff eb\s*bl 0x64 <bar>')
        #assert self.out_dsm.contains('0xe4:\s*fc 00 00 00')
        #assert self.out_dsm.contains('0xe8:\s*0c 01 00 00')

class TestMipsElf(Test):
    settings=TestSettings(
        input='hello-mips-elf.o'
    )

    def test_relocations_applied(self):
        assert self.out_dsm.contains('0xe0:\s*24 44 01 d8\s*addiu \$a0, \$v0, 0x1d8')
        assert self.out_dsm.contains('0xf0:\s*0c 00 00 00\s*jal 0 <foo>')
        assert self.out_dsm.contains('0x100:\s*0c 00 00 1f\s*jal 0x7c <bar>')
        assert self.out_dsm.contains('0x10c:\s*24 64 01 e8\s*addiu \$a0, \$v1, 0x1e8')

class TestPowerPCElf(Test):
    settings=TestSettings(
        input='hello-ppc-elf.o'
    )

    def test_relocations_applied(self):
        assert self.out_dsm.contains('0xfc:\s*30 60 01 6c\s*addic r3, r0, 0x16c')
        assert self.out_dsm.contains('0x108:\s*33 a0 01 7c\s*addic r29, r0, 0x17c')
        assert self.out_dsm.contains('0x110:\s*4b ff fe f1\s*bl 0 <foo>')
        assert self.out_dsm.contains('0x11c:\s*4b ff ff 6d\s*bl 0x88 <bar>')
