from regression_tests import *

class TestUpxDetectionSegfault(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample.ex',
        args='--json'
    )

    # Ensures that PE files without sections do not crash fileinfo upon
    # execution.
    # See https://github.com/avast/retdec/issues/821
    def test_file_analysed_correctly(self):
        self.assertTrue(self.fileinfo.succeeded)
