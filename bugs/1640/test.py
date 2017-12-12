from regression_tests import *

class Test(Test):
    """decfront generated invalid LLVM IR:

        error: use of undefined value '%loc_stack_ptr_store_0'

    This test ensures that this won't happen again.
    """

    settings=TestSettings(
        input='arm-macho-bc74879e25c3a19ae28a6d2370f6c9de'
    )

    def test_decompilation_succeeds(self):
        assert self.decomp.succeeded
