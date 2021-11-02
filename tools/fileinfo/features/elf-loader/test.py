from regression_tests import *


class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            '051c02260e4f10ca956e3bcc8c5ab9295e12660c39fed4fe442e5a22fa09622d',
        ],
        args='--json --verbose'
    )

    def test_corrupted_elf(self):
        assert self.fileinfo.succeeded
        assert 'loaderError' in self.fileinfo.output
        assert self.fileinfo.output['loaderError']['code'] == 1
        assert self.fileinfo.output['loaderError']['code_text'] == "LOAD Segment data is not within file bounds"
        assert self.fileinfo.output['loaderError']['description'] == "LOAD Segment data is not within file bounds"
        assert self.fileinfo.output['loaderError']['loadable_anyway'] == "false"
