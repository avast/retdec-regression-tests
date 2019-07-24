from regression_tests import *

class Test_Watcom1(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_watcom_001.dat',
            'sample_watcom_002.dat',
        ],
        args='--json'
    )

    def test_pe_linker(self):
        assert self.fileinfo.succeeded
        self.assertTrue((self.fileinfo.output['tools'][1]['name'] == 'Watcom') or (self.fileinfo.output['tools'][3]['name'] == 'Watcom'))
