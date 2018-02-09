from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('inputs')
    )

    def test_fileinfo_json_output_correctly_parsed(self):
        self.assertIn('inputFile', self.fileinfo.output)
