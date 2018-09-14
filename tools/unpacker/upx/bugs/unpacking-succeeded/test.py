from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='unpacker',
        input=files_in_dir('inputs'),
        run_fileinfo=True
    )

    def test_unpacker_succeeded_no_imports(self):
        assert self.unpacker.succeeded
        assert self.fileinfo.succeeded
        assert "importTable" not in self.fileinfo.output
