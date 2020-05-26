from regression_tests import *

class Test_plain(Test):
    settings = TestSettings(
        input='ack.x64.gcc.O0.g.exe',
        args='--output-format=plain'
    )
    
    def test_produce_expected_output(self):
        assert self.out_c.contains('int main\(int argc, char \*\* argv\)')

class Test_json(Test):
    settings = TestSettings(
        input='ack.x64.gcc.O0.g.exe',
        args='--output-format=json'
    )
    
    def test_produce_expected_output(self):
        assert self.out_c.contains('{"kind":"i_fnc","val":"main"}')

class Test_json_human(Test):
    settings = TestSettings(
        input='ack.x64.gcc.O0.g.exe',
        args='--output-format=json-human'
    )
    
    def test_produce_expected_output(self):
        assert self.out_c.contains('"kind": "i_fnc"')
        assert self.out_c.contains('"val": "main"')

class Test_json_bad(Test):
    settings = TestSettings(
        input='ack.x64.gcc.O0.g.exe',
        args='--output-format=bad_format'
    )
    
    def setUp(self):
        # Prevent the base class from checking that the decompilation
        # succeeded (we expect it to fail).
        pass
    
    def test_decompilation_fails_with_correct_error_message(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains('Error: \[-f|--output-format\] unknown output format: bad_format')
