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
        linker_found = False
        for tool in self.fileinfo.output['tools']:
            if tool['name'] == 'Watcom':
                linker_found = True
                break
        self.assertTrue(linker_found)
