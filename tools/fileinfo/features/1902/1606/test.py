from regression_tests import *


class TestMachOSwift(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=files_in_dir('macho-swift')
    )

    def test_swift_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'swiftc')
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')
        # Language detection.
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Swift')


class TestMachOGo(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=files_in_dir('macho-go')
    )

    def test_go_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'gc')
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')
        self.assertEqual(self.fileinfo.output['tools'][1]['name'], 'gc')
        self.assertEqual(self.fileinfo.output['tools'][1]['type'], 'compiler')
        self.assertEqual(self.fileinfo.output['tools'][1]['version'], '1.9')
        # Language detection.
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Go')


class TestMachOXcode(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=files_in_dir('macho-xcode')
    )

    def test_xcode_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'XCode')
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')


class TestMachOGhc(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json',
        input=files_in_dir('macho-ghc')
    )

    def test_ghc_was_detected(self):
        assert self.fileinfo.succeeded
        # Compiler detection.
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'GHC')
        self.assertEqual(self.fileinfo.output['tools'][0]['type'], 'compiler')
        # Language detection.
        self.assertEqual(
            self.fileinfo.output['languages'][0]['name'], 'Haskell'
        )
