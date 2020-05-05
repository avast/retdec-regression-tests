from regression_tests import *

class TestExeScriptDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='exescript_uv_01',
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        exescript_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'ExeScript':
                exescript_recognised = True
        self.assertTrue(exescript_recognised)
