from regression_tests import *

class NoBoundImport2Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='No_bound_import2.ex',
        args='--verbose --json'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['sectionTable']['crc32'], '58078107')
        self.assertEqual(self.fileinfo.output['sectionTable']['md5'], '7d4c5cc2526aab0d41f6c4d6d2884c36')
        self.assertEqual(self.fileinfo.output['sectionTable']['sha256'], '91ea35c3d0bcbaf9192532122ef5dda10bfbe4b2c1d994d0caef341443918d03')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['offset'], '0x4')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['crc32'], 'ddeb0ebe')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['md5'], '6a4607fc3e888a0a22f3991c2fdfd8c3')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sha256'], '7647a5b2dba2556ac996b579f8875bdbd64820593b307c96888731c9b1fce3fb')

class WindowManTest(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='WindowMan.ex',
        args='--verbose --json'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['sectionTable']['crc32'], 'e9f359db')
        self.assertEqual(self.fileinfo.output['sectionTable']['md5'], '265deee417288e2d51c704224665aa1f')
        self.assertEqual(self.fileinfo.output['sectionTable']['sha256'], '8e3588193c11bbb6b9a90f1e89bfa41327bd43346e2d12beb2b2335a9b5143bf')
