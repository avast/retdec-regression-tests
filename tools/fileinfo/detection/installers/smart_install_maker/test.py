from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'Setup_calc.exe_',
            'Setup_comp_ultra_410.exe_',
            'Setup_comp_max_502.exe_',
            'Setup_1_nouninst_none_504.exe_'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        installer_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'Smart Install Maker':
                installer_recognized = True
        self.assertTrue(installer_recognized)
