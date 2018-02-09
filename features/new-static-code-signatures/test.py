from regression_tests import *


class TestNewARM32Signatures(Test):
    settings = TestSettings(
        input='arm.exe'
    )

    def test_check_correct_static_functions_detection(self):
        assert self.out_config.is_statically_linked('_raise_exc_ex', 0x40c328)
        #assert self.out_config.is_statically_linked('_set_statfp', 0x40c69c)
        assert self.out_config.is_statically_linked('ceil', 0x40b694)
        assert self.out_config.is_statically_linked('log10', 0x40b74c)
        assert self.out_config.is_statically_linked('memcmp', 0x401bdc)
        #assert self.out_config.is_statically_linked('memcpy', 0x4010e0)
        #assert self.out_config.is_statically_linked('memmove', 0x401320)
        assert self.out_config.is_statically_linked('memset', 0x401040)
        #assert self.out_config.is_statically_linked('raise', 0x408988)
        assert self.out_config.is_statically_linked('strchr', 0x40c7f8)
        #assert self.out_config.is_statically_linked('strlen', 0x404c60)
        assert self.out_config.is_statically_linked('strncpy_s', 0x40aee8)
        assert self.out_config.is_statically_linked('strrchr', 0x40c7c4)
        #assert self.out_config.is_statically_linked('wcslen', 0x406d84)
        assert self.out_config.is_statically_linked('__acrt_free_locale', 0x408410)
        #assert self.out_config.is_statically_linked('__acrt_is_packaged_app', 0x4054c0)
        assert self.out_config.is_statically_linked('__acrt_release_locale_ref', 0x408594)
        assert self.out_config.is_statically_linked('__acrt_set_locale_changed', 0x4045b4)
        assert self.out_config.is_statically_linked('__ascii_strnicmp', 0x40ba40)
        assert self.out_config.is_statically_linked('__get_machine_status', 0x40beb4)
        assert self.out_config.is_statically_linked('__setusermatherr', 0x403c34)
        assert self.out_config.is_statically_linked('__strncnt', 0x40b5dc)
        assert self.out_config.is_statically_linked('__vcrt_initialize_locks', 0x402678)
        assert self.out_config.is_statically_linked('__vcrt_initialize_ptd', 0x402604)
        assert self.out_config.is_statically_linked('__vcrt_initialize_pure_virtual_call_handler', 0x402704)
        assert self.out_config.is_statically_linked('_abstract_cw', 0x40bf5c)
        assert self.out_config.is_statically_linked('_abstract_sw', 0x40bff0)
        #assert self.out_config.is_statically_linked('_clrfp', 0x40c654)
        assert self.out_config.is_statically_linked('_ctrlfp', 0x40c674)
        assert self.out_config.is_statically_linked('_exception_enabled', 0x40c174)
        #assert self.out_config.is_statically_linked('_flushall', 0x405700)
        assert self.out_config.is_statically_linked('_free_base', 0x404b78)
        assert self.out_config.is_statically_linked('_get_printf_count_output', 0x406c54)
        #assert self.out_config.is_statically_linked('_handle_nan', 0x40c2f4)
        #assert self.out_config.is_statically_linked('_initterm', 0x40426c)
        assert self.out_config.is_statically_linked('_malloc_base', 0x404bb4)
        # TODO: Additional functions can be checked when #1759 feature is fixed.


class TestNewx86Signatures(Test):
    settings = TestSettings(
        input='x86.exe'
    )

    def test_check_correct_static_functions_detection(self):
        assert self.out_config.is_statically_linked('_strpbrk', 0x40cac0)
        assert self.out_config.is_statically_linked('_memset', 0x401d10)
        assert self.out_config.is_statically_linked('__sptype', 0x40f531)
        assert self.out_config.is_statically_linked('__set_exp', 0x40f502)
        #assert self.out_config.is_statically_linked('_fast_exit', 0x40e62e)
        assert self.out_config.is_statically_linked('__math_exit', 0x40e63b)
        #assert self.out_config.is_statically_linked('___stdio_common_vfprintf_p', 0x403918)
        assert self.out_config.is_statically_linked('__FindPESection', 0x40f640)
        # TODO: Additional functions can be checked when #1759 and #1760 features are fixed.
