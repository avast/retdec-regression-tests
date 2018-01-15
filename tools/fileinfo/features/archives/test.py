"""Checks that retdec-fileinfo.sh is able to analyze archives (.a/.lib files)."""

from regression_tests import *

class TestPlainOutput(Test):
    """Checks the plain-text output."""

    settings = TestSettings(
        tool='fileinfo',
        input='gnu.a'
    )

    def test_analyzes_archive_and_produces_plain_text_output(self):
        assert self.fileinfo.succeeded
        self.assertIn('fact_x86.o', self.fileinfo.output)
        self.assertIn('lib.o', self.fileinfo.output)

class TestJsonOutput(Test):
    """Checks the JSON output."""

    settings = TestSettings(
        tool='fileinfo',
        input='gnu.a',
        args='--json'
    )

    def test_analyzes_archive_and_produces_json_output(self):
        assert self.fileinfo.succeeded
        output = self.fileinfo.output
        #             (!!!) Important note (!!!)
        #
        #  This format of the JSON is assumed on the web (function
        #  get_names_of_files_in_archive() in web/decompilation/functions.php).
        #  Any changes to the format HAVE to be reflected on the web.
        #  Contact Petr Zemek when you change the format.
        #
        self.assertEqual(output['objects'][0]['name'], 'fact_x86.o')
        self.assertEqual(output['objects'][0]['index'], 0)
        self.assertEqual(output['objects'][1]['name'], 'lib.o')
        self.assertEqual(output['objects'][1]['index'], 1)

class TestInvalidArchive(Test):
    """Checks that fileinfo fails with an error when the input archive is
    invalid.
    """

    settings = TestSettings(
        tool='fileinfo',
        input='invalid.a'
    )

    def test_fails_with_error(self):
        assert self.fileinfo.failed
        self.assertIn('Error: File is not supported archive', self.fileinfo.output)
