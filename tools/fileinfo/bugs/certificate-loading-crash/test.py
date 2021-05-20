from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='c2ee13fd028448d80ed59b445fd647e2'
    )

    def test_certificates_are_present(self):
        assert self.fileinfo.succeeded

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['allCertificates']) == 4
        assert first_sig['warnings'][0] == "Signature digest doesn't match the file digest"

        # test all certificates, there are 2 more than in Signer chain, because they
        # are probably from TimeStamp counter signature that is unparsable
        assert first_sig['allCertificates'][0]['sha256'] == "A2BDF61928644D5A0F5CCC93C9B339E600AD1AD05E4682D86C1477CE39997CFF"
        assert first_sig['allCertificates'][1]['sha256'] == "8815DFF787F21FA8106760CB89C5B4493F4BD45E2CE801D2A4FE1F61DEE0C039"
        assert first_sig['allCertificates'][2]['sha256'] == "AA03C799E7AFAC2858B79ED9710A63191032CC4099CEC75653064B8FACBD09A1"
        assert first_sig['allCertificates'][3]['sha256'] == "1C1983300C10FB262C0B2304B7BE15AABA10AE356EBBBB177583DC44774EB080"

        signer = first_sig['signer']
        # test just the signer chain
        assert signer['chain'][0]['sha256'] == "AA03C799E7AFAC2858B79ED9710A63191032CC4099CEC75653064B8FACBD09A1"
        assert signer['chain'][1]['sha256'] == "A2BDF61928644D5A0F5CCC93C9B339E600AD1AD05E4682D86C1477CE39997CFF"
