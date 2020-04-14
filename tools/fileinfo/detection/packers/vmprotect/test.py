from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='VMProtect-3.4_demo.ex',
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        self.assertTrue(self.fileinfo.succeeded)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'VMProtect')
        self.assertEqual(self.fileinfo.output['tools'][0]['version'], '2.04+')
