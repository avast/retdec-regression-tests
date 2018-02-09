from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '05985BD429997839BD416743EAEDD337C1DD4074409E749A5325EBFC64D53939.dat',
            'E66BEAFCFA74BF929C44100D0AE9EA18FF5DAA6F400EFD8475C6E58C4DD7EF32.dat'
        ]
    )

    def test_has_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
