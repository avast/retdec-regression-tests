from regression_tests import *

class CommonTest(Test):
    """Output of these tests is nearly the same."""
    settings = TestSettings(
        input=[
            'call-rand.x64.clang.opt0.exe',
            'call-rand.x64.clang.opt2.exe',
            'call-rand.x64.gcc.opt0.exe',
            'call-rand.x64.gcc.opt2.exe',
            'call-rand.x86.clang.opt0.exe',
            'call-rand.x86.clang.opt2.exe',
            'call-rand.x86.gcc.opt0.exe',
            'call-rand.x86.gcc.opt2.exe'
        ])

    def test_main_calls_rand(self):
        main = self.out_c.funcs['main']
        assert main.calls('rand')
