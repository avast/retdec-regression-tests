from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='macho_x86'
    )

    def test_imphash_is_present(self):
        self.assertEqual(self.fileinfo.output['importTable']['md5'], '796e60d0879941b6848a356f3d0a548b')
