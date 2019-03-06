from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='255',
            expected_return_code=0,
            expected_output='255 contains 8 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='256',
            expected_return_code=0,
            expected_output='256 contains 1 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='1023',
            expected_return_code=0,
            expected_output='1023 contains 10 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='556445',
            expected_return_code=0,
            expected_output='556445 contains 12 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='457785621',
            expected_return_code=0,
            expected_output='457785621 contains 12 bit set\n'
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2018_x64Pe(Test):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

    def test_check_function_bitcount(self):
        assert self.out_c.has_func('bitcount')
        assert self.out_c.funcs['bitcount'].return_type.is_int(32)
        assert self.out_c.funcs['bitcount'].param_count == 1
        assert self.out_c.funcs['bitcount'].params[0].type.is_int(32)

    def test_check_fucntion_main(self):
        assert self.out_c.has_funcs('main')
        assert self.out_c.funcs['main'].calls('scanf')
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].calls('bitcount')
        assert self.out_c.funcs['main'].has_any_while_loops()

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%ld contains %d bit set\\n')
        assert self.out_c.has_string_literal('%d')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
