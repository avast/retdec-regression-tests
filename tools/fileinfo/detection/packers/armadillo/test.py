from regression_tests import *

class Test_Armadillo(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_armadillo_250.exe',
            'sample_armadillo_640.exe',
            'sample_armadillo_640_64bit.exe',
            'sample_armadillo_700.exe',
            'sample_armadillo_700_64bit.exe',
            'sample_armadillo_800.exe',
            'sample_armadillo_800_64bit.exe',
            'sample_armadillo_900.exe',
            'sample_armadillo_900_64bit.exe',
            'sample_armadillo_964.exe',
            'sample_armadillo_964_64bit.exe',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertTrue(self.fileinfo.output['tools'][0]['name'] == 'Armadillo')
