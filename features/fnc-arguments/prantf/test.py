from regression_tests import *

class CommonTest(Test):
    """Output of these tests is nearly the same."""
    settings = TestSettings(
        input=[
            'prantf.arm.gcc.elf',
            'prantf.arm.clang.elf',
            'prantf.thumb.clang.elf'])

    def test_main_calls_prantf(self):
        main = self.out_c.funcs['main']
        assert main.calls('prantf')
        assert self.out_c.contains('prantf\(.*"My number is %d\.", 1')

class ThumbGccTest(Test):
    settings = TestSettings(input='prantf.thumb.gcc.elf')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('_24_t')
        assert self.out_c.contains('_24_t\(.*"My number is %d\.", 1\)')

        fnc = self.out_c.funcs['_24_t']
        assert fnc.calls('prantf')

class MipsClangTest(Test):
    settings = TestSettings(input='prantf.mips.clang.elf')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('function_400920')
        assert self.out_c.contains('function_400920\(.*"My number is %d\.", 1\)')

        fnc = self.out_c.funcs['function_400920']
        assert fnc.calls('prantf')

class PowerpcClangTest(Test):
    settings = TestSettings(input='prantf.powerpc.clang.elf')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('function_10000630')
        assert self.out_c.contains('function_10000630\(.*"My number is %d\.", 1\)')

        fnc = self.out_c.funcs['function_10000630']
        assert fnc.calls('prantf')

class PowerpcGccTest(Test):
    settings = TestSettings(input='prantf.powerpc.gcc.elf')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('function_10000610')
        assert self.out_c.contains('function_10000610\(.*"My number is %d\.", 1\)')

        fnc = self.out_c.funcs['function_10000610']
        assert fnc.calls('prantf')

class X86ClangElfTest(Test):
    settings = TestSettings(input='prantf.x86.clang.elf')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('function_8048350')
        assert self.out_c.contains('function_8048350\(.*"My number is %d\.", 1\)')

        fnc = self.out_c.funcs['function_8048350']
        assert fnc.calls('prantf')

class X86GccElfTest(Test):
    settings = TestSettings(input='prantf.x86.gcc.elf')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('function_8048350')
        assert self.out_c.contains('function_8048350\(.*"My number is %d\.", 1\)')

        fnc = self.out_c.funcs['function_8048350']
        assert fnc.calls('prantf')

class X86GccPeTest(Test):
    settings = TestSettings(input='prantf.x86.gcc.exe')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('_prantf')
        assert self.out_c.contains('_prantf\(.*"My number is %d\.", 1\)')

        fnc = self.out_c.funcs['_prantf']
        assert fnc.calls('prantf')

class X86ClangPeTest(Test):
    settings = TestSettings(input='prantf.x86.clang.exe')

    def test_structure(self):
        main = self.out_c.funcs['main']
        assert main.calls('_prantf')
        assert self.out_c.contains('_prantf\(.*"My number is %d\.", 1')

        fnc = self.out_c.funcs['_prantf']
        assert fnc.calls('prantf')
