from regression_tests import *

class TestAHKDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'ahk_v_1_0_40_12',
            'ahk_v_1_0_7_x64',
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        ahk_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'AHK2Exe':
                ahk_recognised = True
        self.assertTrue(ahk_recognised)
