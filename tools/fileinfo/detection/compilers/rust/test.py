from regression_tests import *

class TestRustDetection_32bit(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='Test32.exe_',
        args='--json'
    )

    def test_detected_rust(self):
        rust_recognized = False
        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'Rust (32-bit)' and tool['version'] == 'i686-pc-windows-msvc':
                rust_recognized = True
        self.assertTrue(rust_recognized)

class TestRustDetection_64bit(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'c9c94ac5e1991a7db42c7973e328fceeb6f163d9f644031bdfd4123c7b3898b0',
            'Test64.exe_',
            ],
        args='--json'
    )

    def test_detected_rust(self):
        rust_recognized = False
        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output["tools"]:
            if tool['type'] == 'compiler' and tool['name'] == 'Rust (64-bit)' and tool['version'] == 'x86_64-pc-windows-msvc':
                rust_recognized = True
        self.assertTrue(rust_recognized)
