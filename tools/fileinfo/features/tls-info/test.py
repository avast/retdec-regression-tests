from regression_tests import *

# https://github.com/avast-tl/retdec/issues/417
# Test for proper TLS information parsing
class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='0c3031f630adc6cdd7b877fa1c2982909cde01dff612db5dd7df58cc778dd919',
        args='--verbose --json'
    )

    def test_info_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tlsInfo']['callbacksAddress'], '0x408044')
        self.assertEqual(self.fileinfo.output['tlsInfo']['characteristics'], '00000000000000000000000000000000')
        self.assertEqual(self.fileinfo.output['tlsInfo']['indexAddress'], '0x40803c')
        self.assertEqual(self.fileinfo.output['tlsInfo']['rawDataEndAddress'], '0')
        self.assertEqual(self.fileinfo.output['tlsInfo']['rawDataStartAddress'], '0')
        self.assertEqual(self.fileinfo.output['tlsInfo']['sizeOfZeroFill'], '0')

    def test_callbacks_parsed(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tlsInfo']['callbacks'][0], '0x401060')