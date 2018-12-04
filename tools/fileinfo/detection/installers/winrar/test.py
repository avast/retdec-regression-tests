from regression_tests import *

class TestWinRARDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs')
    )

    def test_detected_winrar(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*WinRAR SFX')


class TestWinRARZipDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs-zip')
    )

    def test_detected_winrar(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*WinRAR SFX.*with ZIP payload')
