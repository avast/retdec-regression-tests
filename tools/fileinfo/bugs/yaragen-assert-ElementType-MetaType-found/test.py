from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '0B9B5209DA3612EEF8FA375DAE9BD189FEF724D5C3C8FB6EA1763D3FAB106E6B.dat',
            '48BA93E9CF91C28EDED373D4730914BC61B79129605404A807A1E7A9815F03B5.dat',
            'D6F2AF92B7E87B3033EB9E34BBF488EEAE9CDEB7619C198CF0CB5B3C3195ED09.dat'
        ]
    )

    def test_output_contains_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        assert 'classes' in self.fileinfo.output['dotnetInfo']
