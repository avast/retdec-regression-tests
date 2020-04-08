from regression_tests import *

class Test_ActiveMark(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_activemark.dat',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertTrue(self.fileinfo.output['tools'][1]['name'] == 'ActiveMark')

