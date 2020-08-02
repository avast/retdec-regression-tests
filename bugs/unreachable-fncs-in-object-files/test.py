from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='module.o'
    )

    def test_function_present(self):
        assert self.out_c.has_funcs('func', 'main')
        #assert self.out_c.has_comment_matching('// Address range: 0x0 - 0x1c')
        #assert self.out_c.has_comment_matching('// Address range: 0x1d - 0x26')

    def test_function_func(self):
        func = self.out_c.funcs['func']
        assert func.calls('printf')
        assert self.out_c.has_string_literal('Hellow world from func()')
