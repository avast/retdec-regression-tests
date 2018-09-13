from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='11 7 29',
            expected_output='hello'
        )

        self.assert_c_produces_output_when_run(
            input='2 1 3',
            expected_output='hello'
        )

        self.assert_c_produces_output_when_run(
            input='1 2 3',
            expected_output='greetings'
        )

    def test_c_contains_main(self):
        assert self.out_c.has_func('main')

    def test_c_contains_if(self):
        assert self.out_c.contains(r'if \(')

    def test_c_contains_all_strings(self):
        assert self.out_c.has_string_literal('%d %d %d')
        assert self.out_c.has_string_literal('hello')
        assert self.out_c.has_string_literal('greetings')

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_function_my_sum1(self):
        assert self.out_c.has_func('my_sum1')
        assert self.out_c.funcs['my_sum1'].return_type.is_int(32)
        assert self.out_c.funcs['my_sum1'].param_count == 1
        assert self.out_c.funcs['my_sum1'].params[0].type.is_int(32)
        assert self.out_c.funcs['my_sum1'].calls('rand')
        assert self.out_c.funcs['my_sum1'].has_any_assignments()
        assert self.out_c.funcs['my_sum1'].has_any_return_stmts()
        assert len(self.out_c.funcs['my_sum1'].return_stmts) == 1

    def test_check_function_my_sum2(self):
        assert self.out_c.has_func('my_sum2')
        assert self.out_c.funcs['my_sum2'].return_type.is_int(32)
        assert self.out_c.funcs['my_sum2'].param_count == 1
        assert self.out_c.funcs['my_sum2'].params[0].type.is_int(32)
        assert self.out_c.funcs['my_sum2'].calls('rand')
        assert self.out_c.funcs['my_sum2'].has_any_assignments()
        assert self.out_c.funcs['my_sum2'].has_any_return_stmts()
        assert len(self.out_c.funcs['my_sum2'].return_stmts) == 1

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].calls('my_sum1')
        assert self.out_c.funcs['main'].calls('my_sum2')
        assert self.out_c.funcs['main'].has_any_assignments()
        assert self.out_c.funcs['main'].has_any_if_stmts()
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert len(self.out_c.funcs['main'].return_stmts) == 1

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%d %d %d')
        assert self.out_c.has_string_literal('hello')
        assert self.out_c.has_string_literal('greetings')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
