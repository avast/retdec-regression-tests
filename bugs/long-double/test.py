from regression_tests import *
from regression_tests.utils.os import on_windows

class Test(Test):
    """Checks that we correctly recognize and emit literals of type long
    double.
    """

    settings = TestSettings(
        input=[
            'long-double.x86.clang.O0.elf', 'long-double.x86.clang.O1.elf', 'long-double.x86.clang.O2.elf', 'long-double.x86.clang.O3.elf',
            'long-double.x86.clang.O0.exe', 'long-double.x86.clang.O1.exe', 'long-double.x86.clang.O2.exe', 'long-double.x86.clang.O3.exe',
            'long-double.x86.gcc.O0.elf', 'long-double.x86.gcc.O1.elf', 'long-double.x86.gcc.O2.elf', 'long-double.x86.gcc.O3.elf',
            'long-double.x86.gcc.O0.exe', 'long-double.x86.gcc.O1.exe', 'long-double.x86.gcc.O2.exe', 'long-double.x86.gcc.O3.exe',
        ]
    )

    def test_long_double_literal_is_correctly_recognized(self):
        if on_windows():
            # On Windows, the literal may either be 1e320L or inf, depending on
            # the compiler (MSVC does not support 80b long double, so it uses
            # double, in which the literal "overflows" to inf).
            assert self.out_c.contains('1.0e\+320L') or self.out_c.contains('inf')
        else:  # Linux
            # Both GCC and Clang on Linux support 80b long double.
            assert self.out_c.contains('1.0e\+320L')
