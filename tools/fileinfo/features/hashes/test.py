from regression_tests import *

class TestAllHashes(Test):
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


# https://github.com/avast-tl/retdec/issues/246
# Test for ordinals thar are translated by YARA/pefile LUT.
class TestImportHashYARAcompatibleLutOrds(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ordinal',
        args='--verbose --json'
    )

    def test_correctly_computes_import_hash(self):
        assert self.fileinfo.succeeded
        self.assertEqual(
            self.fileinfo.output['importTable']['md5'],
            'd3bf8a7746a8d1ee8f6e5960c3f69378'
        )


# https://github.com/avast-tl/retdec/issues/246
# Test for ordinals thar are NOT translated by YARA/pefile LUT.
class TestImportHashYARAcompatibleNoLutOrds(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ordinal-nonlut',
        args='--verbose --json'
    )

    def test_correctly_computes_import_hash(self):
        assert self.fileinfo.succeeded
        self.assertEqual(
            self.fileinfo.output['importTable']['md5'],
            '4a685152543193737b50e1b699b8764e'
        )

# https://github.com/avast-tl/retdec/issues/121
# Test export hashes for PE format
class TestExportHashPE(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='export_hashPE',
        args='--verbose --json'
    )

    def test_correctly_computes_export_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['exportTable']['crc32'], '537c3723')
        self.assertEqual(self.fileinfo.output['exportTable']['md5'], 'ed5fc6509f84c22d0a5181a74b169f4d')
        self.assertEqual(self.fileinfo.output['exportTable']['sha256'], '2ad7a39d00b78ab7bcb584bcef1d4a95246ebe9241e5ae3e24234bd6bca63cd9')

# https://github.com/avast-tl/retdec/issues/121
# Test export hashes for ELF format
class TestExportHashELF(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='export_hashELF',
        args='--verbose --json'
    )

    def test_correctly_computes_export_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['exportTable']['crc32'], 'e1696c79')
        self.assertEqual(self.fileinfo.output['exportTable']['md5'], '1751216bdaf64142e87ce756a0c40817')
        self.assertEqual(self.fileinfo.output['exportTable']['sha256'], '6bb3c5893a91e9680ebcedea9f2b01cac380b1f98af4067be567981e3b3bf91b')

# https://github.com/avast-tl/retdec/issues/121
# Test export hashes for ELF format
class TestExportHashMACHO(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='export_hashMACHO',
        args='--verbose --json'
    )

    def test_correctly_computes_export_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['exportTable']['crc32'], 'b4a8ec08')
        self.assertEqual(self.fileinfo.output['exportTable']['md5'], '69c3263d43b9c3a5fad072fd81519e50')
        self.assertEqual(self.fileinfo.output['exportTable']['sha256'], 'b59f469f07123abee30e93a83e8b8908ed7faa8b140dba0093204b6b3efd541c')

