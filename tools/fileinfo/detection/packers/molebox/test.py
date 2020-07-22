from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'sample_20.ex',
            'sample_236.ex',
            'sample_23x.ex',
            'sample_42321.ex',
            'sample_uv_02.ex',
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        molebox_found = False
        self.assertTrue(self.fileinfo.succeeded)

        for tool in self.fileinfo.output['tools']:
            if tool['name'] == 'MoleBox':
                molebox_found = True
        self.assertTrue(molebox_found)
