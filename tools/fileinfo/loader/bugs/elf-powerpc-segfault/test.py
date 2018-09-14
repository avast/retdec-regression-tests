from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            'powerpc-elf-068b6e92780db9dea05e1c7fdd834584',
            'powerpc-elf-bd8ece671f768791e182792d74931120'
        ]
    )

    def test_loaded_successfully(self):
        assert self.fileinfo.succeeded
        assert int(self.fileinfo.output['loaderInfo']['numberOfSegments']) > 0
