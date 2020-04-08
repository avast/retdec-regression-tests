from regression_tests import *

class Test_RLPack(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_rlpack_001.dat',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'RLPack')
