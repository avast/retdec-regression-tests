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
                         ['coffHeader'], '2016-01-09T04:52:11+0000')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['loadConfigDir'], '2031-04-18T05:10:52+0000')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['exportDir'], "2021-08-23T03:12:51+0000")
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['debugDirEntries'][0], "2016-01-09T04:52:11+0000")
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['debugDirEntries'][1], "2016-01-09T04:52:11+0000")
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][0],
            '2021-10-19T11:13:06+0000')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['pdbDebugInfos'][0], '2006-07-25T04:53:49+0000')


class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='7110C2E35B423FCDB50D32DFCBE961CB5E67D9E8C87324A98E6F0191A862C495.ex'
    )

    def test_pe_timestamps(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['coffHeader'], '2016-04-06T14:39:04+0000')
        self.assertEqual(self.fileinfo.output['timestamps']
                         ['loadConfigDir'], '1970-01-01T00:02:52+0000')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][0],
            '1970-08-09T18:46:24+0000')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][1],
            '1970-02-07T06:22:42+0000')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][2],
            '1971-08-21T02:23:31+0000')
        self.assertEqual(
            self.fileinfo.output['timestamps']['resourceDirectories'][3],
            "2024-04-10T04:14:11+0000")
