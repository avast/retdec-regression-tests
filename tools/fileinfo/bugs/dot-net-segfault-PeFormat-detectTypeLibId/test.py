from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='C32B0828AF69D7246A81E8FA5056EE63FF569F4B1151B1BE7C28A00BD5547E81.dat'
    )

    def test_does_not_contains_typelib_id(self):
        assert 'typeLibId' not in self.fileinfo.output['dotnetInfo']
