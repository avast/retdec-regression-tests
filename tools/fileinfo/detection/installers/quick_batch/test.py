from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'qb2160.exe_',
            'qb3200b.exe_',
            'qb3610_noembed.exe_',
            'scr311.exe_'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        desired_tool_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'Quick Batch File Compiler':
                desired_tool_recognized = True
        self.assertTrue(desired_tool_recognized)
