from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='a 10 3.1415',
            expected_return_code=0,
            expected_output=
'''97 10 3.140000
3.140000 10 97
123 97 3.140000
1 2 3 0.000000
3 4 5 4.140000
5 6 7 8.280001
7 8 9 12.420000
9 10 11 16.560001
123 456

0
55
65

1
65
75

2
75
85

3
85
95

4
95
105

5
105
115

6
115
125

7
125
135

8
135
145

9
145
155
'''
        )

class Test_2017(TestBase):
    settings_2017 = CriticalTestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = CriticalTestSettings(
        input=files_in_dir('2015-03-30'),
    )
