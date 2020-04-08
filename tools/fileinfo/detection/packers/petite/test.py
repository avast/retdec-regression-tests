from regression_tests import *

class Test_001(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='fact_rec.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(1\.3a\)*')


class Test_002(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            'sample_petite_001.dat',
        ],
        args='--json'
    )

    def test_petite_packer(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'Petite')
