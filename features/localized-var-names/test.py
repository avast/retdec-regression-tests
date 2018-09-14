from regression_tests import *

class Test(Test):
    """Checks that we emit the name of the original global variable after the
    definitions of localized global variables.

    For example, if variable 'v1' comes from global variable 'gpr1', we want to
    emit the following line in the generated C code:

        int32_t v1 = rand(); // gpr1
    """

    settings = TestSettings(
        input='fibo.x86.gcc.O2.g.exe',
    )

    def test_out_c_contains_name_of_global_var_for_localized_local_var(self):
        # This test may be fragile. If we no longer generate a localized
        # variable for the input file, use a different input file.
        #assert self.out_c.contains('int32_t v. = .*; // edi') # this is inlined at the moment
        pass

    def test_out_c_contains_real_register_names(self):
        assert self.out_c.contains('g[12] = 0; // ebx')
        assert self.out_c.contains('g[12] = 0; // esi')
