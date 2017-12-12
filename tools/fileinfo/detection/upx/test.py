from regression_tests import *

class Upx121Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='UPX121_C_small.7'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'PE')
        self.assertEqual(self.fileinfo.output['Detected tool'][0], 'UPX (1.21 [NRV2B] [Filter: 0x26, Param: 0x7]) (packer), strings heuristic')

class UpxWithoutVersionTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--verbose',
        input='881044e62cdcee9f9e123ad1a8f0d602_edited'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'PE')
        self.assertEqual(self.fileinfo.output['Detected tool'][0], 'UPX ([LZMA] [Filter: 0x26, Param: 0x22]) (packer), strings heuristic')
        self.assertEqual(self.fileinfo.output['Declared number of sections'], '1')
