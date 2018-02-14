from regression_tests import *

class TestDsm(Test):
    settings=TestSettings(
        input='hello-world.exe'
    )

    def test_strings_in_data(self):
        assert self.out_dsm.contains(r'0x409000:\s*5f 73 65 74 5f 69 6e 76  61 6c 69 64 5f 70 61 72\s*|_set_invalid_par|   "_set_invalid_parameter_handler"')
        assert self.out_dsm.contains(r'0x409010:\s*61 6d 65 74 65 72 5f 68  61 6e 64 6c 65 72 00   \s*|ameter_handler. |')
        assert self.out_dsm.contains(r'0x40901f:\s*00                                              \s*|.               |')
        assert self.out_dsm.contains(r'0x409020:\s*6c 69 62 67 63 6a 2d 31  33 2e 64 6c 6c 00      \s*|libgcj-13.dll.  |   "libgcj-13.dll"')
        assert self.out_dsm.contains(r'0x40902e:\s*5f 4a 76 5f 52 65 67 69  73 74 65 72 43 6c 61 73\s*|_Jv_RegisterClas|   "_Jv_RegisterClasses"')
        assert self.out_dsm.contains(r'0x40903e:\s*73 65 73 00                                     \s*|ses.            |')
        assert self.out_dsm.contains(r'0x409042:\s*00 00                                           \s*|..              |')
        assert self.out_dsm.contains(r'0x409044:\s*48 65 6c 6c 6f 2c 20 77  6f 72 6c 64 21 00      \s*|Hello, world!.  |   "Hello, world!"')
        assert self.out_dsm.contains(r'0x409052:\s*00 00 b0 15 40 00 55 6e  6b 6e 6f 77 6e 20 65 72\s*|....@.Unknown er|')
