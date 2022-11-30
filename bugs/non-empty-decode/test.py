from regression_tests import *

class arm_elf_509262418069137b2d989f0ac2d1460f(Test):
    settings = TestSettings(
        input='arm-elf-509262418069137b2d989f0ac2d1460f',
        args='-k'
    )

    # The following functions match the ones detected by IDA.
    #
    def test_check_for_currently_detected_functions(self):
        assert self.out_c.has_func( 'entry_point' )
        assert self.out_c.has_func( 'function_8818' )
        assert self.out_c.has_func( 'function_88bc' )
        assert self.out_c.has_func( 'function_88f0' )
        assert self.out_c.has_func( 'function_8914' )
        assert self.out_c.has_func( 'function_8948' )
        assert self.out_c.has_func( 'function_89b0' )
        assert self.out_c.has_func( 'function_8a84' )
        assert self.out_c.has_func( 'function_8b54' )
        assert self.out_c.has_func( 'function_8bcc' )
        assert self.out_c.has_func( 'function_8d9c' )
        assert self.out_c.has_func( 'function_8da4' )
        assert self.out_c.has_func( 'function_8dac' )
        assert self.out_c.has_func( 'function_8e34' )
        assert self.out_c.has_func( 'function_8ec4' )
        assert self.out_c.has_func( 'function_8f64' )
        assert self.out_c.has_func( 'function_8fd8' )
        assert self.out_c.has_func( 'function_90bc' )
        assert self.out_c.has_func( 'function_9124' )
        assert self.out_c.has_func( 'function_9170' )
        assert self.out_c.has_func( 'function_91c8' )
        assert self.out_c.has_func( 'function_925c' )
        assert self.out_c.has_func( 'function_93d4' )
        assert self.out_c.has_func( 'function_95e4' )
        assert self.out_c.has_func( 'function_95f8' )
        assert self.out_c.has_func( 'function_9cb0' )
        assert self.out_c.has_func( 'function_a078' )
        assert self.out_c.has_func( 'function_a08c' )
        assert self.out_c.has_func( 'function_a0a0' )
        assert self.out_c.has_func( 'function_a0e4' )
        assert self.out_c.has_func( 'function_a108' )
        assert self.out_c.has_func( 'function_a174' )
        assert self.out_c.has_func( 'function_a20c' )
        assert self.out_c.has_func( 'function_a988' )
        assert self.out_c.has_func( 'function_aa30' )
        assert self.out_c.has_func( 'function_aa60' )
        assert self.out_c.has_func( 'function_aa78' )
        assert self.out_c.has_func( 'function_ac4c' )
        assert self.out_c.has_func( 'function_acb8' )
        assert self.out_c.has_func( 'function_adcc' )
        #assert self.out_c.has_func( 'function_ae24' )
        assert self.out_c.has_func( 'function_ae68' )
        assert self.out_c.has_func( 'function_ae90' )
        assert self.out_c.has_func( 'function_aed4' )
        assert self.out_c.has_func( 'function_b2ac' )
        assert self.out_c.has_func( 'function_b60c' )
        assert self.out_c.has_func( 'function_b6b0' )
        assert self.out_c.has_func( 'function_b6cc' )
        assert self.out_c.has_func( 'function_b738' )
        assert self.out_c.has_func( 'function_b75c' )
        assert self.out_c.has_func( 'function_b77c' )
        assert self.out_c.has_func( 'function_b83c' )
        assert self.out_c.has_func( 'function_b850' )
        assert self.out_c.has_func( 'function_b858' )
        assert self.out_c.has_func( 'function_b860' )
        assert self.out_c.has_func( 'function_b868' )
        assert self.out_c.has_func( 'function_b870' )
        assert self.out_c.has_func( 'function_b878' )
        assert self.out_c.has_func( 'function_b880' )
        assert self.out_c.has_func( 'function_b8c4' )
        assert self.out_c.has_func( 'function_b908' )
        assert self.out_c.has_func( 'function_b91c' )
        assert self.out_c.has_func( 'function_b9e4' )
        assert self.out_c.has_func( 'function_ba3c' )

    def test_check_for_currently_detected_strings(self):
        assert self.out_c.has_string_literal( '[-]You Are PIG!' )

    def test_check_std_function_calls(self):
        fnc = self.out_c.funcs[ 'function_8818' ]
        assert fnc.calls( 'mprotect' )
        fnc = self.out_c.funcs[ 'function_89b0' ]
        # assert fnc.calls( 'mmap' )
        fnc = self.out_c.funcs[ 'function_8bcc' ]
        assert fnc.calls( 'memset' )
        fnc = self.out_c.funcs[ 'function_9170' ]
        assert fnc.calls( 'strcmp' )
        assert fnc.calls( 'strrchr' )
        fnc = self.out_c.funcs[ 'function_9cb0' ]
        #assert fnc.calls( 'munmap' )
        assert fnc.calls( 'putchar' )
        assert fnc.calls( 'puts' )
        #assert fnc.calls( 'function_86d4' )
        assert fnc.calls( 'strlen' )
        fnc = self.out_c.funcs[ 'function_a25c' ]
        assert fnc.calls( 'exit' )
        assert fnc.calls( 'free' )
        assert fnc.calls( 'malloc' )
        assert fnc.calls( 'memcpy' )
        # assert fnc.calls( 'srand48' )
        # assert fnc.calls( 'time' )
        fnc = self.out_c.funcs[ 'function_88f0' ]
        assert fnc.calls( 'munmap' )
        # jk: the C parser is unable to find dlopen on Windows
        #assert fnc.calls( 'dlopen' )
        fnc = self.out_c.funcs[ 'function_86d4' ]
        if not on_macos():
            assert fnc.calls( 'strlcpy' )

class p4_firmware_arm(Test):
    settings = TestSettings(
        input='p4_firmware_arm_axf',
        args='-k'
    )

    def test_for_all_functions(self):
        assert self.out_c.has_func( '__ARM_CortexM_Vector_Reset' )

class flash_o(Test):
    settings = TestSettings(
        input='flash.o'
    )

    def test_for_all_functions(self):
        assert self.out_c.has_func( 'halFlashEraseIsActive' )
        assert self.out_c.has_func( 'halInternalCibOptionByteWrite' )
        assert self.out_c.has_func( 'halInternalFlashErase' )
        assert self.out_c.has_func( 'halInternalFlashWrite' )
        assert self.out_c.has_func( 'verifyFib' )
