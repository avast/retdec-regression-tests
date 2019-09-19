from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='fib.mips.clang.O2.elf',
    )

    def test_general_structure(self):
        self.out_c.has_funcs('main', 'fib')

        main = self.out_c.funcs['main']
        assert main.calls('rand')
        assert main.calls('fib')
        assert main.calls('printf')

        fib = self.out_c.funcs['fib']
        assert fib.calls('fib')

        assert self.out_c.has_string_literal( 'fib(%d) = %d\\n' )

    def test_bug_solution(self):
        assert self.out_c.contains(r'v. \= fib.*\- ?1')
        assert self.out_c.contains(r'return fib.*\- ?2.*\+ v.')
