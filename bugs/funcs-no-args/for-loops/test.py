from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input=files_in_dir('2020-07-31')
    )

    def test_check_function_have_no_args(self):
        f1 = 'f1' if self.out_c.has_func('f1') else '_f1'
        assert self.out_c.has_func(f1)
        assert self.out_c.funcs[f1].param_count == 0
        assert self.out_c.funcs[f1].return_type.is_int(32)

        f2 = 'f2' if self.out_c.has_func('f2') else '_f2'
        assert self.out_c.has_func(f2)
        assert self.out_c.funcs[f2].param_count == 0
        assert self.out_c.funcs[f2].return_type.is_int(32)

        f3 = 'f3' if self.out_c.has_func('f3') else '_f3'
        assert self.out_c.has_func(f3)
        assert self.out_c.funcs[f3].param_count == 0
        assert self.out_c.funcs[f3].return_type.is_int(32)
