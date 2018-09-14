"""Checks that we correctly decompiled, detect, and reconstruct loops (for,
while).
"""

import re

from regression_tests import *

class TestBase(Test):
    def assert_func_has_for_loop(self, func_name, expected_loop_header):
        f = self.out_c.func(func_name, '_' + func_name)
        self.assertTrue(f.has_any_for_loops())
        regex = re.compile(expected_loop_header)
        re.match(regex, f.for_loops[0].header)

class for_simple_O0(TestBase):
    settings = TestSettings(
        input=[
            'for-simple.arm.clang.O0.elf',
            'for-simple.arm.gcc.O0.elf',
            'for-simple.mips.clang.O0.elf',
            'for-simple.pic32.gcc.O0.elf',
            'for-simple.powerpc.clang.O0.elf',
            'for-simple.powerpc.gcc.O0.elf',
            'for-simple.thumb.clang.O0.elf',
            'for-simple.thumb.gcc.O0.elf',
            'for-simple.x86.clang.O0.elf',
            'for-simple.x86.gcc.O0.elf',
            'for-simple.arm.gcc.O0.exe',
            'for-simple.x86.clang.O0.exe',
            'for-simple.x86.gcc.O0.exe',
        ]
    )

    def test_f1_has_for_loop(self):
        self.assert_func_has_for_loop('f1', 'int32_t i = 0; i < 100; i\+\+')

    def test_f2_has_for_loop(self):
        self.assert_func_has_for_loop('f2', 'int32_t i = 0; i < 100; i\+\+')

    def test_f3_has_for_loop(self):
        self.assert_func_has_for_loop('f3', 'int32_t i = 1; i < 100; i\+\+')

    def test_f4_has_for_loop(self):
        self.assert_func_has_for_loop('f4', 'int32_t i = 1; i < 100; i\+\+')

    def test_f5_has_for_loop(self):
        self.assert_func_has_for_loop('f5', 'int32_t i = 0; i < g.; i\+\+')

    def test_f6_has_for_loop(self):
        self.assert_func_has_for_loop('f6', 'int32_t i = 0; i < g.; i\+\+')

    def test_f7_has_for_loop(self):
        self.assert_func_has_for_loop('f7', 'int32_t i = 0; i < rand(); i\+\+')

    def test_f8_has_for_loop(self):
        self.assert_func_has_for_loop('f8', 'int32_t i = 0; i < rand(); i\+\+')

    def test_f9_has_for_loop(self):
        self.assert_func_has_for_loop('f9', 'int32_t i = 100; i >= 1; i--')

    # TODO
    #def test_f10_has_for_loop(self):
        #self.assert_func_has_for_loop('f10', 'int32_t i = 100; i >= 2; i--')

class for_simple_O0_MIPS_gcc(TestBase):
    settings = TestSettings(
        input='for-simple.mips.gcc.O0.elf'
    )

    def test_dsm_contains_correct_function_names(self):
        # Ensure that in the generated DSM, we have correct function names
        # (e.g. f1, not f1.1).
        assert self.decompiler.out_dsm.contains(r'; function: f1 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f1>')

        assert self.decompiler.out_dsm.contains(r'; function: f2 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f2>')

        assert self.decompiler.out_dsm.contains(r'; function: f3 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f3>')

        assert self.decompiler.out_dsm.contains(r'; function: f4 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f4>')

        assert self.decompiler.out_dsm.contains(r'; function: f5 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f5>')

        assert self.decompiler.out_dsm.contains(r'; function: f6 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f6>')

        assert self.decompiler.out_dsm.contains(r'; function: f7 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f7>')

        assert self.decompiler.out_dsm.contains(r'; function: f8 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f8>')

        assert self.decompiler.out_dsm.contains(r'; function: f9 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f9>')

        assert self.decompiler.out_dsm.contains(r'; function: f10 at')
        assert self.decompiler.out_dsm.contains(r'jal 0x[0-9a-f]+ <f10>')
