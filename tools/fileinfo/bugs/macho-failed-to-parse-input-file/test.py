from regression_tests import *

class TestMachONotDetected(Test):
    settings=TestSettings(
        tool='fileinfo',
        input='not-macho'
    )

    def test_no_macho_detection(self):
        assert self.fileinfo.failed
        assert self.fileinfo.output.contains(
            r"Error: File format of the input file is not supported."
        )

class TestMachODetected(Test):
    settings=TestSettings(
        tool='fileinfo',
        input='macho'
    )

    def test_macho_detection(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(
            r"File format\s+: Mach-O"
        )
