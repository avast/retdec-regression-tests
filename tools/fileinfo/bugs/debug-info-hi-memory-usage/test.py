from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '022afb79c539b23aecfad315c7d9a712d747b521952184446026f7f2aa9005b8',
        ]
    )

    def test_analysis_succeeds(self):
        assert self.fileinfo.succeeded
