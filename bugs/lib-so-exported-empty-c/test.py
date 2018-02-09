from regression_tests import *

class Test(Test):
    """Checks that exported functions in a Linux shared libraries (.so) are
    kept, even if they are unreachable.

    See #1387.
    """

    settings = TestSettings(
        input='lib.so'
    )

    def test_exported_functions_are_not_removed_even_if_unreachable(self):
        assert self.out_c.has_func('my_func')
