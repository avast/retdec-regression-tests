from regression_tests import *

# A test for the fix of https://github.com/avast/retdec/issues/824. As we do
# not have a way of checking the amount of allocated memory in regression
# tests, just check that the analysis succeeds.
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
