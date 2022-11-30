from regression_tests import *

class dropped(Test):
    settings = TestSettings(
        input='dropped.ex',
        args='--backend-no-opts --select-functions entry_point'
    )

    def test_has_only_selected_function(self):
        assert self.out_c.has_just_funcs('entry_point')

    def test_for_delayed_functions(self):
        fnc = self.out_c.funcs['entry_point']
        assert fnc.calls( 'GetInputState' )
        assert fnc.calls( 'WSAStartup' )
        assert fnc.calls( 'PostThreadMessageA' )
        # assert fnc.calls( 'GetMessageA' )
        assert fnc.calls( 'Sleep' )
        # assert fnc.calls( 'CreateMutexA' )
        assert fnc.calls( 'GetCurrentThreadId' )
        # assert fnc.calls( 'OpenMutexA' )
        assert fnc.calls( 'GetTickCount' )
