from regression_tests import *

class TestWixDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs')
    )

    def test_detected_wix(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*WiX Toolset \(3\..*\)')
