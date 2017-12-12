from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='da43008b2779c2a08740d4d3c792b1e4'
    )

    def test_fileinfo_detect_rich_header_with_suspicious_content(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['crc32'], '7e6b8a5a')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][11]['address'], '0x400228')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][11]['index'], '11')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][11]['size'], '0x20')
        self.assertEqual(self.fileinfo.output['dataDirectories']['dataDirectoryEntries'][11]['type'], 'Bound import table')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '3')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileClass'], '32-bit')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileStatus'], 'PE32')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['md5'], 'da43008b2779c2a08740d4d3c792b1e4')
        self.assertEqual(self.fileinfo.output['numberOfBitsInOneWord'], '32')
        self.assertEqual(self.fileinfo.output['sha256'], '495dc2343345eb31ceef0df860da27e0a0b382b59b0a9fcbe048c6591da91f58')
