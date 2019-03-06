from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='',
            expected_return_code=0,
            expected_output=
'''abcdabcd0001   101 11+1 000100000000000000000000000000000000000000000001
                                                   abcd
'''
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_main_function(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].has_any_return_stmts()
        assert self.out_c.funcs['main'].has_return_stmts('return 0')

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%.*s')
        assert self.out_c.has_string_literal('%*s')
        assert self.out_c.has_string_literal('%.*d')
        assert self.out_c.has_string_literal('%*d')
        assert self.out_c.has_string_literal('%#o')
        assert self.out_c.has_string_literal('% d')
        assert self.out_c.has_string_literal('%-d')
        assert self.out_c.has_string_literal('%+d')
        assert self.out_c.has_string_literal('% .4d')
        assert self.out_c.has_string_literal('%-.44ho\\n')
        assert self.out_c.has_string_literal('%*.*s\\n')
        assert self.out_c.has_string_literal('abcd')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
