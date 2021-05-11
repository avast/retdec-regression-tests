from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='03ea764ead2c27b0a98c48a18d4cc8e831f3d9a7bf62a471c2d57ef81183cf80'
    )

    def test_output_does_not_contain_any_date(self):
        assert self.fileinfo.succeeded
        assert 'validSince' not in self.fileinfo.output['digitalSignatures'][
            'signatures'][0]['allCertificates'][0]['attributes']['subject']
        assert 'validUntil' not in self.fileinfo.output['digitalSignatures'][
            'signatures'][0]['allCertificates'][0]['attributes']['subject']
