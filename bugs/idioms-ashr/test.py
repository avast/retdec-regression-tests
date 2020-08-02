#
# Created from https://github.com/avast/retdec/issues/724
# Author: adahsuzixin
#

from regression_tests import *

class TestBase(Test):
    def test_produce_expected_output(self):
        self.assert_c_produces_output_when_run(
            input='0xa5a5a5a5a5a50020',
            expected_output='getSecondByte( a5a5a5a5a5a50020 ) = 0\n',
            expected_return_code=0
        )

class Test_shiftOrDivide(TestBase):
    shiftOrDivide = TestSettings(
        input=files_in_dir('2020-08-02')
    )
