import re

from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='7e54c386a941a1785233acc8cf12e569',
        args='-k'
    )

    def assert_func_has_for_loop(self, func_name, expected_loop_header):
        f = self.out_c.func(func_name, '_' + func_name)
        self.assertTrue(f.has_any_for_loops())
        regex = re.compile(expected_loop_header)
        re.match(regex, f.for_loops[0].header)

    def test_quality(self):
        assert self.out_c.has_string_literal('flag is not in strings this time :\'(')
        assert self.out_c.has_string_literal('this_cannot_be_the_flag')
        assert self.out_c.has_string_literal('ziw..')
        fnc = self.out_c.funcs['main']
        assert fnc.calls('printf')
        self.assert_func_has_for_loop('main', 'int32_t i = 0; i < 10; i\+\+')

        assert self.out_c.has_string_literal('flagged==> ')
        fnc = self.out_c.funcs['puts_plt']
        assert fnc.calls('printf')
        assert fnc.calls('putchar')
        self.assert_func_has_for_loop('puts_plt', 'int32_t i = 0; i < 14; i\+\+')
