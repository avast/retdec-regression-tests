from regression_tests import *

class TestResources1(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='ef866e5eeacd096c4dab73c6d2b098253ba46f1ecf45467e6d65a8e1a75b4ca9'
    )

    def test_resources(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')
        self.assertEqual(self.fileinfo.output['declaredNumberOfDataDirectories'], '16')
        self.assertEqual(self.fileinfo.output['endianness'], 'Little endian')
        self.assertFalse('resourceTable' in self.fileinfo.output)
