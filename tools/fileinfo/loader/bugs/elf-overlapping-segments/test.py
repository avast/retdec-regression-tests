from regression_tests import *

class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='arm-elf-1070f99f869534eb74b2aa4c916fc20f'
    )

    def test_overlapped_segments(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '2')

        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['size'], '0x286b')

        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], 'seg0001')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0x3e7c')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['size'], '0x29ac')

class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='b5a7da78bd82584c75c479bc46902791'
    )

    def test_overlapped_segments(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['loaderInfo']['numberOfSegments'], '2')

        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['address'], '0')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['size'], '0xb3f3f')

        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], 'seg0001')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['address'], '0xb3f3f')
        self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['size'], '0xdf7d')
