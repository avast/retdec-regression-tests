from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='x86-elf-1d991da0b51196786c6e3e8843435d6e',
        args='-k'
    )

    def test_atexit_calls_arguments_are_not_strings(self):
        assert self.out_c.contains('__cxa_atexit\(.*0x804b138.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x8050ce0.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x8050d00.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x8050d40.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x8051090.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x80510a0.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x80510b0.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x80510c0.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x8051920.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x80510d0.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x80510e0.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x80510f0.*\)')
        assert self.out_c.contains('__cxa_atexit\(.*0x8051100.*\)')
