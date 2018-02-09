from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='47C8FFE7905BD2FA508E9BFE93571010F7F54084C14B76A02341D0A965184CDA.dat'
    )

    def test_output_contains_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        assert 'classes' in self.fileinfo.output['dotnetInfo']
