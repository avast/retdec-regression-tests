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

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
