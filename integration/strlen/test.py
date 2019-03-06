from regression_tests import *

class Test_2018(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

    def test_check_function_my_strlen(self):
        assert self.out_c.has_func('my_strlen')
        assert self.out_c.funcs['my_strlen'].return_type.is_int(64)
        assert self.out_c.funcs['my_strlen'].param_count == 1
        assert self.out_c.funcs['my_strlen'].params[0].type.is_pointer()
        assert self.out_c.funcs['my_strlen'].params[0].type.pointed_type.is_char()
        assert self.out_c.funcs['my_strlen'].has_any_assignments()
        assert (self.out_c.funcs['my_strlen'].has_any_for_loops()
                or self.out_c.funcs['my_strlen'].has_any_while_loops())
        assert self.out_c.funcs['my_strlen'].has_any_return_stmts()

    def test_check_main_function(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('my_strlen')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].has_any_assignments()
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert len(self.out_c.funcs['main'].return_stmts) == 1

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%s')
        assert self.out_c.has_string_literal('%d\\n')

class Test_2017(Test):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='aaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccdddddddddddd',
            expected_output='52\n',
            expected_return_code=52
        )

class Test_2015(Test):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )

    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='aaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccdddddddddddd',
            expected_output='',
            expected_return_code=52
        )
