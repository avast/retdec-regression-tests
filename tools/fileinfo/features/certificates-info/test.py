from regression_tests import *


class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='8b280f2b7788520de214fa8d6ea32a30ebb2a51038381448939530fd0f7dfc16',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 2

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['allCertificates']) == 5

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == 'F6B86E97AEB3E567F58901F799E18FC6F89CC92E'
        assert first_sig['signedDigest'] == 'F6B86E97AEB3E567F58901F799E18FC6F89CC92E'
        assert first_sig['programName'] == "Broadband Download, Thunder in a Flash!"

        assert first_sig['allCertificates'][0]['subject'] == "CN=Symantec Time Stamping Services CA - G2,O=Symantec Corporation,C=US"
        assert first_sig['allCertificates'][0]['issuer'] == "CN=Thawte Timestamping CA,OU=Thawte Certification,O=Thawte,L=Durbanville,ST=Western Cape,C=ZA"
        assert first_sig['allCertificates'][0]['serialNumber'] == "7E93EBFB7CC64E59EA4B9A77D406FC3B"
        assert first_sig['allCertificates'][0]['publicKeyAlgorithm'] == "rsaEncryption"
        assert first_sig['allCertificates'][0]['signatureAlgorithm'] == "sha1WithRSAEncryption"
        assert first_sig['allCertificates'][0]['validSince'] == "Dec 21 00:00:00 2012 GMT"
        assert first_sig['allCertificates'][0]['validUntil'] == "Dec 30 23:59:59 2020 GMT"
        assert first_sig['allCertificates'][0]['sha1'] == "6C07453FFDDA08B83707C09B82FB3D15F35336B1"
        assert first_sig['allCertificates'][0]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"
        assert first_sig['allCertificates'][0]['publicKey'] == (
            'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsayzSVRLl'
            'xwSCtgleZEiVypv3LgmxENza8K/LlBa+xTCdo5DASVDtKHiRfTot3vDdMwi17SUAAL3Te2/tLdEJGvNX0U70UTOQxJzF4KLabQry5kerHIbJk'
            '1xH7Ex3ftRYQJTpqr1SSwFeEWlL4nO55nn/oziVz89xpLcSvh7M+R5CvvwdYhBnP/FA1GZqtdsn5Nph2Upg4XCYBTEyMk7FNrAgfAfDXTekiK'
            'ryvf7dHwn5vdKG3+nw54trorqpuaqJxZ9YfeYcRG84lChS+Vd+uUOpyyfqmUg09iW6Mh8pU5IRP8Z4kQHkgvXaISAXWp4ZEXNYEZ+VMETfMV58cnBcQIDAQAB')

        attributes = first_sig['allCertificates'][0]['attributes']
        assert attributes['subject']['country'] == "US"
        assert attributes['subject']['organization'] == "Symantec Corporation"
        assert attributes['subject']['commonName'] == "Symantec Time Stamping Services CA - G2"
        assert attributes['issuer']['country'] == "ZA"
        assert attributes['issuer']['organization'] == "Thawte"
        assert attributes['issuer']['organizationalUnit'] == "Thawte Certification"
        assert attributes['issuer']['state'] == "Western Cape"
        assert attributes['issuer']['commonName'] == "Thawte Timestamping CA"
        assert attributes['issuer']['locality'] == "Durbanville"

        assert first_sig['allCertificates'][1]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig['allCertificates'][2]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"
        assert first_sig['allCertificates'][3]['sha256'] == "8FB47562286677514075BC38D1CFD2B73481D93CB3F9C23F9AC3E6414EF34A6F"
        assert first_sig['allCertificates'][4]['sha256'] == "582DC1D97A790EF04FE2567B1EC88C26B03BF6E99937CAE6A0B50397AD20BBF8"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "96D052BD1B13E983FC6FE41911F6B49CEB5961B9"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3
        assert first_sig_signer['chain'][0]['sha256'] == "8FB47562286677514075BC38D1CFD2B73481D93CB3F9C23F9AC3E6414EF34A6F"
        assert first_sig_signer['chain'][1]['sha256'] == "582DC1D97A790EF04FE2567B1EC88C26B03BF6E99937CAE6A0B50397AD20BBF8"
        assert first_sig_signer['chain'][2]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert len(first_sig_countersig['warnings']) == 0
        assert first_sig_countersig['signTime'] == "Jun 25 14:19:05 2016 GMT"
        assert first_sig_countersig['digest'] == '8F22E222461E03492E8D67948463100465B1B9D0'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(first_sig_countersig['chain']) == 2
        assert first_sig_countersig['chain'][0]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        second_sig = self.fileinfo.output['digitalSignatures']['signatures'][1]

        assert len(second_sig['warnings']) == 0
        assert second_sig['digestAlgorithm'] == 'sha256'
        assert second_sig['fileDigest'] == '9FC3902927BFEDA2A3F61D650B0D2CBEC6D84597989EA6244D4EF954C67CA0B3'
        assert second_sig['signedDigest'] == '9FC3902927BFEDA2A3F61D650B0D2CBEC6D84597989EA6244D4EF954C67CA0B3'
        assert second_sig['programName'] == "Broadband Download, Thunder in a Flash!"

        assert len(second_sig['allCertificates']) == 6

        assert second_sig['allCertificates'][0]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"
        assert second_sig['allCertificates'][1]['sha256'] == "8FB47562286677514075BC38D1CFD2B73481D93CB3F9C23F9AC3E6414EF34A6F"
        assert second_sig['allCertificates'][2]['sha256'] == "582DC1D97A790EF04FE2567B1EC88C26B03BF6E99937CAE6A0B50397AD20BBF8"
        assert second_sig['allCertificates'][3]['sha256'] == "43CE166BC567F9887D650A2E624473BE7A43A6F378ABE03CB32FA63F7ABB1E45"
        assert second_sig['allCertificates'][4]['sha256'] == "6B6C1E01F590F5AFC5FCF85CD0B9396884048659FC2C6D1170D68B045216C3FD"
        assert second_sig['allCertificates'][5]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        second_sig_signer = second_sig['signer']
        assert second_sig_signer['digest'] == "E421C1A7625B9CD410B64A0EBEA7D991EA1DBAC65A3404A227235E1C0AB781F1"
        assert second_sig_signer['digestAlgorithm'] == 'sha256'

        assert len(second_sig_signer['chain']) == 3
        assert second_sig_signer['chain'][0]['sha256'] == "8FB47562286677514075BC38D1CFD2B73481D93CB3F9C23F9AC3E6414EF34A6F"
        assert second_sig_signer['chain'][1]['sha256'] == "582DC1D97A790EF04FE2567B1EC88C26B03BF6E99937CAE6A0B50397AD20BBF8"
        assert second_sig_signer['chain'][2]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"

        second_sig_countersig = second_sig_signer['counterSigners'][0]
        assert len(second_sig_countersig['warnings']) == 0
        assert second_sig_countersig['signTime'] == "Jun 25 14:19:29 2016 GMT"
        assert second_sig_countersig['digest'] == 'B36785DD22C1E070DB8A198A16C81BD93FB87F4D5B6301ACB2656C23E4EF80F5'
        assert second_sig_countersig['digestAlgorithm'] == 'sha256'

        assert len(second_sig_countersig['chain']) == 3
        assert second_sig_countersig['chain'][0]['sha256'] == "43CE166BC567F9887D650A2E624473BE7A43A6F378ABE03CB32FA63F7ABB1E45"
        assert second_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"
        assert second_sig_countersig['chain'][2]['sha256'] == "6B6C1E01F590F5AFC5FCF85CD0B9396884048659FC2C6D1170D68B045216C3FD"


