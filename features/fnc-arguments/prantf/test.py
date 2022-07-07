from regression_tests import *

class CommonTest(Test):
    """Output of these tests is nearly the same."""
    settings = TestSettings(
        input=[
            'prantf.arm.gcc.elf',
            'prantf.arm.clang.elf',
            'prantf.thumb.clang.elf',
            'prantf.mips.clang.elf',
            'prantf.powerpc.clang.elf',
            'prantf.powerpc.gcc.elf',
            'prantf.thumb.gcc.elf',
            'prantf.x86.clang.elf',
            'prantf.x86.gcc.elf',
            'prantf.x86.gcc.exe',
            'prantf.x86.clang.exe'
        ])

    def test_main_calls_prantf(self):
        main = self.out_c.funcs['main']
        assert main.calls('prantf')
        assert self.out_c.contains('prantf\(.*"My number is %d\.", 1')
