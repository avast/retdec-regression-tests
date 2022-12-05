from regression_tests import *

class TestDefaultLimit(Test):
    """Checks that retdec-decompiler.py correctly decompiles a binary file when
    there is the default memory limit (half of system RAM).

    Test for https://github.com/avast/retdec/issues/270
    """

    settings = TestSettings(
        input='ack.ex',
    )

    def test_correctly_decompiled_file(self):
        # The check whether the decompilation was successful is done
        # automatically during setUp(), so we only check that the default
        # memory limit has been set.
        # For fileinfo:
        #self.assertIn('--max-memory-half-ram', self.decompiler.output)
        # For bin2llvmir and llvmir2hll:
        #self.assertIn(' -max-memory-half-ram', self.decompiler.output)

        # In retdec-as-a-library there is no options passed to subprocesses.
        pass

# TODO: There were problems with this test in GH Actions.
#       For some reason it non-deterministically fails. Perhaps it does
#       not have enough memory on some occasions. Disabling this test is
#       not wanted but as we need to move forward we don't have time to investigate
#       this and create more clean solution.
#
# class TestCustomSufficientLimit(Test):
#     """Checks that retdec-decompiler.py correctly decompiles a binary file when
#     there is a custom memory limit (but sufficient).
#
#     Test for https://github.com/avast/retdec/issues/270
#     """
#
#     settings = TestSettings(
#         input='ack.ex',
#         args='--max-memory 2147483648',  # 2 GB
#     )
#
#     def test_correctly_decompiled_file(self):
#         # The check whether the decompilation was successful is done
#         # automatically during setUp(), so we only check that the memory limit
#         # has been set.
#         # For fileinfo:
#         #self.assertIn('--max-memory 1073741824', self.decompiler.output)
#         # For bin2llvmir and llvmir2hll:
#         #self.assertIn(' -max-memory 1073741824', self.decompiler.output)
#
#         # In retdec-as-a-library there is no options passed to subprocesses.
#         pass

class TestNoLimit(Test):
    """Checks that retdec-decompiler.py correctly decompiles a binary file when
    there is no memory limit.

    Test for https://github.com/avast/retdec/issues/270
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

# Memory limiting does not work correctly on macOS (see
# https://github.com/avast/retdec/issues/379).
if not on_macos():
    class TestCustomInsufficientLimit(Test):
        """Checks that retdec-decompiler.py fails to decompile a binary file when
        the maximal memory limit is too low.

        Test for https://github.com/avast/retdec/issues/270
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
