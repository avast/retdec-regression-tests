from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='unpacker',
        input='x86-pe-4a66a6fea03ce7005bef7085a4e87e42',
        run_fileinfo=True
    )

    def test_certificate_directory(self):
        assert self.unpacker.succeeded
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 1

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]
        assert first_sig['digestAlgorithm'] == 'sha1'
        # Unpacked file -> different contents than original -> different hash -> invalid signature on the unpacked file
        assert first_sig['fileDigest'] == '3E8002A08AEB8A1AF564E26C84FD0352C1302FEA'
        assert first_sig['signedDigest'] == '79FBA75A396B6C8EB65D46C7B75065A75CA5148A'
        assert first_sig['warnings'][0] == "Signature digest doesn't match the file digest"

        assert len(first_sig['allCertificates']) == 4
        assert first_sig['allCertificates'][0]['sha256'] == "2CF1EC6AB594113BD538DF6D5C940E3319B424F8756D975888072C6AB558B771"
        assert first_sig['allCertificates'][1]['sha256'] == "2463525300D9E8E0A6F5D79E2B20B9F5182FE40D3FD7C85DDAF48E6C25BEDF5D"
        assert first_sig['allCertificates'][2]['sha256'] == "8EF8F2565BE30E7CE7BA6302BB18B42A3ACD148A0DDB4779E4C03E862F39589B"
        assert first_sig['allCertificates'][3]['sha256'] == "F63B42F1E0C3950730D95B3B6B78B8F7C7991097B5F8D81F64B2C83A1DECF5CA"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "6ACC465F78C739BD14942911C884D248A0C2687D"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert first_sig_countersig['signTime'] == "Oct  5 20:08:28 2013 GMT"
        assert first_sig_countersig['digest'] == 'E51C5443FA1C958B804E0B02A0AAF535091DFDDC'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'
        assert len(first_sig_countersig['chain']) == 2
