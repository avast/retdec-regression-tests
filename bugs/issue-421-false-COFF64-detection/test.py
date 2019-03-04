from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='8801bfdaf3a3568da4f1696d382854c6ae8be141d3ff861ab019817b1237aee3'
    )

    def test_fileinfo_succeeds(self):
        assert not self.fileinfo.succeeded
        assert self.fileinfo.output.contains(
            'Error: File format of the input file is not supported. Supported formats:'
        )
