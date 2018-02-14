from regression_tests import *

class TestMachONotDetected(Test):
    settings=TestSettings(
        tool='fileinfo',
        input='java'
    )

    def test_no_macho_detection(self):
        assert self.fileinfo.failed
        assert self.fileinfo.output.contains(
            r"Error: File format of the input file is not supported."
        )

class TestMachODetectedButFailedWithDetection(Test):
    settings=TestSettings(
        tool='fileinfo',
        input='broken'
    )

    def test_no_macho_detection(self):
        assert self.fileinfo.failed
        assert self.fileinfo.output.contains(
            r"Error: Failed to parse the input file \(it is probably"
            " corrupted\). Detected format is: Mach-O."
        )
