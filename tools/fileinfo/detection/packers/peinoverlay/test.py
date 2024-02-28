from regression_tests import *

class Test_PeInOverlay(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['pe-in-overlay32.exe_',
               'pe-in-overlay64.exe_'],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        desired_tool_recognized = True
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'packer' and tool['name'] == 'PE-in-Overlay':
                desired_tool_recognized = True
                break
        self.assertTrue(desired_tool_recognized)
