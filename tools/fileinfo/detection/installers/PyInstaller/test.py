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
               'sample_pyinstaller_38_x64.exe_',
               'sample_pyinstaller_39.exe_',
               'sample_pyinstaller_39_x64.exe_',
               'sample_pyinstallerx_310.exe_',
               'sample_pyinstallerx_310_x64.exe_',
               'sample_pyinstallerx_311.exe_',
               'sample_pyinstallerx_311_x64.exe_']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'PyInstaller \(3.x\)')

class TestPyInstaller_3x_no_data(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['c58ef748edbbc86dcf2790f9f75ec244393732965103ef5caaa1627bcb52a2aa',
               '4c4067fd7a1e901207760b9e7b89ba959868368a42c4ca792b90ab9c31180fe5']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'PyInstaller \(no data\) \(3.x\)')

class TestPyInstaller_3x_corrupt(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['d5eebf39ea2e58315f140b1d8ac786ac53f4d6b5415c757d8a935a3effd3b0d8',
               'd8d38c6c50d295eeae0b3e1be5a81e43d935d96343e8f6ea376f6729bf55a3cc']
    )

    def test_detected_pyinstaller(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'PyInstaller \(corrupt\) \(3.x\)')
