from regression_tests import *

class Test(Test):
    """Check that we emit 'char' instead of 'int8_t'.
    """
    settings = TestSettings(
        input='test.x86.gcc.O0.elf',
    )

    def test_type_of_print_param_is_char_star(self):
        assert self.out_c.funcs['print'].params[0].type.is_pointer()
        assert self.out_c.funcs['print'].params[0].type.pointed_type.is_char()
