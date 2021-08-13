from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='c2ee13fd028448d80ed59b445fd647e2'
    )

    def test_certificates_are_present(self):
        assert self.fileinfo.succeeded

        assert 'digitalSignatures' not in self.fileinfo.output
