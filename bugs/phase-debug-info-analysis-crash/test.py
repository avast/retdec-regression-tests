from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='tail.ex',
        pdb='tail.pdb',
        args='-k'
    )

    def test_check_for_some_random_strings(self):
        assert self.out_c.has_string_literal('r')
        # Issue #652
        #assert self.out_c.has_string_literal('Chyba: %s\\n')

    def test_has_all_named_functions(self):
        assert self.out_c.has_func('printError')
        assert self.out_c.has_func('getParams')
        #assert self.out_c.has_func('mainCRTStartup')
        assert self.out_c.has_func('_setargv')
        assert self.out_c.has_func('NtCurrentTeb')
        #assert self.out_c.has_func('_RTC_Shutdown')
        #assert self.out_c.has_func('_RTC_SetErrorFuncW')
        #assert self.out_c.has_func('_RTC_SetErrorFunc')
        assert self.out_c.has_func('_RTC_NumErrors')
        assert self.out_c.has_func('_RTC_GetErrorFuncW')
        assert self.out_c.has_func('_RTC_GetErrorFunc')
        #assert self.out_c.has_func('_RTC_GetErrDesc')
        assert self.out_c.has_func('_matherr')
        assert self.out_c.has_func('__XcptFilter')
        assert self.out_c.has_func('__security_check_cookie')
        assert self.out_c.has_func('__lock')
        assert self.out_c.has_func('__initterm_e')
        assert self.out_c.has_func('__initterm')
        #assert self.out_c.has_func('__exit')
        assert self.out_c.has_func('__except_handler4_common')
        #assert self.out_c.has_func('__CxxSetUnhandledExceptionFilter')
        assert self.out_c.has_func('__CRT_RTC_INITW')
        #assert self.out_c.has_func('__configthreadlocale')
        assert self.out_c.has_func('__amsg_exit')
        #assert self.out_c.has_func('___setusermatherr')
        #assert self.out_c.has_func('___set_app_type')

    def test_has_some_random_imported_functions(self):
        assert self.out_c.contains(r'int32_t \(\*__dllonexit\(int32_t.*\);')
        assert self.out_c.contains(r'void __set_app_type\(int32_t a1\);')

    def test_declared_fnc_signatures_added_by_1628(self):
        assert self.out_c.contains(r'.*void _?_RTC_CheckStackVars\(char.*, int32_t.*\);')
        # the problem is that when we do not remove unreachable BBs, this fnc is called from
        # without params from call table -- we should not considered such calls, but we have
        # no way to detect it is the case.
        #assert self.out_c.contains(r'.*void _CrtSetCheckCount\(int32_t.*\);')
