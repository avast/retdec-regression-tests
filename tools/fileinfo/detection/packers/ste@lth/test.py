from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample.ex',
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        self.assertTrue(self.fileinfo.succeeded)
        self.assertEqual(self.fileinfo.output['tools'][1]['name'], 'Ste@lth')
        self.assertEqual(self.fileinfo.output['tools'][1]['version'], '2.10')
