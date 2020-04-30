from regression_tests import *

class TestABTEDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='abte_uv_01',
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        abte_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'Advanced BAT to EXE Converter':
                abte_recognised = True
        self.assertTrue(abte_recognised)
