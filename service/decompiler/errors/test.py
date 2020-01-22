"""Tests for error messages produced by our decompiler.

These error messages are parsed by the decompilation service and shown to the
user (either as-is or modified).
"""

from regression_tests import *

class NoSectionsOrSegmentsErrorTest(Test):
    """Checks that bin2llvmir fails with a proper error message when neither
    sections nor segments are found.
    """

    settings = TestSettings(
        input='91635bb90bc581e0946284d1bb3fb4f9'
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    # IMPORTANT: Do NOT change the format or text of the error because the
    #            parser of the decompiler's output relies on it. If you want to
    #            change it, consult this with Petr Zemek.
    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'Error: Failed to load input file')

class NoInstructionsDecodedTest(Test):
    """Checks that bin2llvmir fails with a proper error message when no
    instructions were decoded.
    """

    settings = TestSettings(
        input='payload.bin'
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    # IMPORTANT: Do NOT change the format or text of the error because the
    #            parser of the decompiler's output relies on it. If you want to
    #            change it, consult this with Petr Zemek.
    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'Error: No instructions were decoded')

class InvalidInputConfigErrorTest(Test):
    """Checks that fileinfo fails with a proper error message when the input
    JSON config is invalid.

    This is important because of the IDA plugin (it sends input JSON file
    configs to the web service). We want to ensure that an error is printed so
    it can be shown to the user if an invalid config is received.

    Fileinfo error messages are directly shown to the user (no special handling
    is needed in the decompilation service).
    """

    settings = TestSettings(
        input='invalid-config.exe',
        config='invalid-config.json'
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'Error: loading of config failed')

class MissingInfoAboutFileTest(Test):
    """Checks that bin2llvmir fails with a proper error message when basic
    information about the input file is missing.

    This happens when a different architecture is forced for a binary file.
    """

    settings = TestSettings(
        input='ptzdriver',
        arch='x86' # x86 is forced to reproduce the situation with missing info.
    )

    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass

    # IMPORTANT: Do NOT change the format or text of the error because the
    #            parser of the decompiler's output relies on it. If you want to
    #            change it, consult this with Petr Zemek.
    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'Error: Missing basic info about input file -> there can be no decompilation')
