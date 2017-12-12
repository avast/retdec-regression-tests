from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='5c6dd5fc0fef8736f8fd1bebab8f1c3e'
    )

    def test_has_imports_and_resources(self):
        assert self.fileinfo.succeeded
        self.assertEqual('51', self.fileinfo.output['importTable']['numberOfImports'])
        self.assertEqual('3', self.fileinfo.output['resourceTable']['numberOfResources'])
