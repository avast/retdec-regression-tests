"""
    Checks that we emit real register names in comments instead of our custom
    ones.
"""

from regression_tests import *

class X86Test(Test):
    settings = TestSettings(
        input='input-x86.ex'
    )

    # TODO: we should test that v1 is in fact ecx
    def test_ecx_is_used(self):
        assert self.out_c.contains(r'return printf\("%d\\n", v1\);')

class SameRegAndFncNameTest(Test):
    settings = TestSettings(
        input='eax.x86.gcc.O0.g.exe',
    )

    # we want to find out if there was no LLVM IR syntax error
    # -> c was generated -> just check for main function
    def test_for_main(self):
        assert self.out_c.has_func('main')
