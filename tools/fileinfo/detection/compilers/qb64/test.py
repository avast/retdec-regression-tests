from regression_tests import *

class TestDetection_QB64(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs'),
        args='--json'
    )

    def test_detected_autoit(self):
        qb64_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'QB64':
                qb64_recognized = True
        self.assertTrue(qb64_recognized)