class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='avgcfgex.ex',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 2

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['allCertificates']) == 5

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == '3E7B33AB316770BD369BFADF5FB5354730C89991'
        assert first_sig['signedDigest'] == '3E7B33AB316770BD369BFADF5FB5354730C89991'

        assert first_sig['allCertificates'][0]['subject'] == "CN=Symantec Time Stamping Services CA - G2,O=Symantec Corporation,C=US"
        assert first_sig['allCertificates'][0]['issuer'] == "CN=Thawte Timestamping CA,OU=Thawte Certification,O=Thawte,L=Durbanville,ST=Western Cape,C=ZA"
        assert first_sig['allCertificates'][0]['serialNumber'] == "7E93EBFB7CC64E59EA4B9A77D406FC3B"
        assert first_sig['allCertificates'][0]['publicKeyAlgorithm'] == "rsaEncryption"
        assert first_sig['allCertificates'][0]['signatureAlgorithm'] == "sha1WithRSAEncryption"
        assert first_sig['allCertificates'][0]['validSince'] == "Dec 21 00:00:00 2012 GMT"
        assert first_sig['allCertificates'][0]['validUntil'] == "Dec 30 23:59:59 2020 GMT"
        assert first_sig['allCertificates'][0]['sha1'] == "6C07453FFDDA08B83707C09B82FB3D15F35336B1"
        assert first_sig['allCertificates'][0]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"
        assert first_sig['allCertificates'][0]['publicKey'] == (
            'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsayzSVRLl'
            'xwSCtgleZEiVypv3LgmxENza8K/LlBa+xTCdo5DASVDtKHiRfTot3vDdMwi17SUAAL3Te2/tLdEJGvNX0U70UTOQxJzF4KLabQry5kerHIbJk'
            '1xH7Ex3ftRYQJTpqr1SSwFeEWlL4nO55nn/oziVz89xpLcSvh7M+R5CvvwdYhBnP/FA1GZqtdsn5Nph2Upg4XCYBTEyMk7FNrAgfAfDXTekiK'
            'ryvf7dHwn5vdKG3+nw54trorqpuaqJxZ9YfeYcRG84lChS+Vd+uUOpyyfqmUg09iW6Mh8pU5IRP8Z4kQHkgvXaISAXWp4ZEXNYEZ+VMETfMV58cnBcQIDAQAB')

        attributes = first_sig['allCertificates'][0]['attributes']
        assert attributes['subject']['country'] == "US"
        assert attributes['subject']['organization'] == "Symantec Corporation"
        assert attributes['subject']['commonName'] == "Symantec Time Stamping Services CA - G2"
        assert attributes['issuer']['country'] == "ZA"
        assert attributes['issuer']['organization'] == "Thawte"
        assert attributes['issuer']['organizationalUnit'] == "Thawte Certification"
        assert attributes['issuer']['state'] == "Western Cape"
        assert attributes['issuer']['commonName'] == "Thawte Timestamping CA"
        assert attributes['issuer']['locality'] == "Durbanville"

        assert first_sig['allCertificates'][1]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig['allCertificates'][2]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"
        assert first_sig['allCertificates'][3]['sha256'] == "3B0ABE047D7E84F3BBD12B5E399BED55E4D7E9FCC3F629B8953A8C060EF6D746"
        assert first_sig['allCertificates'][4]['sha256'] == "0CFC19DB681B014BFE3F23CB3A78B67208B4E3D8D7B6A7B1807F7CD6ECB2A54E"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "229A2D7B4C8F2E8EC5B6943D0F0E53B9F59E33B5"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3
        assert first_sig_signer['chain'][0]['sha256'] == "3B0ABE047D7E84F3BBD12B5E399BED55E4D7E9FCC3F629B8953A8C060EF6D746"
        assert first_sig_signer['chain'][1]['sha256'] == "0CFC19DB681B014BFE3F23CB3A78B67208B4E3D8D7B6A7B1807F7CD6ECB2A54E"
        assert first_sig_signer['chain'][2]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert len(first_sig_countersig['warnings']) == 0
        assert first_sig_countersig['signTime'] == "Feb  1 14:02:52 2016 GMT"
        assert first_sig_countersig['digest'] == '0DAAC35A77C75EAEA723AE13E61C927F676080A2'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(first_sig_countersig['chain']) == 2
        assert first_sig_countersig['chain'][0]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        second_sig = self.fileinfo.output['digitalSignatures']['signatures'][1]

        assert len(second_sig['warnings']) == 0
        assert second_sig['digestAlgorithm'] == 'sha256'
        assert second_sig['fileDigest'] == '6BE0FA5AB9336DDCC6ACE35ED2BC9744860E80088F35E5D77AF254F246228CDE'
        assert second_sig['signedDigest'] == '6BE0FA5AB9336DDCC6ACE35ED2BC9744860E80088F35E5D77AF254F246228CDE'

        assert len(second_sig['allCertificates']) == 6

        assert second_sig['allCertificates'][0]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"
        assert second_sig['allCertificates'][1]['sha256'] == "3A0682AB7FB478BA82FD11CE4DB9B0ADEA55DA05558A0CF737453D51572163D0"
        assert second_sig['allCertificates'][2]['sha256'] == "0CFC19DB681B014BFE3F23CB3A78B67208B4E3D8D7B6A7B1807F7CD6ECB2A54E"
        assert second_sig['allCertificates'][3]['sha256'] == "43CE166BC567F9887D650A2E624473BE7A43A6F378ABE03CB32FA63F7ABB1E45"
        assert second_sig['allCertificates'][4]['sha256'] == "6B6C1E01F590F5AFC5FCF85CD0B9396884048659FC2C6D1170D68B045216C3FD"
        assert second_sig['allCertificates'][5]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        second_sig_signer = second_sig['signer']
        assert second_sig_signer['digest'] == "0183B70327A59E8006B666E908D798CCD309BC4C2FFFD10E551E040B9B1DC449"
        assert second_sig_signer['digestAlgorithm'] == 'sha256'

        assert len(second_sig_signer['chain']) == 3
        assert second_sig_signer['chain'][0]['sha256'] == "3A0682AB7FB478BA82FD11CE4DB9B0ADEA55DA05558A0CF737453D51572163D0"
        assert second_sig_signer['chain'][1]['sha256'] == "0CFC19DB681B014BFE3F23CB3A78B67208B4E3D8D7B6A7B1807F7CD6ECB2A54E"
        assert second_sig_signer['chain'][2]['sha256'] == "8420DFBE376F414BF4C0A81E6936D24CCC03F304835B86C7A39142FCA723A689"

        second_sig_countersig = second_sig_signer['counterSigners'][0]
        assert len(second_sig_countersig['warnings']) == 0
        assert second_sig_countersig['signTime'] == "Feb  1 14:02:54 2016 GMT"
        assert second_sig_countersig['digest'] == '1C5206936E053F3D79A046D0E359FB32926AA9D8C269812A80A188AE04DC3E34'
        assert second_sig_countersig['digestAlgorithm'] == 'sha256'

        assert len(second_sig_countersig['chain']) == 3
        assert second_sig_countersig['chain'][0]['sha256'] == "43CE166BC567F9887D650A2E624473BE7A43A6F378ABE03CB32FA63F7ABB1E45"
        assert second_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"
        assert second_sig_countersig['chain'][2]['sha256'] == "6B6C1E01F590F5AFC5FCF85CD0B9396884048659FC2C6D1170D68B045216C3FD"


