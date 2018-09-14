from regression_tests import *

class Test(Test):

    settings = TestSettings( input = 'bitcnt-1.bin' )

    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='255',
            expected_output='255 contains 8 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='256',
            expected_output='256 contains 1 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='1023',
            expected_output='1023 contains 10 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='556445',
            expected_output='556445 contains 12 bit set\n'
        )
        self.assert_c_produces_output_when_run(
            input='457785621',
            expected_output='457785621 contains 12 bit set\n'
        )

    def test_does_not_contain_unused_global_variables(self):
        # Function scanf() uses global variable _impure_ptr. This function is
        # not removed in the front-end. It is, however, removed in the
        # back-end, which removes statically linked library functions. This
        # removal causes _impure_ptr to become unused. The following test
        # ensures that it is not present in the decompiled code.
        assert not self.out_c.has_global_var('_impure_ptr')
