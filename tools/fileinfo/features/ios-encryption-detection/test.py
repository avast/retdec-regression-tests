from regression_tests import *

class TestMachoEncryptedPlain(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_encrypted',
        args='--verbose'
    )

    def setUp(self):
        assert self.fileinfo.succeeded

    def test_detect_encryption_message(self):
        assert self.fileinfo.output.contains(r'arm64')
        assert self.fileinfo.output.contains(r'armv7')
        assert self.fileinfo.output.contains(r'Warning: This file is encrypted \(encryption algorithm: 1, offset: 0x4000, size: 0xc000\)')
        assert self.fileinfo.output.contains(r'OS/ABI                                 : iOS')
        assert self.fileinfo.output.contains(r'OS/ABI version                         : 8\.0\.0')
