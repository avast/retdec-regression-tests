from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='972C1741D9D7A6FF63A56434031098041312E7CC769C33008D5BDE0A47F80F21.dat'
    )

    def test_no_dotnet_classes(self):
        assert self.fileinfo.succeeded
        assert 'classes' not in self.fileinfo.output['dotnetInfo']
