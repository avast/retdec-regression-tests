from regression_tests import *

class TestRsds(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input = "x86_64-pe-aa0a91227631a09cd075d315646fb7a9"
    )

    def test_correctly_analyzes_pdb_info(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['pdbInfo']['age'], '1')
        self.assertEqual(self.fileinfo.output['pdbInfo']['guid'], 'b57b8088-ec47-4900-ba81-e571172dfce')
        self.assertEqual(self.fileinfo.output['pdbInfo']['path'], 'DpInst.pdb')
        self.assertEqual(self.fileinfo.output['pdbInfo']['timestamp'], '2009-05-23T10:37:17+0000')
        self.assertEqual(self.fileinfo.output['pdbInfo']['type'], 'RSDS')

class TestNb10(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--verbose --json',
        input = "f56049df7e33162724c3f22a034b43be"
    )

    def test_correctly_analyzes_pdb_info(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains('s5spi.pdb')

        self.assertEqual(self.fileinfo.output['pdbInfo']['age'], '1')
        self.assertEqual(self.fileinfo.output['pdbInfo']['guid'], '55308367')
        self.assertEqual(self.fileinfo.output['pdbInfo']['timestamp'], '2015-04-17T03:52:07+0000')
        self.assertEqual(self.fileinfo.output['pdbInfo']['type'], 'NB10')
