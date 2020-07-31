from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='test.elf'
    )

    def test_check_function_have_no_args(self):
        assert self.out_c.has_func('foo')
        assert self.out_c.funcs['foo'].param_count == 0
        # TODO: currently RetDec returns int32_t for every
        # unkown type.
        # assert self.out_c.funcs['foo'].return_type.is_int(8)

        assert self.out_c.has_func('bar')
        assert self.out_c.funcs['bar'].param_count == 0
        # test.elf binary is 32 bit -> int is 32 bit.
        assert self.out_c.funcs['foo'].return_type.is_int(32)
