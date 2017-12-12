from regression_tests import *

base_settings = TestSettings(
    tool='idaplugin',
    input='unp1b_good.out'
)

class Test_17_2_2015(Test):
    settings = TestSettings.from_settings(base_settings,
        args='--select 0x409640'
    )

    def test_has_only_selected_fnc(self):
        assert self.out_c.has_just_funcs('sub_409640')

    def test_sub_409640_properties(self):
        fnc = self.out_c.funcs['sub_409640']

        assert fnc.return_type.is_int(32)
        assert fnc.param_count == 1
        assert fnc.params['a1'].type.is_int(32)

        assert fnc.calls('CreateMutexW','GetLastError','HeapFree','sub_4094B0')

        # Check that GetLastError() call is compared with 183 and result stored to some variable.
        #
        assert self.out_c.contains('\=.*\(GetLastError\(\) \=\= 183\)')

    def test_switch_in_sub_409640(self):
        assert self.out_c.contains('switch \(GetLastError\(\)\)')
        assert self.out_c.contains('case 0:')
        assert self.out_c.contains('result = 0;')
        assert self.out_c.contains('case 2:')
        assert self.out_c.contains('result = 6;')
        assert self.out_c.contains('case 3:')
        assert self.out_c.contains('result = 6;')
        assert self.out_c.contains('case 5:')
        assert self.out_c.contains('result = 4;')
        assert self.out_c.contains('case 8:')
        assert self.out_c.contains('result = 3;')
        assert self.out_c.contains('case 87:')
        assert self.out_c.contains('result = 2;')

        assert self.out_c.contains('return result;')
