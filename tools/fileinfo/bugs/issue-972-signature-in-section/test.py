from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='026ca63f4f1364726b32af8d6e628172dcffc36405c4e09a140bf422045c743b'
    )

    def issue_972_signatures_inside_(self):
        assert self.fileinfo.succeeded

        assert 'digitalSignatures' not in self.fileinfo.output
