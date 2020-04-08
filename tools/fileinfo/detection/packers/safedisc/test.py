from regression_tests import *

class Test_SafeDisc(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_safedisc_001.dat',
            'sample_safedisc_002.dat',
            'sample_safedisc_003.dat',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertIn('SafeDisc', [tool['name'] for tool in self.fileinfo.output['tools']])
