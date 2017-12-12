from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ack.ihex',
        args='--verbose --json'
    )

    def test_correctly_analyzes_input_ihex_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['crc32'], '313a1bf1')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '2')
        self.assertEqual(self.fileinfo.output['entryPoint']['address'], '0x890003c')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Intel HEX')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['md5'], '99551ea5f0098fb04a490093505615d7')
        self.assertEqual(self.fileinfo.output['sha256'], '8c32c2ccb6e4efa724978ca689258b3dec8ae1e0938647469f82d7ad45f35e2f')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['address'], '0x8900018')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['crc32'], '6d551839')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['index'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['md5'], 'ae0289d5cb0dbfd42aead3e1d4da0636')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['offset'], '0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sha256'], '48936f07fc139bcce0d516c1feb63afa7a987c0b9a66e75c3a233046fe514680')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sizeInFile'], '0x16e20')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sizeInMemory'], '0x16e20')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['address'], '0x8916f38')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['crc32'], 'ed739c69')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['index'], '1')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['md5'], 'bb7e35470d2de75d3929f3db70e50d1a')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['offset'], '0x16e20')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['sha256'], '68a7e5b4cb186704c19271c0bed67a2e8a4af24e6e98b176f61b175185d0dab0')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['sizeInFile'], '0xb9c')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][1]['sizeInMemory'], '0xb9c')
