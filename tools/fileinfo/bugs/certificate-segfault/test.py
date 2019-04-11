from regression_tests import *

class Test1(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='c1ae78a9681fd2c6dac9501258ee8f69'
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded
        assert 'signerCertificateIndex' not in self.fileinfo.output['certificateTable']
        self.assertEqual(self.fileinfo.output['certificateTable']['numberOfCertificates'], '2')
        self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][0]['sha256'], '8815dff787f21fa8106760cb89c5b4493f4bd45e2ce801d2a4fe1f61dee0c039')
        self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][1]['sha256'], '1c1983300c10fb262c0b2304b7be15aaba10ae356ebbbb177583dc44774eb080')


class Test2(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='d4744d78e0b4c1f50bc081eff41b69d6'
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded
        assert 'signerCertificateIndex' not in self.fileinfo.output['certificateTable']
        self.assertEqual(self.fileinfo.output['certificateTable']['numberOfCertificates'], '1')
        self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][0]['sha256'], 'ced5ab020125966499a067abfb138434281bc5b00c90d5d74d31529ff5169bf2')


# https://github.com/avast-tl/retdec/issues/255
class Test3(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '65BB4991028F627C5B832C5E9189118FF656F71481931BB98EB9F211FA4F6B5F',
            'DA9AC36A6A69CBE79D266AE695906296F8AABDE7713624D29553BC22508D9AC3'
        ]
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][0]['sha256'], 'a2219c3e44ee3748eae12e5aa6c961af47c185e25a8e59affd8fcaed641286cd')


# https://github.com/avast-tl/retdec/issues/250
class Test4(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='34722C26B5557979DE5B4DCAE01DD4D0CD1DC99AF78656D7DA93D3B6BB907C9A'
    )

    def test_certificate_table_present(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['certificateTable']['certificates'][0]['sha256'], 'f0a14c45793c834fa6b10891813fd27487315e98bf5423d30dcaa44b4b28cd04')
