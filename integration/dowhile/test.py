from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='3',
            expected_return_code=10,
            expected_output='Read 3\nReturn 10\n'
        )
        self.assert_c_produces_output_when_run(
            input='0',
            expected_return_code=3,
            expected_output='Read 0\nReturn 3\n'
        )
        self.assert_c_produces_output_when_run(
            input='2',
            expected_return_code=1,
            expected_output='Read 2\nReturn 1\n'
        )
        self.assert_c_produces_output_when_run(
            input='4',
            expected_return_code=10,
            expected_output='Read 4\nReturn 10\n'
        )

class Test_2018(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17'),
    )

class Test_2018_x64Pe(Test):
    settings = TestSettings( input=['2018-10-01-win/dowhile.x64.clang.O0.g.exe', '2018-10-01-win/dowhile.x64.gcc.O0.g.exe'] )

    def test_check_function_main(self):
        assert self.out_c.contains('printf\("Read %d\\\\n", .*\);')
        assert self.out_c.contains('printf\("Return %d\\\\n", .*\);')

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )
