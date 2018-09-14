
from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='66f3c6045a1c739fd8069c7ca838ce7a',
        args='-k'
    )

    #def test_check_for_all_currently_detected_strings(self):
        #assert self.out_c.has_string_literal('admin')
        #assert self.out_c.has_string_literal('1234')
        #assert self.out_c.has_string_literal('default')
        #assert self.out_c.has_string_literal('0.0')
        #assert self.out_c.has_string_literal('<%d>dlopen fail: %s\\n')
        #assert self.out_c.has_string_literal('libInit')
        #assert self.out_c.has_string_literal('<param><code value=\\"%d\\" /><port value=\\"%u\\" /></param>')
        #assert self.out_c.has_string_literal('check_dup_port:sendto')
        #assert self.out_c.has_string_literal('/dev/urandom')
        #assert self.out_c.has_string_literal('r')
        #assert self.out_c.has_string_literal('pnvplugin.so')

    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( 'function_4091e0' )
        assert self.out_c.has_func( 'function_4096bc' )
        assert self.out_c.has_func( 'bind_local_port' )
        assert self.out_c.has_func( 'main' )

    def test_check_that_empty_string_is_not_used_as_fnc_param(self):
        assert not self.out_c.contains( r'bzero\(""' )
        #assert not self.out_c.contains( r'strcpy\(""' )
