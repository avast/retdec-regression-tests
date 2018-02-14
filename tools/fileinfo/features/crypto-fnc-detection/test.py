import os.path

from regression_tests import *

class CryptoCrcTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('inputs' + os.path.sep + 'crc')
    )

    def test_fileinfo_detect_crc_crypto_patterns(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['fileClass'], '32-bit')
        self.assertTrue(len(self.fileinfo.output['patterns']))
        self.assertTrue(self.fileinfo.output['patterns'][0]['endian'] == 'little' or self.fileinfo.output['patterns'][0]['endian'] == 'big')
        self.assertEqual(self.fileinfo.output['patterns'][0]['name'], 'CRC_32_IEEE_802_3_poly_0x04C11DB7')
        self.assertEqual(self.fileinfo.output['patterns'][0]['type'], 'crypto')
