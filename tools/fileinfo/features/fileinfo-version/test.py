from regression_tests import *

class TestPlain(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose',
        input='file-32bit.ex_'
    )

    def test_fileinfo_version_string_present(self):
        self.assertRegex(self.fileinfo.output, r'RetDec Fileinfo version  : RetDec .* built on .*')

class TestJson(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input='file-32bit.ex_'
    )

    def test_fileinfo_version_info_present(self):
        self.assertTrue(self.fileinfo.output['fileinfoVersion']['commitHash'])
        self.assertTrue(self.fileinfo.output['fileinfoVersion']['versionTag'])
        self.assertTrue(self.fileinfo.output['fileinfoVersion']['buildDate'])