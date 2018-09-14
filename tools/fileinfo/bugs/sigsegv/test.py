from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='MEW_SE11_1.2_MEW_SE11_1.2_C_DLL.DEF.ex'
    )

    def test_detection_works(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'PE')
        self.assertEqual(self.fileinfo.output['imageBaseAddress'], '0x5f070000')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '2')
        self.assertEqual(self.fileinfo.output['importTable']['numberOfImports'], '2')
        self.assertEqual(self.fileinfo.output['resourceTable']['numberOfResources'], '64')
