from regression_tests import *

class TestInnoSetupDetection_540(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='inno-5.4.0.exe_'
    )

    def test_detected_inno(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Inno Setup \(5.4.0 - 5.5.1\)')

class TestInnoSetupDetection_670(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='inno-6.7.0.exe_'
    )

    def test_detected_inno(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Inno Setup \(6.x\)')

class TestInnoSetupDetection_700(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='inno-7.0.0.exe_'
    )

    def test_detected_inno(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Inno Setup \(7.x\)')

class TestInnoUnistallerDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='inno-uninstall.exe_'
    )

    def test_detected_inno(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Inno Uninstaller')
