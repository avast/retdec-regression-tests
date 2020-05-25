from regression_tests import *

class TestF2KODetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'f2ko_bat2exe_x86',
            'f2ko_bat2exe_x64',
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        f2ko_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'F2KO Bat2Exe':
                f2ko_recognised = True
        self.assertTrue(f2ko_recognised)
