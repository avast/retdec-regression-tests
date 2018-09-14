from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='unpacker',
        input='0d52fef11e4a676c999265d5019a6ce8'
    )

    def unpacker_fails_on_corrupted_unpacking_stub(self):
        self.assertEqual(self.unpacker.return_code, 2)
        assert self.unpacker.output.contains('[MPRESS] Corrupted unpacking stub detected.')
