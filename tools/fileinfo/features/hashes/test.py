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

# https://github.com/avast/retdec/issues/246
# Test for ordinals that are translated by YARA/pefile LUT.
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

# https://github.com/avast/retdec/issues/246
# Test for ordinals that are NOT translated by YARA/pefile LUT.
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

# https://github.com/avast/retdec/issues/121
# Test export hashes for PE format
class TestExportHashPE(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='export_hashPE',
        args='--verbose --json'
    )

    def test_correctly_computes_export_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['exportTable']['crc32'], '0129b53c')
        self.assertEqual(self.fileinfo.output['exportTable']['md5'], 'aad0eae4ce7252a9bfd0ffaa3f5f9785')
        self.assertEqual(self.fileinfo.output['exportTable']['sha256'], '96ed433038a072261a91f36898fe9189a64a626472638a0d78f21b8979acefcf')

# https://github.com/avast/retdec/issues/121
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

# https://github.com/avast/retdec/issues/121
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

# Test average hash of a PE icon
class TestResourceIconHash1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='resource_icon_hash1',
        args='--verbose --json'
    )

    def test_correctly_computes_resource_icon_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['resourceTable']['iconCrc32'], 'ffcc3f4a')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconMd5'], 'b05b211c2e111a918ada5876438647c7')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconSha256'], '817d4da182600378d119408d56693fc0daba9d4296e56ef7b7c2e49caf916d37')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconAvgHash'], '0000202038380000')

class TestResourceIconHash2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='resource_icon_hash2',
        args='--verbose --json'
    )

    def test_correctly_computes_resource_icon_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['resourceTable']['iconCrc32'], 'ad0052e5')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconMd5'], '9ec05f304e57a9e606c0032634e559db')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconSha256'], 'bdb247c84e26b93d2ea6b7f4e12d3949ef5be2e9c5eff07a805bdc658a770e84')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconAvgHash'], '0000202038380000')

class TestResourceIconHash3(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='resource_icon_hash3',
        args='--verbose --json'
    )

    def test_correctly_computes_resource_icon_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['resourceTable']['iconCrc32'], '06272459')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconMd5'], 'be0bd1d1c38eb059201c3a97141728f6')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconSha256'], '7e648590d398e4313266a5c7ace61a07302e5325137d03e8fa8f9cc443a15fe4')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconAvgHash'], '0042001000004200')

class TestResourceIconHash4(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample-cross-linked-icons.dat',
        args='--verbose --json'
    )

    def test_correctly_computes_resource_icon_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['resourceTable']['iconCrc32'], '57d94c0d')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconMd5'], 'f16287a63f1594c772a6be0a090f9440')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconSha256'], 'bb6f9795ad97367b4dc0dd5787ca0a9160d62b95a34f5830e7f6f69d791e42c6')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconAvgHash'], 'ffc3bdffbd8183ff')

class TestResourceIconHashPng(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='png_icon.file',
        args='--verbose --json'
    )

    def test_correctly_computes_resource_icon_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['resourceTable']['iconMd5'], '4066f80a90faf7d2bb0b2b3cfba3f91e')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconAvgHash'], 'ffffdffbefefefff')

class TestResourceIconHashDib(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='dib_icon.file',
        args='--verbose --json'
    )

    def test_correctly_computes_resource_icon_hash(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['resourceTable']['iconMd5'], '6fc488a9aaa79eb8bea0e6e4e586ba87')
        self.assertEqual(self.fileinfo.output['resourceTable']['iconAvgHash'], 'ffffdffbefefefff')

class TestTelfhash1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='export_hashELF',
        args='--verbose --json'
    )

    def test_telfhash(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['telfhash'], 'T1DAB0126DD319C94560CE1610444376B7D106C875105B601301F010B85E001801447D3D')

    def test_import_table_hashes(self):
        self.assertEqual(self.fileinfo.output['importTable']['crc32'], 'e441714e')
        self.assertEqual(self.fileinfo.output['importTable']['md5'], '26e125edc4bb34a4a3a424543f0cac84')
        self.assertEqual(self.fileinfo.output['importTable']['sha256'], 'afcb2d66afb328958e3fd93f4fd5028eb66edb61cb407e20f10bacd489315ed1')
        self.assertEqual(self.fileinfo.output['importTable']['tlsh'], 't167d095efc918dd4f4c4d9514247738343191c5033d1480c3477042dc002446d35cdc6c')

class TestTelfhash2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='telfhash',
        args='--verbose --json'
    )

    def test_telfhash(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['telfhash'], 'T1E123FC0C6CF10E452ACA53E7EC3409C4237BE21E15A978159E2CD3BD99AD2CD1DB6B1E')
