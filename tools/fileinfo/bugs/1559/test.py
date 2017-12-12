from regression_tests import *

import os

class CryptoWallTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('inputs' + os.path.sep + 'cryptowall')
    )

    def test_fileinfo_detect_rich_header_with_suspicious_content(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['crc32'], '5937c664')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '6')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileStatus'], 'PE32')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['md5'], '50b965686ad2cbdc0066e870a928177e')
        self.assertEqual(self.fileinfo.output['numberOfBitsInOneWord'], '32')
        self.assertEqual(self.fileinfo.output['richHeader']['key'], '0xd256b6fe')
        self.assertEqual(self.fileinfo.output['richHeader']['offset'], '0x80')
        self.assertEqual(self.fileinfo.output['richHeader']['signature'], '00964fbd000000050084521e000000080095521e00000015008378090000006e0083521e00000005006dc62700000003007bc6270000000d00010000000000dc00847809000000360094521e000000010091780900000001')
        self.assertEqual(self.fileinfo.output['richHeader']['numberOfRecords'], '11')
        self.assertEqual(self.fileinfo.output['sha256'], '4ae64579fa0efd0be978c6797efe05d31517985b28ebd95dcadfacf3bb551f56')
        self.assertEqual(self.fileinfo.output['warnings'][0], 'Rich header contains suspicious content.')

class TeslaCryptTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('inputs' + os.path.sep + 'teslacrypt')
    )

    def test_fileinfo_detect_rich_header_with_invalid_key_but_analyse_rich_header(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['fileStatus'], 'PE32')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['numberOfBitsInOneWord'], '32')
        self.assertEqual(self.fileinfo.output['richHeader']['offset'], '0x80')
        self.assertEqual(self.fileinfo.output['richHeader']['numberOfRecords'], '8')
        self.assertEqual(self.fileinfo.output['warnings'][0], 'Rich header has invalid key.')
