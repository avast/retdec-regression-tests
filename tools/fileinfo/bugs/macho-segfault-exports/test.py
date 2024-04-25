from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=files_in_dir('inputs')
    )

    def test_no_import_and_export_table(self):
        assert self.fileinfo.succeeded
        assert "symbolTable" not in self.fileinfo.output
