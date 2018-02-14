from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='input.ex',
        args='--verbose --json'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['importTable']['crc32'], '3b95cf01')
        self.assertEqual(self.fileinfo.output['importTable']['md5'], 'f34d5f2d4577ed6d9ceec516c1f5a744')
        self.assertEqual(self.fileinfo.output['importTable']['sha256'], '04e4985516701e4f52c771794fec457bb96615ddc661e7233d24e1c66fb5cea0')
        self.assertEqual(self.fileinfo.output['resourceTable']['numberOfResources'], '9')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['crc32'], 'fe6778e7')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['md5'], 'cdd4230fcf2eab1bd99d86ac64a3c27b')
        self.assertEqual(self.fileinfo.output['resourceTable']['resources'][0]['sha256'], '945961afc0bb5c44e2745e3cdadf834685a9233ae5822e731a963b38fdce51a1')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['crc32'], '1dc813aa')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['md5'], '3a25e22e869087ef1ca62f2bf3ce384f')
        self.assertEqual(self.fileinfo.output['sectionTable']['sections'][0]['sha256'], '4739240e8490e5d84f78bb8eb3e9670ac676f3e4b6eea462e62a4b3311582368')
        self.assertEqual(self.fileinfo.output['crc32'], '754f366a')
        self.assertEqual(self.fileinfo.output['md5'], '496c97a81e58c72398750b5c4808261e')
        self.assertEqual(self.fileinfo.output['sha256'], '7b016e04b4ac2cd10cbbad5978be9c460adf274ed12b4872965572980b386d59')
