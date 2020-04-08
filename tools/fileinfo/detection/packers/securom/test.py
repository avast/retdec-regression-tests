from regression_tests import *

class Test_SecuROM(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_securom_001.dat',
            'sample_securom_002.dat',
            'sample_securom_003.dat',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'SecuROM')
