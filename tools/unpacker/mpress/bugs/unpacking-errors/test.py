from regression_tests import *

class TestNoEntryPoint(Test):
    settings=TestSettings(
        tool='unpacker',
        input='c544ff15f206b1a6864cfd865c909dc4'
    )

    def test_no_entry_point(self):
        self.assertEqual(self.unpacker.return_code, 2)
        assert self.unpacker.output.contains('No entry point segment found.')

class TestInvalidImportHints(Test):
    settings=TestSettings(
        tool='unpacker',
        input='ea4fee3ab95e4257651b632425f09198'
    )

    def test_invalid_import_hints(self):
        self.assertEqual(self.unpacker.return_code, 2)
        assert self.unpacker.output.contains('Invalid import hints detected.')

class TestResourcesStillPresent(Test):
    settings=TestSettings(
        tool='unpacker',
        input='61d0e6a206de8bde427ff79ea68d0d88d5ca1021ab335ac8c63b98be8a8b05ea',
        run_fileinfo=True
    )

    def test_resources_still_present(self):
        assert self.unpacker.succeeded
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["resourceTable"]["numberOfResources"], "3")
