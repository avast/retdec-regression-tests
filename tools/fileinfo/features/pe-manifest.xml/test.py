from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('inputs')
    )

    def test_fileinfo_json_output_is_correctly_parsed(self):
        self.assertIn('inputFile', self.fileinfo.output)
        self.assertIn('manifest', self.fileinfo.output)
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