class Test3(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='c339b87d932b3f86c298b1745db1a28b1214fb7635ba3805851ef8699290f9b8',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 2

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == '0C13D3C2B3C6F48FA3485B36E08AC822C579C1E0'
        assert first_sig['signedDigest'] == '0C13D3C2B3C6F48FA3485B36E08AC822C579C1E0'

        # 2 certificates are there indeed stored twice, confirmed with LIEF
        assert len(first_sig['allCertificates']) == 7
        assert first_sig['allCertificates'][0]['sha256'] == "FCB433D6D1AFBEC9E8F5447C2C0FA4AE7553986D5C2703BE82524BE608F35F61"
        assert first_sig['allCertificates'][1]['sha256'] == "53793CFC1B2B5096CC4EDBEC527ABC5CBC20470C788162D9E54C370D51625F4A"
        assert first_sig['allCertificates'][2]['sha256'] == "C766A9BEF2D4071C863A31AA4920E813B2D198608CB7B7CFE21143B836DF09EA"
        assert first_sig['allCertificates'][3]['sha256'] == "53793CFC1B2B5096CC4EDBEC527ABC5CBC20470C788162D9E54C370D51625F4A"
        assert first_sig['allCertificates'][4]['sha256'] == "C766A9BEF2D4071C863A31AA4920E813B2D198608CB7B7CFE21143B836DF09EA"
        assert first_sig['allCertificates'][5]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig['allCertificates'][6]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "AC1E29C0611678FA7E5B98A11106A1F9D69B224F"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3
        assert first_sig_signer['chain'][0]['sha256'] == "FCB433D6D1AFBEC9E8F5447C2C0FA4AE7553986D5C2703BE82524BE608F35F61"
        assert first_sig_signer['chain'][1]['sha256'] == "53793CFC1B2B5096CC4EDBEC527ABC5CBC20470C788162D9E54C370D51625F4A"
        assert first_sig_signer['chain'][2]['sha256'] == "C766A9BEF2D4071C863A31AA4920E813B2D198608CB7B7CFE21143B836DF09EA"

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert len(first_sig_countersig['warnings']) == 0
        assert first_sig_countersig['signTime'] == "Feb  1 15:47:14 2016 GMT"
        assert first_sig_countersig['digest'] == 'DE8E927CEC0175F4544CAFBBAC55D584DAE15C20'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(first_sig_countersig['chain']) == 2
        assert first_sig_countersig['chain'][0]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        second_sig = self.fileinfo.output['digitalSignatures']['signatures'][1]

        assert len(second_sig['warnings']) == 0
        assert second_sig['digestAlgorithm'] == 'sha256'
        assert second_sig['fileDigest'] == '838379A390118A6562F3E06BE818F5A6407FD7F4FEA9ADF4C36A8B6952B1336B'
        assert second_sig['signedDigest'] == '838379A390118A6562F3E06BE818F5A6407FD7F4FEA9ADF4C36A8B6952B1336B'

        assert len(second_sig['allCertificates']) == 8

        assert second_sig['allCertificates'][0]['sha256'] == "D09EDDF7DA800BCC3AC114852614124706D94EA473A98DB19BC4F4CB6AEE16A4"
        assert second_sig['allCertificates'][1]['sha256'] == "5E6D2F88F617DC8B809AEE712445A41B3CDE26AF874A221A9DC98EA1DC68E3D5"
        assert second_sig['allCertificates'][2]['sha256'] == "4F32D5DC00F715250ABCC486511E37F501A899DEB3BF7EA8ADBBD3AEF1C412DA"
        assert second_sig['allCertificates'][3]['sha256'] == "687FA451382278FFF0C8B11F8D43D576671C6EB2BCEAB413FB83D965D06D2FF2"
        assert second_sig['allCertificates'][4]['sha256'] == "52F0E1C4E58EC629291B60317F074671B85D7EA80D5B07273463534B32B40234"
        assert second_sig['allCertificates'][5]['sha256'] == "5E6D2F88F617DC8B809AEE712445A41B3CDE26AF874A221A9DC98EA1DC68E3D5"
        assert second_sig['allCertificates'][6]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert second_sig['allCertificates'][7]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        second_sig_signer = second_sig['signer']
        assert second_sig_signer['digest'] == "FB26A5FA064C2789EEE8560B4F8A82B7FE968B0D776CE02F52AA3BA11D8CB22C"
        assert second_sig_signer['digestAlgorithm'] == 'sha256'

        assert len(second_sig_signer['chain']) == 3
        assert second_sig_signer['chain'][0]['sha256'] == "D09EDDF7DA800BCC3AC114852614124706D94EA473A98DB19BC4F4CB6AEE16A4"
        assert second_sig_signer['chain'][1]['sha256'] == "5E6D2F88F617DC8B809AEE712445A41B3CDE26AF874A221A9DC98EA1DC68E3D5"
        assert second_sig_signer['chain'][2]['sha256'] == "52F0E1C4E58EC629291B60317F074671B85D7EA80D5B07273463534B32B40234"

        second_sig_countersig = second_sig_signer['counterSigners'][0]
        assert len(second_sig_countersig['warnings']) == 0
        assert second_sig_countersig['signTime'] == "Feb  1 15:47:15 2016 GMT"
        assert second_sig_countersig['digest'] == 'C361F36F13601CEAF01F3480C58F98660205981A'
        assert second_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(second_sig_countersig['chain']) == 2
        assert second_sig_countersig['chain'][0]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert second_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"


class Test4(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='c58e6118bbe12d2c56b2db014c4eb0d3fd32cde7bca1f32a2da8169be1301e23',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 1

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == 'F9D74771FD4A1A2233D266F1F73B53464328EE1E'
        assert first_sig['signedDigest'] == 'F9D74771FD4A1A2233D266F1F73B53464328EE1E'
        assert first_sig['programName'] == 'Alveo'

        assert len(first_sig['allCertificates']) == 5
        assert first_sig['allCertificates'][0]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"
        assert first_sig['allCertificates'][1]['sha256'] == "3A2FBE92891E57FE05D57087F48E730F17E5A5F53EF403D618E5B74D7A7E6ECB"
        assert first_sig['allCertificates'][2]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig['allCertificates'][3]['sha256'] == "973A41276FFD01E027A2AAD49E34C37846D3E976FF6A620B6712E33832041AA6"
        assert first_sig['allCertificates'][4]['sha256'] == "E2DBA399BE32992B74DF8A86CFD9886C2304CCC19DA8A9BE2B87809DA006379E"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "C2072238EB76B1C42F366FD72B85304A88AE5037"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3
        assert first_sig_signer['chain'][0]['sha256'] == "E2DBA399BE32992B74DF8A86CFD9886C2304CCC19DA8A9BE2B87809DA006379E"
        assert first_sig_signer['chain'][1]['sha256'] == "973A41276FFD01E027A2AAD49E34C37846D3E976FF6A620B6712E33832041AA6"
        assert first_sig_signer['chain'][2]['sha256'] == "3A2FBE92891E57FE05D57087F48E730F17E5A5F53EF403D618E5B74D7A7E6ECB"

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert len(first_sig_countersig['warnings']) == 0
        assert first_sig_countersig['signTime'] == "Jul  1 20:02:53 2016 GMT"
        assert first_sig_countersig['digest'] == 'BFFD2E4E2707EE7BF5EB9B1381F100771CCCCD45'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(first_sig_countersig['chain']) == 2
        assert first_sig_countersig['chain'][0]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"


class Test5(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='crashreporter.ex',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 1

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == '65901089C84EF122BE9397F508580A3EFC674D1D'
        assert first_sig['signedDigest'] == '65901089C84EF122BE9397F508580A3EFC674D1D'

        assert len(first_sig['allCertificates']) == 5
        assert first_sig['allCertificates'][0]['sha1'] == "0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43"
        assert first_sig['allCertificates'][1]['sha1'] == "92C1588E85AF2201CE7915E8538B492F605B80C6"
        assert first_sig['allCertificates'][2]['sha1'] == "50600FD631998451C8F75EF3F618E31FC74D1585"
        assert first_sig['allCertificates'][3]['sha1'] == "65439929B67973EB192D6FF243E6767ADF0834E4"
        assert first_sig['allCertificates'][4]['sha1'] == "6C07453FFDDA08B83707C09B82FB3D15F35336B1"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "21C4C8CCB2A4B1A878D8347D5F07B8BE4A44693E"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3
        assert first_sig_signer['chain'][0]['sha256'] == "1A73BF16814D061CF5930634FBBD8A55E53DF2A556469C48FDF2623DFEEEE8A8"
        assert first_sig_signer['chain'][1]['sha256'] == "51044706BD237B91B89B781337E6D62656C69F0FCFFBE8E43741367948127862"
        assert first_sig_signer['chain'][2]['sha256'] == "3E9099B5015E8F486C00BCEA9D111EE721FABA355A89BCF1DF69561E3DC6325C"

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert len(first_sig_countersig['warnings']) == 0
        assert first_sig_countersig['signTime'] == "Jan 24 02:14:31 2016 GMT"
        assert first_sig_countersig['digest'] == 'F5D8409366948F3B1185F0D7032759C5A1E2FAF5'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(first_sig_countersig['chain']) == 2
        assert first_sig_countersig['chain'][0]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert first_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"


class Test6(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='f77acb4e1523b882f5307864345e5f7d20a657a7f40863bd7ae41d2521703fec',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 2

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == 'A6BE6C062A26427A722571FD634838DD2FE3743D'
        assert first_sig['signedDigest'] == 'A6BE6C062A26427A722571FD634838DD2FE3743D'
        assert len(first_sig['warnings']) == 0
        assert len(first_sig['allCertificates']) == 7

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "5370C469214E0A599238F7FA851BD86E633FB4E2"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert first_sig_countersig['signTime'] == "Feb  1 14:55:04 2016 GMT"
        assert first_sig_countersig['digest'] == 'B49D4C25284D735D3DCD7B3BBCE6FDA6828F774E'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'
        assert len(first_sig_countersig['warnings']) == 0
        assert len(first_sig_countersig['chain']) == 2

        second_sig = self.fileinfo.output['digitalSignatures']['signatures'][1]

        assert len(second_sig['warnings']) == 0
        assert second_sig['digestAlgorithm'] == 'sha256'
        assert second_sig['fileDigest'] == '54227373068BB3F2721F0E9B849142F3B68FDDD43571A9327C3F9CA44420EEA8'
        assert second_sig['signedDigest'] == '54227373068BB3F2721F0E9B849142F3B68FDDD43571A9327C3F9CA44420EEA8'

        assert len(second_sig['allCertificates']) == 8
        assert second_sig['allCertificates'][0]['sha256'] == "D09EDDF7DA800BCC3AC114852614124706D94EA473A98DB19BC4F4CB6AEE16A4"
        assert second_sig['allCertificates'][1]['sha256'] == "5E6D2F88F617DC8B809AEE712445A41B3CDE26AF874A221A9DC98EA1DC68E3D5"
        assert second_sig['allCertificates'][2]['sha256'] == "4F32D5DC00F715250ABCC486511E37F501A899DEB3BF7EA8ADBBD3AEF1C412DA"
        assert second_sig['allCertificates'][3]['sha256'] == "687FA451382278FFF0C8B11F8D43D576671C6EB2BCEAB413FB83D965D06D2FF2"
        assert second_sig['allCertificates'][4]['sha256'] == "52F0E1C4E58EC629291B60317F074671B85D7EA80D5B07273463534B32B40234"
        assert second_sig['allCertificates'][5]['sha256'] == "5E6D2F88F617DC8B809AEE712445A41B3CDE26AF874A221A9DC98EA1DC68E3D5"
        assert second_sig['allCertificates'][6]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert second_sig['allCertificates'][7]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"

        second_sig_signer = second_sig['signer']
        assert second_sig_signer['digest'] == "400EAD9ABBA5A18062E513E78DB4E7535A81F2B250C9E35A50D158DFA82CFD45"
        assert second_sig_signer['digestAlgorithm'] == 'sha256'

        assert len(second_sig_signer['chain']) == 3
        assert second_sig_signer['chain'][0]['sha256'] == "D09EDDF7DA800BCC3AC114852614124706D94EA473A98DB19BC4F4CB6AEE16A4"
        assert second_sig_signer['chain'][1]['sha256'] == "5E6D2F88F617DC8B809AEE712445A41B3CDE26AF874A221A9DC98EA1DC68E3D5"
        assert second_sig_signer['chain'][2]['sha256'] == "52F0E1C4E58EC629291B60317F074671B85D7EA80D5B07273463534B32B40234"

        second_sig_countersig = second_sig_signer['counterSigners'][0]
        assert len(second_sig_countersig['warnings']) == 0
        assert second_sig_countersig['signTime'] == "Feb  1 14:55:06 2016 GMT"
        assert second_sig_countersig['digest'] == '46A76769C69B78945E9B12594F638A943017F26E'
        assert second_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(second_sig_countersig['chain']) == 2
        assert second_sig_countersig['chain'][0]['sha256'] == "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0"
        assert second_sig_countersig['chain'][1]['sha256'] == "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95"


class Test7(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='msenvmnu.dll',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 2

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == '798D33E74F6F28A62A336C61CF81AE0277F47516'
        assert first_sig['signedDigest'] == '798D33E74F6F28A62A336C61CF81AE0277F47516'
        assert first_sig['programName'] == 'msenvmnu.dll'

        assert len(first_sig['allCertificates']) == 4

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "BC70A3256BE34E5FBB8874E3E6D58664F3F27BE5"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 2

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert first_sig_countersig['signTime'] == "Jul  7 07:30:56 2015 GMT"
        assert first_sig_countersig['digest'] == '7F95DBB284EFE07428573201F47342592CA9E007'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'
        assert len(first_sig_countersig['warnings']) == 0
        assert len(first_sig_countersig['chain']) == 2

        second_sig = self.fileinfo.output['digitalSignatures']['signatures'][1]

        assert len(second_sig['warnings']) == 0
        assert second_sig['digestAlgorithm'] == 'sha256'
        assert second_sig['fileDigest'] == '5BFB3AB09F359E11D76D95640BACB3A6CD65F2EF0D1763DC47D0B7F7203D22B7'
        assert second_sig['signedDigest'] == '5BFB3AB09F359E11D76D95640BACB3A6CD65F2EF0D1763DC47D0B7F7203D22B7'
        assert first_sig['programName'] == 'msenvmnu.dll'

        assert len(second_sig['allCertificates']) == 2
        assert second_sig['allCertificates'][0]['sha1'] == "76DAF3E30F95B244CA4D6107E0243BB97F7DF965"
        assert second_sig['allCertificates'][1]['sha1'] == "F252E794FE438E35ACE6E53762C0A234A2C52135"

        second_sig_signer = second_sig['signer']
        assert second_sig_signer['digest'] == "2B80E8B619EDC847B62A8A58785C70830B10ACA6863FE30C590F5AE4034258E9"
        assert second_sig_signer['digestAlgorithm'] == 'sha256'
        assert len(second_sig_signer['chain']) == 2

        second_sig_countersig = second_sig_signer['counterSigners'][0]
        assert len(second_sig_countersig['warnings']) == 1
        assert second_sig_countersig['warnings'][0] == "Couldn't parse signature"


class Test8(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='PdfConv_32.dll',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 1

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == '714A802FB13B89160538890320E519F7A9260E84'
        assert first_sig['signedDigest'] == '714A802FB13B89160538890320E519F7A9260E84'

        assert len(first_sig['allCertificates']) == 4
        assert first_sig['allCertificates'][0]['sha1'] == "DF946A5E503015777FD22F46B5624ECD27BEE376"
        assert first_sig['allCertificates'][1]['sha1'] == "DF540F8FEDBA6454E039DD5E21B3B7C99E327B51"
        assert first_sig['allCertificates'][2]['sha1'] == "F5AD0BCC1AD56CD150725B1C866C30AD92EF21B0"
        assert first_sig['allCertificates'][3]['sha1'] == "B69E752BBE88B4458200A7C0F4F5B3CCE6F35B47"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "807D00A61C50095D308F33F29EDD644A06E5C514"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert len(first_sig_countersig['warnings']) == 0
        assert first_sig_countersig['signTime'] == "Aug 14 07:58:15 2015 GMT"
        assert first_sig_countersig['digest'] == 'FDD38655C08F04B887C4992656CD4F35DE6E6A07'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'

        assert len(first_sig_countersig['chain']) == 1
        assert first_sig_countersig['chain'][0]['sha256'] == "12F0A1DDF83D265B205B4F3BCA43B3FA89A748E9834EC24004774FD2FDE34073"


class Test9(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='thunderbird.ex',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 1

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == '0813562802948CCB60D288A84147671FBFC10CD4'
        assert first_sig['signedDigest'] == '0813562802948CCB60D288A84147671FBFC10CD4'

        assert len(first_sig['allCertificates']) == 5

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "A6549FE9A61275AD574F53D2A299138E534780E6"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert len(first_sig_countersig['warnings']) == 0
        assert first_sig_countersig['signTime'] == "Feb 11 22:09:49 2016 GMT"
        assert first_sig_countersig['digest'] == 'BEFD25FA1E19A6D90B1918D4E06E465FE3BC57E3'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'
        assert len(first_sig_countersig['chain']) == 2


class Test10(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='VSTST-FileConverter.ex',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 2

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == '427DC17A763807D2DEAD406DDFD3AAE93F5CE235'
        assert first_sig['signedDigest'] == '427DC17A763807D2DEAD406DDFD3AAE93F5CE235'
        assert first_sig['programName'] == 'VSTST-FileConverter.exe'
        assert len(first_sig['warnings']) == 0
        assert len(first_sig['allCertificates']) == 4
        assert first_sig['allCertificates'][0]['sha256'] == "E43F82BC40029F17DBB516613D1E1A96EC2940CE76E0A9CD5F53BA50175A8766"
        assert first_sig['allCertificates'][1]['sha256'] == "67C529AD57B2AEDD4D248993324270C7064D4F6BDAAF70044D772D05C56001A4"
        assert first_sig['allCertificates'][2]['sha256'] == "9CBF22FAE0DD53A7395556CE6154AA14A0D03360AA8C51CFEA05D1FD8819E043"
        assert first_sig['allCertificates'][3]['sha256'] == "4F987BBE4E0D1DCF48FCEFC9239AC6E62EE9DF38CAC2D32993B8533CD95C2E49"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "C66CA59AF0B63A5758EC97F74FA33C686DBD06D0"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 2

        first_sig_countersig = first_sig_signer['counterSigners'][0]
        assert first_sig_countersig['signTime'] == "Jul  7 07:34:43 2015 GMT"
        assert first_sig_countersig['digest'] == 'C29360ED776638FE506A2641A5F13A9975EA9945'
        assert first_sig_countersig['digestAlgorithm'] == 'sha1'
        assert len(first_sig_countersig['warnings']) == 0
        assert len(first_sig_countersig['chain']) == 2

        second_sig = self.fileinfo.output['digitalSignatures']['signatures'][1]

        assert len(second_sig['warnings']) == 0
        assert second_sig['digestAlgorithm'] == 'sha256'
        assert second_sig['fileDigest'] == '7E6B06384FF2B27537F0AC76E311C116434D02DBC735FAF113B6EFD6D629F74C'
        assert second_sig['signedDigest'] == '7E6B06384FF2B27537F0AC76E311C116434D02DBC735FAF113B6EFD6D629F74C'
        assert first_sig['programName'] == 'VSTST-FileConverter.exe'

        assert len(second_sig['allCertificates']) == 2
        assert second_sig['allCertificates'][0]['sha256'] == "BD3FCED7A02EA9A18CEBC0628AF487A2925960BE8A88A35609666FA7901987AA"
        assert second_sig['allCertificates'][1]['sha256'] == "56DA8722AFD94066FFE1E4595473A4854892B843A0827D53FB7D8F4AEED1E18B"

        second_sig_signer = second_sig['signer']
        assert second_sig_signer['digest'] == "61A1F261448BCD1CC8AB9F03DF0209951734455840B2B0C2CFB11FC1DB0C1A81"
        assert second_sig_signer['digestAlgorithm'] == 'sha256'
        assert len(second_sig_signer['chain']) == 2

        second_sig_countersig = second_sig_signer['counterSigners'][0]
        assert len(second_sig_countersig['warnings']) == 1
        assert second_sig_countersig['warnings'][0] == "Couldn't parse signature"


class TestEscaping(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='3708882e564ba289416f65cb4cb2b4de',
        args='--json --verbose'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded
        self.assertEqual(
            len(self.fileinfo.output["digitalSignatures"]["signatures"][0]['allCertificates']), 4)

        self.assertEqual(self.fileinfo.output["digitalSignatures"]['signatures'][0]['signer']['chain'][0]
                         ["sha256"], "9D5DC543A16E3B97AA12ABB6A09C9393C1F6778E475D95C81607335D5D19AF8B")
        self.assertEqual(self.fileinfo.output["digitalSignatures"]['signatures'][0]['signer']['chain'][1]
                         ["sha256"], "0D34394100E961CE4318DBA9B8DD38EBC25BB07AEF78FDA3FFF632685549BA0F")
        self.assertEqual(self.fileinfo.output["digitalSignatures"]['signatures'][0]['signer']['counterSigners'][0]['chain'][0]
                         ["sha256"], "0374881C9B74D31F28DC580B0F2B9D2B14A97CE31CBEC2A05AEB377DCDDCC2B0")
        self.assertEqual(self.fileinfo.output["digitalSignatures"]['signatures'][0]['signer']['counterSigners'][0]['chain'][1]
                         ["sha256"], "0625FEE1A80D7B897A9712249C2F55FF391D6661DBD8B87F9BE6F252D88CED95")

        self.assertEqual(self.fileinfo.output["digitalSignatures"]['signatures'][0]['signer']['chain'][0]
                         ["attributes"]["subject"]["locality"], R"M\xfcnchen")


class Test11(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='x86-pe-ff6717faf307cdc5ba2d07e320cb8e33'
    )

    def test_certificates(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 1

        first_sig = self.fileinfo.output['digitalSignatures']['signatures'][0]

        assert len(first_sig['warnings']) == 0
        assert first_sig['digestAlgorithm'] == 'sha1'
        assert first_sig['fileDigest'] == 'F48199821F5D51C334E00532FABB05E3F2D3D92C'
        assert first_sig['signedDigest'] == 'F48199821F5D51C334E00532FABB05E3F2D3D92C'

        assert len(first_sig['allCertificates']) == 3
        assert first_sig['allCertificates'][0]['sha1'] == "C5DAAAEAA82AAF90C2963CE7432E934A8DE17D51"
        assert first_sig['allCertificates'][1]['sha1'] == "7C4656C3061F7F4C0D67B319A855F60EBC11FC44"
        assert first_sig['allCertificates'][2]['sha1'] == "2796BAE63F1801E277261BA0D77770028F20EEE4"

        first_sig_signer = first_sig['signer']
        assert first_sig_signer['digest'] == "9C6BCEE73B8C669764AEDB8046C064C71C5B6A27"
        assert first_sig_signer['digestAlgorithm'] == 'sha1'

        assert len(first_sig_signer['chain']) == 3


class Test12(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='002720d5ed0df9fe550d52145a44268d24b6368c61065be070e3319b9a67b082',
        args='-j -v'
    )

    def test(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 2
        assert len(self.fileinfo.output['digitalSignatures']['signatures']) == 2

        first_signature = self.fileinfo.output['digitalSignatures']['signatures'][0]
        assert len(first_signature['warnings']) == 0
        assert len(first_signature['allCertificates']) == 6
        assert first_signature['fileDigest'] == 'D643405056A4A16042D47942A8C6A59524BDA64A'
        assert first_signature['fileDigest'] == first_signature['signedDigest']
        assert first_signature['digestAlgorithm'] == 'sha1'

        signer = first_signature['signer']
        assert len(signer['warnings']) == 0
        assert signer['digest'] == '2C39C585984D98957CA03802F8C255EE4359D8EE'
        assert signer['digestAlgorithm'] == 'sha1'
        assert len(signer['chain']) == 4
        assert len(signer['counterSigners']) == 1

        counter_signer = signer['counterSigners'][0]
        assert len(counter_signer['warnings']) == 0
        assert len(counter_signer['chain']) == 2
        assert counter_signer['signTime'] == 'Aug 21 14:53:13 2017 GMT'
        assert counter_signer['digest'] == '1530CD732860961182222E7C955AEF70BD0BA570'
        assert counter_signer['digestAlgorithm'] == 'sha1'

        #######################################################################
        second_signature = self.fileinfo.output['digitalSignatures']['signatures'][1]
        assert len(second_signature['warnings']) == 0
        assert len(first_signature['allCertificates']) == 6
        assert second_signature['fileDigest'] == '75CACDF5BE7BAEECB89C70BC01343FB7C9E8FD000CC191F08D2A996359D617FE'
        assert second_signature['fileDigest'] == second_signature['signedDigest']
        assert second_signature['digestAlgorithm'] == 'sha256'

        signer = second_signature['signer']
        assert len(signer['warnings']) == 0
        assert signer['digest'] == '018A36C7429C0058101D3F087E69E27824CC68FEC8A745B8AF59D5D225BBDB77'
        assert signer['digestAlgorithm'] == 'sha256'
        assert len(signer['chain']) == 4
        assert len(signer['counterSigners']) == 1

        counter_signer = signer['counterSigners'][0]
        assert len(counter_signer['warnings']) == 0
        assert len(counter_signer['chain']) == 2
        assert counter_signer['signTime'] == 'Aug 21 14:53:39 2017 GMT'
        assert counter_signer['digest'] == '32344850DE23CE4A6312A69CC355AC6D16968964'
        assert counter_signer['digestAlgorithm'] == 'sha1'


class TestProgramName(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='0059fb3f225c5784789622eeccb97197d591972851b63d59f5bd107ddfdb7a21',
        args='-j -v'
    )

    def test(self):
        assert self.fileinfo.succeeded

        assert self.fileinfo.output['digitalSignatures']['numberOfSignatures'] == 1

        first_signature = self.fileinfo.output['digitalSignatures']['signatures'][0]
        assert first_signature['programName'] == "GoTo Opener"
