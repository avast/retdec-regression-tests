from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='unpacker',
        input='20e9ddcd5f3b1c82d60026196e2ab629',
        run_fileinfo=True
    )

    def test_fileinfo_runs_successfully_on_unpacked_file(self):
        assert self.unpacker.succeeded
        assert self.fileinfo.succeeded
