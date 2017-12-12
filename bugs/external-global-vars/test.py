from regression_tests import *

class Test(Test):
    """The test checks that (1) we do not optimize user-defined global variables
    with external linkage, and (2) we remove global variables with no uses.

    The reason for (1) is that compilers do not optimize such global variables,
    and we should do the same. The reason for (2) is that we do not want unused
    variables to be present in the decompiled code.
    """

    settings = TestSettings(
        input='input.gcc.x86.g.exe',
    )

    def test_global_variable_is_not_optimized(self):
        assert self.out_c.has_global_var('g')
        assert self.out_c.contains(r'g = 1;')

    def test_there_are_no_other_global_variables(self):
        assert self.out_c.has_just_global_vars('g')
