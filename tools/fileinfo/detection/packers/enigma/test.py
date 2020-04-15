from regression_tests import *

class TestEnigma0x(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='enigma_0x',
        args='--json'
    )

    def test_enigma_detected(self):
        self.assertTrue(self.fileinfo.succeeded)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Enigma')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '0.x beta')

class TestEnigma102(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='enigma_102',
        args='--json'
    )

    def test_enigma_detected(self):
        self.assertTrue(self.fileinfo.succeeded)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Enigma')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '1.02')

class TestEnigma1x(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='enigma_1x',
        args='--json'
    )

    def test_enigma_detected(self):
        self.assertTrue(self.fileinfo.succeeded)
        self.assertEqual(self.fileinfo.output['tools'][2]['name'], 'Enigma')
        self.assertEqual(self.fileinfo.output['tools'][2]['version'], '1.x+')

class TestEnigmax64(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='enigma_x64_610',
        args='--json'
    )

    def test_enigma_detected(self):
        self.assertTrue(self.fileinfo.succeeded)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Enigma')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '1.x+ (64-bit)')
