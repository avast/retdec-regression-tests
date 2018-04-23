from regression_tests import *

class TestDecodeAll(Test):
    settings = TestSettings(
        input='korean_f1f365e089fe6fcd7d101b4ffad77555',
        args='--select-ranges 0x804900f-0x804906a'
    )

    def test_check_for_selected_function(self):
        assert self.out_c.has_just_funcs( 'function_804900f' )

        assert self.out_c.has_comment_matching( '// Address range: 0x804900f - 0x804906a' )
        fnc = self.out_c.funcs['function_804900f']
        assert fnc.calls('function_804a271','function_8048fdf','atoi','__stack_chk_fail')

class TestDecodeOnly(Test):
    settings = TestSettings(
        input='korean_f1f365e089fe6fcd7d101b4ffad77555',
        args='--select-ranges 0x804900f-0x804906a --select-decode-only'
    )

    def test_check_for_selected_function(self):
        assert self.out_c.has_just_funcs( 'function_804900f' )

        assert self.out_c.has_comment_matching( '// Address range: 0x804900f - 0x804906a' )
        fnc = self.out_c.funcs['function_804900f']
        assert fnc.calls('function_804a271','function_8048fdf','atoi','__stack_chk_fail')

        # bug #1162
        assert not self.out_c.has_comment_matching( '// void' )
