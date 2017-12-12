from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='1  1',
            expected_output='ackerman( 1 , 1 ) = 3\n',
            expected_return_code=3
        )
        self.assert_c_produces_output_when_run(
            input='2  23  1',
            expected_output='ackerman( 2 , 23 ) = 49\n',
            expected_return_code=49
        )
        self.assert_c_produces_output_when_run(
            input='0       0',
            expected_output='ackerman( 0 , 0 ) = 1\n',
            expected_return_code=1
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015_ArmClangElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.arm.clang-3.2.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x844c:\s*0d 20 a0 e1\s*mov r2, sp')
        assert self.out_dsm.contains('0x85e4:\s*08 00 8d e5\s*str r0, \[sp, \#8\]')
        assert self.out_dsm.contains('0x8694:\s*10 10 1b e5\s*ldr r1, \[fp, \#\-0x10\]')

class Test_2015_ArmGccElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.arm.gnuarmgcc-4.4.1.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x8084:\s*01 30 a0 e3\s*mov r3, \#1')
        assert self.out_dsm.contains('0x8214:\s*ff 00 00 00\s*strdeq r0, r1, \[r0\], \-pc')
        assert self.out_dsm.contains('0x81c4:\s*04 40 12 85\s*ldrhi r4, \[r2, \#\-4\]')

class Test_2015_ArmGccExe(TestBase):
    settings = TestSettings( input='2015-03-30/ack.arm.mingw32ce-4.4.0.O0.g.ex' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x11004:\s*00 40 a0 e1\s*mov r4, r0')
        assert self.out_dsm.contains('0x11080:\s*10 30 1b e5\s*ldr r3, \[fp, \#\-0x10\]')
        assert self.out_dsm.contains('0x11628:\s*00 b0 a0 11\s*movne fp, r0')

class Test_2015_MipsClangElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.mips.clang-3.2.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x4004ec:\s*af bc 00 10\s*sw \$gp, 0x10\(\$sp\)')
        assert self.out_dsm.contains('0x4005e4:\s*24 84 0b 14\s*addiu \$a0, \$a0, 0xb14')
        assert self.out_dsm.contains('0x4008f8:\s*00 12 90 83\s*sra \$s2, \$s2, 2')

class Test_2015_MipsGccElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.mips.pspgcc-4.3.5.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x8900044:\s*00 00 62 24\s*addiu \$v0, \$v1, 0')
        assert self.out_dsm.contains('0x890018c:\s*60 00 b3 af\s*sw \$s3, 0x60\(\$sp\)')
        assert self.out_dsm.contains('0x890026c:\s*ff ff 51 24\s*addiu \$s1, \$v0, -1')

    def test_properties(self):
        assert self.out_c.has_comment_matching('// int printf\(const char \* restrict format, ...\);')
        assert self.out_c.has_comment_matching('// int scanf\(const char \* restrict format, ...\);')
        assert self.out_c.contains('int32_t x = 0; // bp-28')
        assert self.out_c.contains('int32_t y = 0; // bp-24')

class Test_2015_Pic32GccElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.pic32.gcc-4.5.2.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x9d001dac:\s*01 00 05 24\s*addiu \$a1, \$zero, 1')
        assert self.out_dsm.contains('0x9d001e38:\s*00 9d 04 3c\s*lui \$a0, 0x9d00')
        assert self.out_dsm.contains('0x9d002c1c:\s*25 64 20 25\s*addiu \$zero, \$t1, 0x6425')

class Test_2015_PowerpcGccElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.powerpc.gcc-4.5.1.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x100003ac:\s*93 a1 00 14\s*stw r29, 0x14\(r1\)')
        assert self.out_dsm.contains('0x1000047c:\s*38 09 00 00\s*addi r0, r9, 0')
        assert self.out_dsm.contains('0x10000548:\s*7c 60 1b 78\s*mr r0, r3')

class Test_2015_ThumbClangElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.thumb.clang-3.2.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x8458:\s*10 c0 9f e5\s*ldr ip, \[pc, \#0x10\]')
        assert self.out_dsm.contains('0x8500:\s*08 80 bd 08\s*popeq \{r3, pc\}')
        assert self.out_dsm.contains('0x85a8:\s*06 98\s*ldr r0, \[sp, \#0x18\]')

class Test_2015_ThumbGccElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.thumb.gnuarmgcc-4.4.1.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x8100:\s*0b 78\s*ldrb r3, \[r1\]')
        assert self.out_dsm.contains('0x81e0:\s*bd 46\s*mov sp, r7')
        assert self.out_dsm.contains('0xe1e2:\s*18 43\s*orrs r0, r3')

class Test_2015_X86ClangElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.x86.clang-3.2.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x8048479:\s*89 44 24 04\s*mov dword ptr \[esp \+ 4\], eax')
        assert self.out_dsm.contains('0x80484f0:\s*a1 24 98 04 08\s*mov eax, dword ptr \[0x8049824\]')
        assert self.out_dsm.contains('0x8048699:\s*29 c6\s*sub esi, eax')

class Test_2015_X86ClangExe(TestBase):
    settings = TestSettings( input='2015-03-30/ack.x86.clang-3.2.O0.g.ex' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x4010d3:\s*89 10\s*mov dword ptr \[eax\], edx')
        assert self.out_dsm.contains('0x401563:\s*83 ec 1c\s*sub esp, 0x1c')
        assert self.out_dsm.contains('0x40138b:\s*8d 70 01\s*lea esi, \[eax \+ 1\]')

class Test_2015_X86GccElf(TestBase):
    settings = TestSettings( input='2015-03-30/ack.x86.gcc-4.7.2.O0.g.elf' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x8048420:\s*b8 03 99 04 08\s*mov eax, 0x8049903')
        assert self.out_dsm.contains('0x804853c:\s*c7 44 24 04 01 00 00 00\s*mov dword ptr \[esp \+ 4\], 1')
        assert self.out_dsm.contains('0x804864b:\s*ff 94 bb 18 ff ff ff\s*call dword ptr \[ebx \+ edi\*4 \- 0xe8\]')

    def test_check_for_tmp_variable_address_in_output_c(self):
        assert self.out_c.contains('result = ack\(x, y\); // 0x80485c3')

class Test_2015_X86GccExe(TestBase):
    settings = TestSettings( input='2015-03-30/ack.x86.mingw32-gcc-4.7.3.O0.g.ex' )

    def test_check_dsm(self):
        assert self.out_dsm.contains('0x4010ce:\s*a1 cc b1 40 00\s*mov eax, dword ptr \[0x40b1cc\]')
        assert self.out_dsm.contains('0x401123:\s*66 81 fa 0b 02\s*cmp dx, 0x20b')
        assert self.out_dsm.contains('0x4011a0:\s*8d 44 24 1b\s*lea eax, \[esp \+ 0x1b\]')

    def test_unwanted_properties(self):
        assert not self.out_c.contains('int32_t g.*; // ebp') # there should be no work with ebp

    def test_properties(self):
        assert self.out_c.has_comment_matching('// int printf\(const char \* restrict format, ...\);')
        assert self.out_c.has_comment_matching('// int scanf\(const char \* restrict format, ...\);')
        assert self.out_c.contains('int32_t x = 0; // bp-24')
        assert self.out_c.contains('int32_t y = 0; // bp-28')
