from regression_tests import *


class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='c1ae78a9681fd2c6dac9501258ee8f69'
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['signer']['chain']) == 0

        # Malware - invalid signature
        assert first_sig['signatureVerified'] == False
        assert first_sig['warnings'][0] == "Signature digest doesn't match the file digest"

        assert len(first_sig['allCertificates']) == 5

        # all certs
        assert first_sig['allCertificates'][0]['sha256'] == "AB7036365C7154AA29C2C29F5D4191163B162A2225011357D56D07FFA7BC1F72"
        assert first_sig['allCertificates'][1]['sha256'] == "A2BDF61928644D5A0F5CCC93C9B339E600AD1AD05E4682D86C1477CE39997CFF"
        assert first_sig['allCertificates'][2]['sha256'] == "8815DFF787F21FA8106760CB89C5B4493F4BD45E2CE801D2A4FE1F61DEE0C039"
        assert first_sig['allCertificates'][3]['sha256'] == "1C1983300C10FB262C0B2304B7BE15AABA10AE356EBBBB177583DC44774EB080"
        assert first_sig['allCertificates'][4]['sha256'] == "647B6D0F5F2C7F079A5A19532C07018515CABF7E6B9FE54086DC8E6786463893"

        # Counter-sig chain
        counter_sig = first_sig['signer']['counterSigners'][0]
        assert counter_sig['chain'][0]['sha256'] == '8815DFF787F21FA8106760CB89C5B4493F4BD45E2CE801D2A4FE1F61DEE0C039'
        assert counter_sig['chain'][1]['sha256'] == '1C1983300C10FB262C0B2304B7BE15AABA10AE356EBBBB177583DC44774EB080'

        assert counter_sig['warnings'][0] == "Couldn't decrypt the digest"


class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='d4744d78e0b4c1f50bc081eff41b69d6'
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['signer']['chain']) == 0

        # Malware - invalid signature
        assert first_sig['signatureVerified'] == False
        assert first_sig['warnings'][0] == "Signature digest doesn't match the file digest"

        assert len(first_sig['allCertificates']) == 3

        assert first_sig['allCertificates'][0]['sha256'] == "CED5AB020125966499A067ABFB138434281BC5B00C90D5D74D31529FF5169BF2"
        assert first_sig['allCertificates'][1]['sha256'] == "931802145A1193CD0DC7D84F45530E166D29672A3C8A0B80A9EAA0A5023ACEC3"
        assert first_sig['allCertificates'][2]['sha256'] == "6CA93FE1705083A68C1C87326CA367972C89BB2765289A2A6E97B77668A19E80"

        counter_sig = first_sig['signer']['counterSigners'][0]

        assert len(counter_sig['chain']) == 1

        assert counter_sig['chain'][0]['sha256'] == 'CED5AB020125966499A067ABFB138434281BC5B00C90D5D74D31529FF5169BF2'
        assert counter_sig['warnings'][0] == "Failed to verify the counter-signature"

# https://github.com/avast/retdec/issues/255


class Test3(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '65BB4991028F627C5B832C5E9189118FF656F71481931BB98EB9F211FA4F6B5F',
            'DA9AC36A6A69CBE79D266AE695906296F8AABDE7713624D29553BC22508D9AC3'
        ]
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert first_sig['signatureVerified'] == False
        assert first_sig['warnings'][0] == "Couldn't get contentInfo"

        assert first_sig['allCertificates'][0]['sha256'] == "A2219C3E44EE3748EAE12E5AA6C961AF47C185E25A8E59AFFD8FCAED641286CD"

# https://github.com/avast/retdec/issues/250


class Test4(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='34722C26B5557979DE5B4DCAE01DD4D0CD1DC99AF78656D7DA93D3B6BB907C9A'
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded
        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['signer']['chain']) == 1

        # Malware - invalid signature
        assert first_sig['signatureVerified'] == False
        assert first_sig['warnings'][0] == "Signature digest doesn't match the file digest"

        assert len(first_sig['allCertificates']) == 3

        assert first_sig['allCertificates'][0]['sha256'] == "8815DFF787F21FA8106760CB89C5B4493F4BD45E2CE801D2A4FE1F61DEE0C039"
        assert first_sig['allCertificates'][1]['sha256'] == "1C1983300C10FB262C0B2304B7BE15AABA10AE356EBBBB177583DC44774EB080"
        assert first_sig['allCertificates'][2]['sha256'] == "F0A14C45793C834FA6B10891813FD27487315E98BF5423D30DCAA44B4B28CD04"
