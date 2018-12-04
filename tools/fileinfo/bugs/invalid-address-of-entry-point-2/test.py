from regression_tests import *

class TestInvalidEntryPointWarning(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='invalid-ep.exe',
    )

    def test_invalid_entry_point(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'Warning: Invalid address of entry point.')

class TestNoInvalidEntryPointWarning(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='no-ep.o',
    )

    def test_no_entry_point(self):
        assert self.fileinfo.succeeded
        assert not self.fileinfo.output.contains(r'Warning: Invalid address of entry point.')
