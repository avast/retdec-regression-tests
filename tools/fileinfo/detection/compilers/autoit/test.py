from regression_tests import *

class TestAutoItDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('inputs')
    )

    def test_detected_autoit(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Aut2Exe \(3\.3\..*\)')
        assert self.fileinfo.output.contains(r'.*AutoIt \(bytecode\)')
