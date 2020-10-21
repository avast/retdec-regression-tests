from regression_tests import *

class TestAnalysisWhenNoLimit(Test):
    """Checks that fileinfo correctly analyzes file when there is no memory
    limit.

    Test for https://github.com/avast/retdec/issues/270
    """

    settings = TestSettings(
        tool='fileinfo',
        input='ack.ex',
    )

    def test_correctly_analyzes_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(
            self.fileinfo.output['SHA256'],
            '35f7b82373b66579d782fa61732da86717631eff95876b799a9549661709fd8b'
        )

class TestAnalysisWhenSufficient(Test):
    """Checks that fileinfo correctly analyzes file when there is a sufficient
    memory limit.

    Test for https://github.com/avast/retdec/issues/270
    """

    settings = TestSettings(
        tool='fileinfo',
        args=[
            '--max-memory=104857600',  # 100 MB
            '--max-memory-half-ram',
        ],
        input='ack.ex'
    )

    def test_correctly_analyzes_file(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['SHA256'], '35f7b82373b66579d782fa61732da86717631eff95876b799a9549661709fd8b')

class TestAnalysis_Issue872(Test):
    settings = TestSettings(
        tool='fileinfo',
        args=[
            '--max-memory=157286400',  # 150 MB. Needed to be updated after VS2017 Spectre update
            '--max-memory-half-ram',
        ],
        input='E556E9A67BBED5B6C32BE434A148841FEFEE81EB39432D427CB08FEFB0098173'
    )

    def test_correctly_analyzes_file(self):
        self.assertEqual(self.fileinfo.output['SHA256'], 'e556e9a67bbed5b6c32be434a148841fefee81eb39432d427cb08fefb0098173')

# Memory limiting does not work correctly on macOS (see
# https://github.com/avast/retdec/issues/379).
if not on_macos():
    class TestAnalysisWhenInsufficientLimit(Test):
        """Checks that fileinfo fails to analyze the file when the memory limit is
        not sufficient.

        Test for https://github.com/avast/retdec/issues/270
        """

        settings = TestSettings(
            tool='fileinfo',
            args='--max-memory=4096',  # minimal limit is 1 page (4096 bytes)
            input='ack.ex',
        )

        def test_fails_to_analyze_file(self):
            assert not self.fileinfo.succeeded, 'fileinfo succeeded but should have failed'
