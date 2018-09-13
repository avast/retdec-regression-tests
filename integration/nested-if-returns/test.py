from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='1 2 3',
            expected_return_code=4,
            expected_output='XYZ\n'
        )
        self.assert_c_produces_output_when_run(
            input='0 10 0',
            expected_return_code=3,
            expected_output='XY\n'
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_function_func(self):
        assert self.out_c.has_func('func')
        func = self.out_c.funcs['func']
        assert func.return_type.is_int(32)
        assert func.param_count == 0
        assert func.has_any_if_stmts()
        assert func.has_any_return_stmts()
        assert func.calls('scanf')
        assert func.calls('printf') or func.calls('puts')
        if func.calls('printf'):
            assert self.out_c.has_string_literal('XYZ\\n')
            assert self.out_c.has_string_literal('XY\\n')
            assert self.out_c.has_string_literal('X\\n')

        elif func.calls('puts'):
            assert self.out_c.has_string_literal('XYZ')
            assert self.out_c.has_string_literal('XY')
            assert self.out_c.has_string_literal('X')

    def test_check_funcion_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('func')
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert len(self.out_c.funcs['main'].return_stmts) == 1

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%d %d %d')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
