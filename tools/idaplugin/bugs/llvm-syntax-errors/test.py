from regression_tests import *

class Test_564362585985abcb938c6022aa12f8f8(Test):
    settings = TestSettings(
        tool='idaplugin',
        input='564362585985abcb938c6022aa12f8f8'
    )

    # whatever test -- we just want to check if it decompiles OK.
    # I checked the binary with IDA, these functions are there and we should detect them.
    #
    def test_have_some_fncs(self):
        assert self.out_c.has_funcs('_main', 'sub_4019D0')

class Test_b6789310b7e04fd7da575d2db6fd8860(Test):
    settings = TestSettings(
        tool='idaplugin',
        input='b6789310b7e04fd7da575d2db6fd8860'
    )

    # whatever test -- we just want to check if it decompiles OK.
    # I checked the binary with IDA, these functions are there and we should detect them.
    #
    def test_have_some_fncs(self):
        assert self.out_c.has_funcs(
            '__sti___21_sfun_clusttopol_L_cpp_44b6780b',
            '_M_throw_length_error__Q2_9stlp_priv49_String_base__tm__29_cQ2_3std18allocator__tm__2_cCFv_v',
            '_M_append__Q2_3std78basic_string__tm__58_cQ2_3std20char_traits__tm__2_cQ2_3std18allocator__tm__2_cFPCZ1ZT1_RQ2_3std30basic_string__tm__10_Z1ZZ2ZZ3Z',
            '__dt__Q2_9stlp_priv56_STLP_alloc_proxy__tm__31_PccQ2_3std18allocator__tm__2_cFv')
