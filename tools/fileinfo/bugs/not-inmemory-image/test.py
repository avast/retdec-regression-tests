from regression_tests import *

class Test000(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'FileTest_mpress219.ex',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        assert 'loaderError' not in self.fileinfo.output, 'unexpectedly found loader error'
