from regression_tests import *

class Test(Test):
    """Checks that we correctly detect and report cases when the input file
    contains bytecode.
    """

    settings = TestSettings(
        input=['InjectionLibrary.dll', 'billingsoft.ex'],
        # Deliberately decompile nothing to make the test run faster
        # (decompilation of bytecode takes very long). After all, we only want
        # to detect the presence of a warning after fileinfo is run.
        args='--select-ranges 0x0-0x1 --select-decode-only'
    )

    def setUp(self):
        pass

    def test_fileinfo_detects_bytecode(self):
        self.assertEqual(self.decompiler.fileinfo_output['Original language'], 'CIL/.NET (bytecode)')

    def test_warning_is_emitted(self):
        # Do NOT change the format of the following warning because the
        # decompilation service depends on it.
        assert self.decompiler.log.contains(r'Warning: Detected CIL/.NET bytecode, which .*')
