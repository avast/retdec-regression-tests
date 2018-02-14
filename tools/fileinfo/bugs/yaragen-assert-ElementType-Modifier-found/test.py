from regression_tests import *

class Test:
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='EE2F1883CFD5D481CCDAA17A73F6BA6FDD9325D13B45DAA34470F7122C225882.dat'
    )

    def test_has_dotnet_info(self):
        assert 'dotnetInfo' in self.fileinfo.output
