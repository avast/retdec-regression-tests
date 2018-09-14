from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='564ee59caad056d98ed274c8c4f06e82'
    )

    def test_fileinfo_succeeded(self):
        assert self.fileinfo.succeeded
        assert 'importTable' not in self.fileinfo.output
