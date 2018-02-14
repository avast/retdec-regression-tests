from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '564FAF0B9F25C0A8F156E9C82A36D2B854E5110820C9400374EB26EC631C19E5.dat',
            'F70FA1DCD6C54E95D4F5FE69F62AD5AED813FB6F9ECB27D8637E34F517ACE97E.dat'
        ]
    )

    def test_output_contains_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert 'dotnetInfo' in self.fileinfo.output
        assert 'classes' in self.fileinfo.output['dotnetInfo']
