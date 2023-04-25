from regression_tests import *

class TestMsSetupDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs')
    )

    def test_detected_ms_setup(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Microsoft Setup \(8\..*\)')
