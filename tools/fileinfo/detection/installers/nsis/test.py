from regression_tests import *

class TestNSISDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='nsis249.exe'
    )

    def test_detected_nsis(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Nullsoft Install System \(2.49\)')


class TestNSISNoManifestDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='nsis-sig.exe'
    )

    def test_detected_nsis(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Nullsoft Install System \(2.26 - 2.28\)')
