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

    def test_statically_linked_function_detection(self):
        # confirmed functions
        assert self.out_config.is_statically_linked('___dyn_tls_dtor@12', 0x401640)
        assert self.out_config.is_statically_linked('___dyn_tls_init@12', 0x401690)
        assert self.out_config.is_statically_linked('__decode_pointer', 0x401730)
        assert self.out_config.is_statically_linked('_mingw_onexit', 0x401750)
        assert self.out_config.is_statically_linked('_atexit', 0x401810)
        assert self.out_config.is_statically_linked('__gnu_exception_handler@4', 0x401830)
        assert self.out_config.is_statically_linked('___mingw_raise_matherr', 0x401990)
        assert self.out_config.is_statically_linked('__matherr', 0x4019f0)
        assert self.out_config.is_statically_linked('___report_error', 0x401a60)
        assert self.out_config.is_statically_linked('___write_memory.part.0', 0x401ab0)
        assert self.out_config.is_statically_linked('__pei386_runtime_relocator', 0x401d00)
        assert self.out_config.is_statically_linked('__ValidateImageBase', 0x401fb0)
        assert self.out_config.is_statically_linked('__FindPESection', 0x401fe0)
        assert self.out_config.is_statically_linked('__FindPESectionByName', 0x402020)
        assert self.out_config.is_statically_linked('___mingw_GetSectionForAddress', 0x4020b0)
        assert self.out_config.is_statically_linked('___mingw_GetSectionCount', 0x4020f0)
        assert self.out_config.is_statically_linked('__FindPESectionExec', 0x402120)
        assert self.out_config.is_statically_linked('__GetPEImageBase', 0x402180)
        assert self.out_config.is_statically_linked('__IsNonwritableInCurrentImage', 0x4021b0)
        assert self.out_config.is_statically_linked('___mingw_enum_import_library_names', 0x402200)
        assert self.out_config.is_statically_linked('___mingw_get_msvcrt_handle', 0x402290)
        assert self.out_config.is_statically_linked('___do_global_dtors', 0x402360)
        assert self.out_config.is_statically_linked('___main', 0x4023e0)
        assert self.out_config.is_statically_linked('___security_init_cookie', 0x402400)
        assert self.out_config.is_statically_linked('___report_gsfailure', 0x4024d0)
        assert self.out_config.is_statically_linked('___mingwthr_run_key_dtors.part.0', 0x402560)
        assert self.out_config.is_statically_linked('____w64_mingwthr_add_key_dtor', 0x4025d0)
        assert self.out_config.is_statically_linked('____w64_mingwthr_remove_key_dtor', 0x402660)
        assert self.out_config.is_statically_linked('___mingw_TLScallback', 0x402700)
        assert self.out_config.is_statically_linked('__InterlockedCompareExchange', 0x4027d0)
        assert self.out_config.is_statically_linked('_InterlockedCompareExchange@12', 0x4027f0)
        assert self.out_config.is_statically_linked('___mingw_fprintf', 0x402810)
        assert self.out_config.is_statically_linked('___mingw_vfprintf', 0x402850)
        assert self.out_config.is_statically_linked('___pformat_cvt', 0x402890)
        assert self.out_config.is_statically_linked('___pformat_putc', 0x402990)
        assert self.out_config.is_statically_linked('___pformat_wputchars', 0x4029f0)
        assert self.out_config.is_statically_linked('___pformat_putchars', 0x402af0)
        assert self.out_config.is_statically_linked('___pformat_emit_inf_or_nan', 0x402b90)
        assert self.out_config.is_statically_linked('___pformat_int', 0x402c30)
        assert self.out_config.is_statically_linked('___pformat_xint', 0x402ef0)
        assert self.out_config.is_statically_linked('___pformat_emit_radix_point', 0x403200)
        assert self.out_config.is_statically_linked('___pformat_emit_float', 0x4032e0)
        assert self.out_config.is_statically_linked('___pformat_emit_efloat', 0x403600)
        assert self.out_config.is_statically_linked('___pformat_float', 0x4036d0)
        assert self.out_config.is_statically_linked('___pformat_gfloat', 0x4037b0)
        assert self.out_config.is_statically_linked('___pformat_xldouble', 0x403930)
        assert self.out_config.is_statically_linked('___pformat_efloat', 0x403e30)
        assert self.out_config.is_statically_linked('___mingw_pformat', 0x403ee0)
        assert self.out_config.is_statically_linked('___gdtoa', 0x404830)
        assert self.out_config.is_statically_linked('___wcrtomb_cp', 0x405e40)
        assert self.out_config.is_statically_linked('_wcrtomb', 0x405ee0)
        assert self.out_config.is_statically_linked('_wcsrtombs', 0x405f40)
        assert self.out_config.is_statically_linked('___mbrtowc_cp', 0x406040)
        assert self.out_config.is_statically_linked('_mbrtowc', 0x4061e0)
        assert self.out_config.is_statically_linked('_mbsrtowcs', 0x406260)
        assert self.out_config.is_statically_linked('_mbrlen', 0x406390)
        assert self.out_config.is_statically_linked('___rv_alloc_D2A', 0x4063f0)
        assert self.out_config.is_statically_linked('___nrv_alloc_D2A', 0x406430)
        assert self.out_config.is_statically_linked('___freedtoa', 0x406480)
        assert self.out_config.is_statically_linked('___quorem_D2A', 0x4064a0)
        assert self.out_config.is_statically_linked('___mingw_set_output_format', 0x4066b0)
        assert self.out_config.is_statically_linked('___mingw_get_output_format', 0x406720)
        assert self.out_config.is_statically_linked('_dtoa_lock', 0x406780)
        assert self.out_config.is_statically_linked('_dtoa_unlock', 0x406840)
        assert self.out_config.is_statically_linked('_dtoa_lock_cleanup', 0x406870)
        assert self.out_config.is_statically_linked('___Balloc_D2A', 0x4068b0)
        assert self.out_config.is_statically_linked('___Bfree_D2A', 0x406970)
        assert self.out_config.is_statically_linked('___multadd_D2A', 0x4069c0)
        assert self.out_config.is_statically_linked('___i2b_D2A', 0x406ab0)
        assert self.out_config.is_statically_linked('___mult_D2A', 0x406ae0)
        assert self.out_config.is_statically_linked('___pow5mult_D2A', 0x406c40)
        assert self.out_config.is_statically_linked('___lshift_D2A', 0x406d60)
        assert self.out_config.is_statically_linked('___cmp_D2A', 0x406e70)
        assert self.out_config.is_statically_linked('___diff_D2A', 0x406ee0)
        assert self.out_config.is_statically_linked('___b2d_D2A', 0x407070)
        assert self.out_config.is_statically_linked('___d2b_D2A', 0x407170)
        assert self.out_config.is_statically_linked('___strcp_D2A', 0x407280)
        assert self.out_config.is_statically_linked('___rshift_D2A', 0x4072b0)
        assert self.out_config.is_statically_linked('___trailz_D2A', 0x4073c0)
        assert self.out_config.is_statically_linked('_msvcrt__lc_codepage_func', 0x407400)
        assert self.out_config.is_statically_linked('_setlocale_codepage_hack', 0x407410)
        assert self.out_config.is_statically_linked('_init_codepage_func', 0x407450)
        assert self.out_config.is_statically_linked('__umoddi3', 0x4075e0)
        assert self.out_config.is_statically_linked('__udivdi3', 0x407720)
        # leftovers - unconfirmed
        assert not self.out_config.is_statically_linked('___do_global_ctors', 0x402390)
