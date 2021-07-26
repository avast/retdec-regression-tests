from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='026ca63f4f1364726b32af8d6e628172dcffc36405c4e09a140bf422045c743b'
    )

    def issue_972_signatures_inside_(self):
        assert self.fileinfo.succeeded

        sigs = self.fileinfo.output['invalidSignatures']

        assert sigs["numberOfSignatures"] == 2

        first_sig = sigs['signatures'][0]
        assert len(first_sig['allCertificates']) == 4
        assert first_sig['warnings'][0] == "Signature digest doesn't match the file digest"
        assert first_sig['fileDigest'] == "2E5F57F9449FF69D4936CC297442E271A7BA4D1C"
        assert first_sig['signedDigest'] == "5C14701C4D368146F53DF573451546D00F0608D6"

        assert first_sig['allCertificates'][0]['sha256'] == "AF840CA2B9DFB776BF81AA94C401BC440C52E5C590C43607A13D6680D83E3349"
        assert first_sig['allCertificates'][1]['sha256'] == "BA215596C19AEC4E1D25D32D284474D6F824228B74621738F6EE2CE603C9EF2F"
        assert first_sig['allCertificates'][2]['sha256'] == "34BB219C2589B1D7658503E1246B013606D00F6B00310E7A4087EA2098832596"
        assert first_sig['allCertificates'][3]['sha256'] == "425E72C87FF22855D9908B71AB4C64B0D2F248287097690C62FE733F631DE38F"