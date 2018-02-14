import re

from regression_tests import *

class mips_elf_efbb701bea47201fffe8ecb4443f1ccc(Test):

    settings = TestSettings(
        input='mips-elf-efbb701bea47201fffe8ecb4443f1ccc',
        args='-k'
    )

    def test_for_some_functions(self):
        assert self.out_c.has_func( 'function_401420' )
        assert self.out_c.has_func( 'function_401440' )
        assert self.out_c.has_func( 'function_405488' )
        assert self.out_c.has_func( 'function_4054d8' )
        assert self.out_c.has_func( 'function_4054fc' )
        assert self.out_c.has_func( 'function_405670' )
        assert self.out_c.has_func( 'function_405818' )
        assert self.out_c.has_func( 'my_perl_destruct' )
        assert self.out_c.has_func( 'my_share_hek' )

    def test_for_some_dynamically_linked_function(self):
        expected_code_re = re.compile("""
                .*
                -\ Dynamically\ Linked\ Functions\ -
                .*
                boot_DynaLoader.*
                Perl_av_store.*
                Perl_free_tmps.*
                Perl_gv_stashpvn.*
                Perl_mg_set.*
                Perl_newSVpvn_flags.*
                Perl_PerlIO_stdout.*
                Perl_safesysmalloc.*
                Perl_share_hek.*
                Perl_sv_newmortal.*
                Perl_sv_setpvn.*
                Perl_sys_term.*
            """,
            flags=re.VERBOSE | re.DOTALL
        )
        assert self.out_c.contains(expected_code_re)

class x86_elf_8e2d7ac57bded5f52a6b5cd6d769da31(Test):

    settings = TestSettings(
        input='x86-elf-8e2d7ac57bded5f52a6b5cd6d769da31',
    )

    def test_for_all_functions(self):
        assert self.out_c.has_func( 'entry_point' )
        assert self.out_c.has_func( 'function_80480d4' )
        assert self.out_c.has_func( 'function_804831c' )
