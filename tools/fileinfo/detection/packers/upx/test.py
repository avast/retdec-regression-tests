from regression_tests import *

class TestUPXLZMADetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('lzma')
    )

    def test_detected_upx(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*UPX \(3\..* \[LZMA\]\)')

class TestUPXNRV2BDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('nrv2b')
    )

    def test_detected_upx(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*UPX \(3\..* \[NRV2B\]\)')

class TestUPXNRV2DDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('nrv2d')
    )

    def test_detected_upx(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*UPX \(3\..* \[NRV2D\]\)')

class TestUPXNRV2EDetection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=files_in_dir('nrv2e')
    )

    def test_detected_upx(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*UPX \(3\..* \[NRV2E\]\)')