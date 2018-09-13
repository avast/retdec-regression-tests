from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='1.2 34.56 67.89',
            expected_return_code=0,
            expected_output=
'''#2 3.140000
3.140000
67.889999
'''
        )
        self.assert_c_produces_output_when_run(
            input='123.456 67.89 34.56',
            expected_return_code=0,
            expected_output=
'''#2 3.140000
123.456001
67.889999
'''
        )

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

    def test_check_function_comp_const_const(self):
        assert self.out_c.has_func('comp_const_const')
        assert self.out_c.funcs['comp_const_const'].return_type.is_void()
        assert self.out_c.funcs['comp_const_const'].param_count == 0
        #assert self.out_c.funcs['comp_const_const'].calls('scanf')
        assert self.out_c.funcs['comp_const_const'].calls('printf')
        #assert self.out_c.funcs['comp_const_const'].has_any_if_stmts()

    def test_check_function_comp_scanf_scanf(self):
        assert self.out_c.has_func('comp_scanf_scanf')
        assert self.out_c.funcs['comp_scanf_scanf'].return_type.is_void()
        assert self.out_c.funcs['comp_scanf_scanf'].param_count == 0
        assert self.out_c.funcs['comp_scanf_scanf'].calls('scanf')
        assert self.out_c.funcs['comp_scanf_scanf'].calls('printf')

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('comp_const_const')
        assert self.out_c.funcs['main'].calls('comp_scanf_scanf')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
