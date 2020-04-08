from regression_tests import *

class Test_StarForce(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_starforce_001.dat',
            'sample_starforce_002.dat',
            'sample_starforce_003.dat',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertTrue('StarForce' in self.fileinfo.output['tools'][0]['name'])
