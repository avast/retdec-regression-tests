from regression_tests import *

class Test(Test):
    """Checks that ExitProcess() is recognized as never-returning function.
    """

    settings = TestSettings(
        input='imports.ex'
    )

    def test_exit_process_is_recognized_as_never_returning_function(self):
        # Currently, there is no other way of checking this than searching for
        # the following pattern:
        #
        #     ExitProcess(0);
        #     // UNREACHABLE
        #
        assert self.out_c.contains(r'ExitProcess\(0\);\n\s*// UNREACHABLE')
