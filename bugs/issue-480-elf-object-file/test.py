from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='test.o'
    )

    def test_c(self):
        f = self.out_c.funcs['reverseArray']
        assert f.calls('__x86_get_pc_thunk_ax')

        self.out_c.contains(r'if (.* >= a3)')
        self.out_c.contains(r'while (.* < a3)')
        self.out_c.contains(r'\*v[0-9] = \*v[0-9]') # memory store
        self.out_c.contains(r'[a-b0-9]+ = [a-b0-9]+ + 1') # counter increment
        self.out_c.contains(r'return result') # value return

    def test_dsm(self):
        assert self.out_dsm.contains('; function: reverseArray at 0x0 -- 0x6f')
        assert self.out_dsm.contains('; function: __x86.get_pc_thunk.ax at 0x6f -- 0x73')
