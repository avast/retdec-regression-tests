from regression_tests import *

# Test for existance of dllFlags even in EXE files
class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['Test32.dll_', 'Test32.exe_'],
        args='--verbose --json'
    )

    def test_dllflags_present(self):
        assert self.fileinfo.succeeded
        self.assertIn('dllFlags', self.fileinfo.output)
