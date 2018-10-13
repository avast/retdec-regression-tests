from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='0',
            expected_return_code=0,
            expected_output=' 0 after 0 after 0 after 0 after 0 after 0 after 0 0 22 after before  0  after '
        )
        self.assert_c_produces_output_when_run(
            input='1',
            expected_return_code=0,
            expected_output=' 1 after 1 after 1 1after 1 1after 1 after 1 after1 22 after before  1  after '
        )
        self.assert_c_produces_output_when_run(
            input='4',
            expected_return_code=0,
            expected_output='4 0 after4after4after4after4after4after4 22 after before  4  after '
        )
        self.assert_c_produces_output_when_run(
            input='22',
            expected_return_code=0,
            expected_output='22 0 after22after22after22after22after22after 22 after before  22  after '
        )
        self.assert_c_produces_output_when_run(
            input='26',
            expected_return_code=0,
            expected_output='26 0 after26after26after26after26after26after26 22 after before  26  after '
        )
        self.assert_c_produces_output_when_run(
            input='30',
            expected_return_code=0,
            expected_output='30 0 after30after30after30after30after30after30 22 after before  30  after '
        )

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )

class Test_MSVC(Test):
    settings = TestSettings(
        input='switch-test-msvc-O0.ex',
    )

    def test_for_switches_in_function_411a90(self):
        assert self.out_c.contains('default: {')
        assert self.out_c.contains('case 20: {')
        assert self.out_c.contains('case 21: {')
        assert self.out_c.contains('case 22: {')
        assert self.out_c.contains('case 23: {')
        assert self.out_c.contains('case 24: {')
        assert self.out_c.contains('case 25: {')
        assert self.out_c.contains('case 28: {')

    def test_for_switches_in_function_411c90(self):
        assert self.out_c.contains('default: {')
        assert self.out_c.contains('case 0: {')
        assert self.out_c.contains('case 2: {')
        assert self.out_c.contains('case 3: {')
        assert self.out_c.contains('case 5: {')
        assert self.out_c.contains('case 8: {')
        assert self.out_c.contains('case 57: {')

    def test_for_strings(self):
        assert self.out_c.has_string_literal(' before ')
        assert self.out_c.has_string_literal(' after ')
        assert self.out_c.has_string_literal(' 0 ')
        assert self.out_c.has_string_literal(' 1 ')
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal(' 20 ')
        assert self.out_c.has_string_literal(' 21 ')
        assert self.out_c.has_string_literal(' 22 ')
        assert self.out_c.has_string_literal(' 23 ')
        assert self.out_c.has_string_literal(' 24 ')
        assert self.out_c.has_string_literal(' 25 ')
        assert self.out_c.has_string_literal(' 28 ')
        assert self.out_c.has_string_literal(' before jump table 2 ')
        assert self.out_c.has_string_literal(' break \\n')
        assert self.out_c.has_string_literal(' 0 \\n')
        assert self.out_c.has_string_literal(' 2, 3 \\n')
        assert self.out_c.has_string_literal(' 5 \\n')
        assert self.out_c.has_string_literal(' 8 \\n')
        assert self.out_c.has_string_literal(' 57 \\n')
        assert self.out_c.has_string_literal(' after jumpt table 2 ')
