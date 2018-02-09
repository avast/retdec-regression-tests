from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['382f4a1a3949fe9c52e2183131f11b4b', 'ff932fe448c312d7a623bb928c7eb6cd']
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'PE')
        self.assertEqual(self.fileinfo.output['File class'], '64-bit')
        self.assertEqual(self.fileinfo.output['File type'], 'Executable file')
        self.assertEqual(self.fileinfo.output['Architecture'], 'x86-64')
