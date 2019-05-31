from regression_tests import *

class Test7ZipDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs')
    )

    def test_detected_autoit(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*7-Zip SFX')

class Test7ZipConsoleDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs-console')
    )

    def test_detected_autoit(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*7-Zip SFX.*console version')
