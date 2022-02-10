from regression_tests import *

# Test for existance of dllFlags even in EXE files
class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['Test32.dll_'],
        args='--verbose --json'
    )

    def test_dllflags_present(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['dllName'], 'TestDll.dll')
