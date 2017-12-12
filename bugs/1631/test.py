from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='hello-world.bin'
    )

    def test_strings_in_code(self):
        assert self.out_dsm.contains(r'0x804831b:\s*8b 83 fc ff ff ff\s*mov eax, dword ptr \[ebx \- 4\]')
        assert self.out_dsm.contains(r'0x804835b:\s*e9 e0 ff ff ff   \s*jmp 0x8048340 <function_8048340>')
        assert self.out_dsm.contains(r'0x8048561:\s*83 f8 ff         \s*cmp eax, \-1')
