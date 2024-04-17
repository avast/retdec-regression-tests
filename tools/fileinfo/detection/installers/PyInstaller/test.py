from regression_tests import *

class TestPyInstaller_27(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['sample_pyinstaller_27_001.exe_',
               'sample_pyinstaller_27_002.exe_',
               'sample_pyinstaller_27_003.exe_']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'PyInstaller \(2.7\)')

class TestPyInstaller_30_38(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['sample_pyinstaller_35.exe_',
               'sample_pyinstaller_35_x64.exe_',
               'sample_pyinstaller_36.exe_',
               'sample_pyinstaller_36_x64.exe_',
               'sample_pyinstaller_37.exe_',
               'sample_pyinstaller_37_x64.exe_',
               'sample_pyinstaller_38.exe_',
               'sample_pyinstaller_38_x64.exe_']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'PyInstaller \(3.0-3.8\)')

class TestPyInstaller_39(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['sample_pyinstaller_39.exe_',
               'sample_pyinstaller_39_x64.exe_']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'PyInstaller \(3.9\)')

class TestPyInstaller_310_plus(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['sample_pyinstallerx_310.exe_',
               'sample_pyinstallerx_310_x64.exe_',
               'sample_pyinstallerx_311.exe_',
               'sample_pyinstallerx_311_x64.exe_']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'PyInstaller \(3.10\+\)')
