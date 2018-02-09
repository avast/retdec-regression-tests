from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ca9998268d1038d448958a4430cd4641'
    )

    def test_fileinfo_succeeds(self):
        assert not self.fileinfo.succeeded
        assert self.fileinfo.output.contains(
            'Error: Failed to parse the input file \(it is probably'
            ' corrupted\). Detected format is: Mach-O.'
        )
