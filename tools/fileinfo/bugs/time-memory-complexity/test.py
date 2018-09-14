from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='7af149ab9336bc7f2d33af2171ff034f'
    )

    def test_invalid_import_descriptor(self):
        assert self.fileinfo.succeeded
        assert "importTable" not in self.fileinfo.output
