from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='21FC9AD1B275B0F9C9525385070A025965E4CCA089E86109A02F48892C23A4C5.dat'
    )

    def test_no_segfault(self):
        assert self.fileinfo.succeeded
        assert 'classes' not in self.fileinfo.output['dotnetInfo']
