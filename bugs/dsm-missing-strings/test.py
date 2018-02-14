from regression_tests import *

class TestDsm(Test):
    settings=TestSettings(
        input='hello.exe'
    )

    def test_strings_in_code(self):
        assert self.out_dsm.contains(r'0x4012b7:.* ; "_set_invalid_parameter_handler"\n')
        assert self.out_dsm.contains(r'0x40150f:.* ; "libgcj-13.dll"\n')
        assert self.out_dsm.contains(r'0x401528:.* ; "_Jv_RegisterClasses"\n')
        assert self.out_dsm.contains(r'0x40774e:.* ; "Hello, world!"\n')

    def test_strings_in_data(self):
        assert self.out_dsm.contains(r'0x409000:.* "_set_invalid_parameter_handler"\n')
        assert self.out_dsm.contains(r'0x409020:.* "libgcj-13.dll"\n')
        assert self.out_dsm.contains(r'0x40902e:.* "_Jv_RegisterClasses"\n')
        assert self.out_dsm.contains(r'0x409044:.* "Hello, world!"\n')
