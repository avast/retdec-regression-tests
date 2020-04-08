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

class Test_MPRMMGVA(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_mprmmgva.dat',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertTrue(self.fileinfo.output['tools'][0]['name'] == 'MPRMMGVA')

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

class Test_Petite(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_petite_001.dat',
        ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Petite')

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
