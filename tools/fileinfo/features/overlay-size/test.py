from regression_tests import *

class Test000(Test):
    settings=TestSettings(
        tool='fileinfo',
        input='sample-with-overlay-and-coff.dat',
        args='--json --verbose'
    )

    def test_overlay_size(self):
        assert self.fileinfo.succeeded
        assert 'loaderError' not in self.fileinfo.output, 'unexpectedly found loader error'
        self.assertEqual(self.fileinfo.output["overlay"]["offset"], '0xe2e00')
        self.assertEqual(self.fileinfo.output["overlay"]["size"], '0xbf28')
