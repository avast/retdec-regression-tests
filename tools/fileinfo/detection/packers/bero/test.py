from regression_tests import *

class TestBeroDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('samples'),
        args='--json'
    )

    def test_detected_bero(self):
        bero_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'packer' and tool['name'] == 'BeRoEXEPacker':
                bero_recognised = True
        self.assertTrue(bero_recognised)
