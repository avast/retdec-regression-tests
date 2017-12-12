"""
    Checks that we emit real register names in comments instead of our custom
    ones.
"""

from regression_tests import *

class X86Test(Test):
    settings = TestSettings(
        input='input-x86.ex'
    )

    def test_real_register_name_is_emitted_in_comment(self):
        assert self.out_c.contains(r'int32_t g[0-9]+ = 0; // ecx')

class SameRegAndFncNameTest(Test):
    settings = TestSettings(
        input='eax.x86.gcc.O0.g.exe',
    )

    # we want to find out if there was no LLVM IR syntax error
    # -> c was generated -> just check for main function
    def test_for_main(self):
        assert self.out_c.has_func('main')
