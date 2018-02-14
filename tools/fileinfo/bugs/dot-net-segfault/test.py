from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '47D6742DB3446366171B081610759BA1121E1602BE9D815F8C8A36005B54635D.dat',
            '49B5FC784CB848E89AA4339743349CAF988E1967734148CE5F3B23E49CE659A3.dat',
            '4E6ADC91661057FE9A6339DEE7CB4024BB0273227B3F81C53FABBCC62455EEB1.dat',
            'D98375CDFEA784E35E7AA34AC201469BE55F21DDA8D8EDF4EBEF28ACAA9116C6.dat'
        ]
    )

    def test_has_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
