from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '2166c04fc0b4e0dbeff7a3226308e01a',
            '5955d1b2aa045aa7bba2a927c1250963',
            '838a884ba06e092865f5aae4e2438e0c',
            'cf2244f794754c20ff6092f3ee892a42',
            'db1c9c99aeb5a493e6beb40746437977'
        ]
    )

    def test_detected_as_dotnet_and_has_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        self.assertEqual('CIL/.NET', self.fileinfo.output['languages'][0]['name'])
