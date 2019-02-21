from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='test',
    )

    def test_quality(self):
        assert self.out_c.has_string_literal('/tmp/myfile')
        assert self.out_c.has_string_literal('malicious payload here\\n')

        fnc = self.out_c.funcs['_start']
        assert fnc.calls('open')
        assert fnc.calls('write')
        assert fnc.calls('exit')

    def test_garbage_not_present(self):
        """ If decoder does not terminate BB on sys_exit(), then
            garbage gets decoded.
            Test that there are no garbage function calls.
        """
        fnc = self.out_c.funcs['_start']
        assert not fnc.calls('__asm_insd')
        assert not fnc.calls('__asm_arpl')
        assert not fnc.calls('__asm_outsd')
        assert not fnc.calls('__readfsbyte')
        assert not fnc.calls('__writefsbyte')
