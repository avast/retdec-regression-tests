from regression_tests import *


class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='TidyESP.ex'
    )

    def test_pe_timestamps(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['coffHeader'], 'Jan  9 04:52:11 2016 GMT')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['loadConfigDir'], 'Apr 18 05:10:52 2031 GMT')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['exportDir'], "Aug 23 03:12:51 2021 GMT")
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['debugDirEntries'][0], "Jan  9 04:52:11 2016 GMT")
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['debugDirEntries'][1], "Jan  9 04:52:11 2016 GMT")
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][0],
            'Oct 19 11:13:06 2021 GMT')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['pdbDebugInfos'][0], 'Jul 25 04:53:49 2006 GMT')


class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='7110C2E35B423FCDB50D32DFCBE961CB5E67D9E8C87324A98E6F0191A862C495.ex'
    )

    def test_pe_timestamps(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['coffHeader'], 'Apr  6 14:39:04 2016 GMT')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['loadConfigDir'], 'Jan  1 00:02:52 1970 GMT')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][0],
            'Aug  9 18:46:24 1970 GMT')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][1],
            'Feb  7 06:22:42 1970 GMT')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][2],
            'Aug 21 02:23:31 1971 GMT')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][3],
            "Apr 10 04:14:11 2024 GMT")
