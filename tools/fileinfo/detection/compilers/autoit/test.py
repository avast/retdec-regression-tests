from regression_tests import *

class TestAutoItDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs'),
        args='--json'
    )

    def test_detected_autoit(self):
        autoit_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'Aut2Exe':
                autoit_recognised = True
        self.assertTrue(autoit_recognised)
