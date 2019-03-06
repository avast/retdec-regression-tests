from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        assert self.out_c.has_func( 'main' )
        self.assert_c_produces_output_when_run(
            input='100 500',
            expected_return_code=0,
            expected_output=
'''123456
456789
654321
100
987654
500
'''
        )
        self.assert_c_produces_output_when_run(
            input='200 600',
            expected_return_code=0,
            expected_output=
'''123456
456789
654321
200
987654
600
'''
        )

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

    def test_check_global_vars(self):
        assert self.out_c.has_any_global_vars()
        assert self.out_c.has_global_vars('g1', 'g3')
        assert self.out_c.global_vars['g1'].type.is_int(32)
        assert self.out_c.global_vars['g3'].type.is_int(32)
        assert self.out_c.global_vars['g1'].initializer == 987654
        assert self.out_c.global_vars['g3'].initializer == 654321

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert self.out_c.funcs['main'].has_return_stmts('return 0')

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal('%d\\n')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
