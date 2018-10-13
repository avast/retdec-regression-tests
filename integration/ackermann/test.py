from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='0 0',
            expected_return_code=0,
            expected_output=
'''Naive:     3 (4 calls)
Iterative: 3 (2 calls)
Formula:   3 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='1 1',
            expected_return_code=0,
            expected_output=
'''Naive:     7 (27 calls)
Iterative: 7 (12 calls)
Formula:   7 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='2 2',
            expected_return_code=0,
            expected_output=
'''Naive:     61 (2432 calls)
Iterative: 61 (1188 calls)
Formula:   61 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='4 1',
            expected_return_code=0,
            expected_output=
'''Naive:     4 (6 calls)
Iterative: 4 (3 calls)
Formula:   4 (1 calls)
'''
        )
        self.assert_c_produces_output_when_run(
            input='6 2',
            expected_return_code=0,
            expected_output=
'''Naive:     61 (2432 calls)
Iterative: 61 (1188 calls)
Formula:   61 (1 calls)
'''
        )

class Test_2017(TestBase):
    settings_2017 = TestSettings(
        input=files_in_dir('2017-11-14'),
    )

class Test_2015(TestBase):
    settings_2015 = TestSettings(
        input=files_in_dir('2015-03-30'),
    )

# Decoder should not decode physical bytes with no virtual counterparts.
class Test_2015_Decoder(Test):
    settings = TestSettings(
        input = '2015-03-30/ackermann.x86.clang-3.2.O0.g.ex'
    )

    def test_decodes_only_valid_range(self):
        assert self.out_dsm.contains('0x407a69:   00 00 00 ff ff ff ff')
        assert not self.out_dsm.contains('0x407a73:   00 00                          \tadd byte [ eax ], al')
