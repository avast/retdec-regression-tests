from regression_tests import *

class Test(Test):
    settings = CriticalTestSettings(
        input=['gpr0.x86.gcc.O0.g.elf', 'gpr0.x86.gcc.O0.g.exe'],
    )

    def test_c_produce_same_output_when_run(self):
        self.assert_c_produces_output_when_run(
            input='',
            expected_output='1\n',
            expected_return_code=0
        )
