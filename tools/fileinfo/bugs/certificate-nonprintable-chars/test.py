from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--verbose',
        input='03ea764ead2c27b0a98c48a18d4cc8e831f3d9a7bf62a471c2d57ef81183cf80'
    )

    def test_output_contains_subject_with_escaped_nonprintable_chars(self):
        assert self.fileinfo.succeeded
        self.fileinfo.output.contains('Subject name        : Microsoft Windows 20\\x00\\x00 Publisher')
