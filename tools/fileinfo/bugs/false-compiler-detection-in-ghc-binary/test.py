from regression_tests import *

class TestInvalidGHCVersion(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='not-ghc',
    )

    def test_invalid_ghc_version(self):
        assert not self.fileinfo.output.contains(r'GHC')

class TestValidGHCVersion(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='is-ghc',
    )

    def test_invalid_ghc_version(self):
        assert self.fileinfo.output.contains(r'Haskell')
        assert self.fileinfo.output.contains(
           r'GHC \(7.6.3\) \(compiler\), combined heuristic'
        )
