from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='79346D1FF291AF6C61DE41558EBEED0AF1EAB22DD9D773B9C028FF3A95A6B029.dat'
    )

    def test_attributes_are_empty_but_present(self):
        assert self.fileinfo.succeeded
        self.assertEqual(len(self.fileinfo.output['digitalSignatures'][
            'signatures'][0]['allCertificates'][0]['attributes']['issuer']), 0)
        self.assertEqual(len(
            self.fileinfo.output['digitalSignatures'][
                'signatures'][0]['allCertificates'][0]['attributes']['subject']), 0)
