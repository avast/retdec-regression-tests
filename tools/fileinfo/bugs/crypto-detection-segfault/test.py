from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='mips-elf-6105b9d6abebd67d0258962d92b9b4dd',
        args='--verbose --json'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['crc32'], '357c4a41')
        self.assertEqual(self.fileinfo.output['md5'], '6105b9d6abebd67d0258962d92b9b4dd')
        self.assertEqual(self.fileinfo.output['sha256'], 'a1ba459edce86313d674f509bee82e0a09a74379239610cefb3bf36da3521076')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '30')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSegments'], '4')
        self.assertEqual(self.fileinfo.output['fileClass'], '32-bit')
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')
        self.assertEqual(self.fileinfo.output['fileType'], 'Executable file')
        self.assertEqual(self.fileinfo.output['sectionTable']['numberOfSections'], '30')
        self.assertEqual(len(self.fileinfo.output['segmentTable']), 4)
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['crc32'], '5b8da846')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['md5'], 'e892dce653aba7cde74a8077b5f5841f')
        self.assertEqual(self.fileinfo.output['segmentTable'][0]['sha256'], '391f59a0f8288daca456c0607c9f67cfb39fb9c7fbb7176d3092c178b43a4299')
        self.assertEqual(self.fileinfo.output['sizeOfOneEntryInTableOfSections'], '0x28')
        self.assertEqual(self.fileinfo.output['sizeOfOneEntryInTableOfSegments'], '0x20')
