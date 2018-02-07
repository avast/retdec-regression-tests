from regression_tests import *

class TestGcGoDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='gc-pe-x86.exe'
    )

    def test_detected_autoit(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'gc \(compiler\)')
        assert self.fileinfo.output.contains(r'Original language.*Go')

class TestGccGoDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='gccgo-elf-x64'
    )

    def test_detected_autoit(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'gccgo \(compiler\)')
        assert self.fileinfo.output.contains(r'Original language.*Go')
