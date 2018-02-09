from regression_tests import *

class TestMachoUniversal(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['hello-rust.elf', 'rust-without-debug.elf'],
        args='--json'
    )

    def test_fileinfo_detect_rust_and_rustc(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['fileFormat'], 'ELF')
        self.assertTrue(len(self.fileinfo.output['tools']) >= 1)
        self.assertEqual(self.fileinfo.output['tools'][0]['heuristics'], True)
        self.assertEqual(self.fileinfo.output['tools'][0]['identicalSignificantNibbles'], 0)
        self.assertEqual(self.fileinfo.output['tools'][0]['totalSignificantNibbles'], 0)
        self.assertEqual(self.fileinfo.output['tools'][0]['percentage'], 0)
        self.assertEqual(self.fileinfo.output['tools'][0]['name'], 'rustc')
        self.assertTrue(len(self.fileinfo.output['languages']) >= 1)
        self.assertEqual(self.fileinfo.output['languages'][0]['bytecode'], False)
        self.assertEqual(self.fileinfo.output['languages'][0]['name'], 'Rust')
