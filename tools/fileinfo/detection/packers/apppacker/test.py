from regression_tests import *

class Test_AppPacker(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=["FileTest_AppPacker_1.3.2_32bit.exe_",
               "FileTest_AppPacker_1.3.2_64bit.exe_",
               "FileTest_AppPacker_1.3.b_32bit.exe_",
               "FileTest_AppPacker_1.3.b_64bit.exe_"
              ],
        args='--json'
    )

    def test_pe_packer(self):
        assert self.fileinfo.succeeded
        self.assertTrue(self.fileinfo.output['tools'][0]['name'] == 'AppPacker 1.3.x')

