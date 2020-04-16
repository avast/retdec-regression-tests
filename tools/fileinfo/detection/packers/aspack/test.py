from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='ASP212_C_big.Exp_tbl_comp.ex'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*ASPack \(2\.12\)*')

class TestASPack(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'asp_uv_09',
            'asp_uv_10',
            'asp_uv_11',
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        aspack_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'packer' and tool['name'] == 'ASPack':
                aspack_recognised = True
        self.assertTrue(aspack_recognised)
