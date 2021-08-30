from regression_tests import *

class TestInvalidEntryPointWarning(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='invalid-ep.exe',
        args='--verbose --json'
    )

    def test_invalid_entry_point(self):
        assert self.fileinfo.succeeded
        assert "offset" not in self.fileinfo.output['entryPoint']

        self.assertEqual(self.fileinfo.output['loaderError']['description'], 'The position of the entry point is out of the image')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'EpOutsideSections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point is outside of mapped sections')

class TestNoInvalidEntryPointWarning(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='no-ep.o',
    )

    def test_no_entry_point(self):
        assert self.fileinfo.succeeded
        assert not self.fileinfo.output.contains(r'Warning: Invalid address of entry point.')
