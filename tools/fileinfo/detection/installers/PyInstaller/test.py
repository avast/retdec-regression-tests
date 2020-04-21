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

class TestPyInstaller_3x(Test):
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
        assert self.fileinfo.output.contains(r'PyInstaller \(3.x\)')
