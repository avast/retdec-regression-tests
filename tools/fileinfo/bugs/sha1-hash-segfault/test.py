from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='08A2437BFE40329F132CD98CA1988CB13B0F32E8CE57FEBDD3CA0A6B641219D4.dat'
    )

    def test_has_certificate_table(self):
        assert self.fileinfo.succeeded
        assert 'certificateTable' in self.fileinfo.output
        self.assertEqual(5, len(
            self.fileinfo.output['certificateTable']['signatures'][0]['allCertificates']))

        self.assertEqual('CN=Microsoft Corporation,O=Microsoft Corporation,L=Redmond,ST=Washington,C=US',
                         self.fileinfo.output['certificateTable']['signatures'][0]['signer']['chain'][0]['subject'])
