from regression_tests import *

class TestBase(Test):
    def test_c_contains_for_or_while_loop(self):
        assert self.out_c.contains(r'(for|while) \(')

    def test_c_contains_no_gotos(self):
        assert not self.out_c.contains(r'goto .*;')

    def test_c_contains_all_strings(self):
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal('test')

class TestRunBase(TestBase):
    def test_c_produces_correct_output_when_run(self):
        self.assert_c_produces_output_when_run(
            input='3',
            expected_output='testtest',
            expected_return_code=0
        )

    def test_c_contains_just_main(self):
        assert self.out_c.has_just_funcs('main')

class Test_2018_x64Pe(TestBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', matching=r'.*\.exe'),
    )

class Test_2018(TestRunBase):
    settings_2018 = TestSettings(
        input=files_in_dir('2018-09-17', excluding=r'.*\.exe'),
    )

class Test_2017(TestRunBase):
    settings = TestSettings(
        input=files_in_dir('2017-11-14'),
    )
