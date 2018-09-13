from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='',
            expected_return_code=0,
            expected_output=
'''0 0
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 9
1 0
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
2 0
2 1
2 2
2 3
2 4
2 5
2 6
2 7
2 8
2 9
3 0
3 1
3 2
3 3
3 4
3 5
3 6
3 7
3 8
3 9
4 0
4 1
4 2
4 3
4 4
4 5
4 6
4 7
4 8
4 9
5 0
5 1
5 2
5 3
5 4
5 5
5 6
5 7
5 8
5 9
6 0
6 1
6 2
6 3
6 4
6 5
6 6
6 7
6 8
6 9
7 0
7 1
7 2
7 3
7 4
7 5
7 6
7 7
7 8
7 9
8 0
8 1
8 2
8 3
8 4
8 5
8 6
8 7
8 8
8 9
9 0
9 1
9 2
9 3
9 4
9 5
9 6
9 7
9 8
9 9
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

    def test_check_function_main(self):
        assert self.out_c.has_func('main')
        assert self.out_c.funcs['main'].has_any_for_loops()
        assert (self.out_c.funcs['main'].has_for_loops('for (uint64_t i = 0; i < 10; i++)')
                or self.out_c.funcs['main'].has_for_loops('for (uint64_t i = 0; i < (uint64_t)10; i++)'))
        assert (self.out_c.funcs['main'].has_for_loops('for (uint64_t j = 0; j < 10; j++)')
                or self.out_c.funcs['main'].has_for_loops('for (uint64_t j = 0; j < (uint64_t)10; j++)'))
        assert self.out_c.funcs['main'].calls('printf')

    def test_check_presence_of_literals(self):
        assert self.out_c.has_string_literal('%d %d\\n')

class Test_2017(TestBase):
    settings = TestSettings(
        input=files_in_dir('2017-11-14'),
    )
