from regression_tests import *


class TestDefaultLimit(Test):
    """Checks that retdec-decompiler.py correctly decompiles a binary file when
    there is the default memory limit (half of system RAM).

    Test for https://github.com/avast-tl/retdec/issues/270
    """

    settings = TestSettings(
        input='ack.ex',
    )

    def test_correctly_decompiled_file(self):
        # The check whether the decompilation was successful is done
        # automatically during setUp(), so we only check that the default
        # memory limit has been set.
        # For fileinfo:
        self.assertIn('--max-memory-half-ram', self.decompiler.output)
        # For bin2llvmir and llvmir2hll:
        self.assertIn(' -max-memory-half-ram', self.decompiler.output)


class TestCustomSufficientLimit(Test):
    """Checks that retdec-decompiler.py correctly decompiles a binary file when
    there is a custom memory limit (but sufficient).

    Test for https://github.com/avast-tl/retdec/issues/270
    """

    settings = TestSettings(
        input='ack.ex',
        args='--max-memory 107374182400',  # 1 GB
    )

    def test_correctly_decompiled_file(self):
        # The check whether the decompilation was successful is done
        # automatically during setUp(), so we only check that the memory limit
        # has been set.
        # For fileinfo:
        self.assertIn('--max-memory 107374182400', self.decompiler.output)
        # For bin2llvmir and llvmir2hll:
        self.assertIn(' -max-memory 107374182400', self.decompiler.output)


class TestCustomInsufficientLimit(Test):
    """Checks that retdec-decompiler.py fails to decompile a binary file when
    the maximal memory limit is too low.

    Test for https://github.com/avast-tl/retdec/issues/270
    """

    settings = TestSettings(
        input='ack.ex',
        args='--max-memory=4096',  # minimal limit is 1 page (4096 bytes)
    )

    def setUp(self):
        # Fail expected.
        pass

    def test_failed_to_decompile_file(self):
        self.assertNotEqual(self.decompiler.return_code, 0)


class TestNoLimit(Test):
    """Checks that retdec-decompiler.py correctly decompiles a binary file when
    there is no memory limit.

    Test for https://github.com/avast-tl/retdec/issues/270
    """

    settings = TestSettings(
        input='ack.ex',
        args='--no-memory-limit',
    )

    def test_correctly_decompiled_file(self):
        # The check whether the decompilation was successful is done
        # automatically during setUp(), so we only check that no memory limit
        # has been set.
        # For fileinfo:
        self.assertNotIn('--max-memory', self.decompiler.output)
        # For bin2llvmir and llvmir2hll:
        self.assertNotIn(' -max-memory', self.decompiler.output)
