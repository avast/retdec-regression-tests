from regression_tests import *

class Testx64MSVCDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ackermann.exe'
    )

    def test_detected_autoit(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'Microsoft Linker \(14\.1\)')
        assert self.fileinfo.output.contains(r'MSVC \(15\.0\) Visual Studio 2017')

