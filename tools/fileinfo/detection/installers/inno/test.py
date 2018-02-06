from regression_tests import *

class TestInnoSetupDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='inno.exe'
    )

    def test_detected_inno(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Inno Setup \(5.4.0 - 5.5.1\)')


