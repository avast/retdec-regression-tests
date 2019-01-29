from regression_tests import *

class FiboTest(Test):
    """Symbols of imported functions in this binary are prefixed with
    '__isoc99_' e.g. __isoc99_scanf.
    Tests that these prefixes are removed and correct LTI signatures are used.
    """

    settings = TestSettings(
        input='fibo.x86-clang-O1.elf'
    )

    def test_imported_functions(self):
        assert self.out_c.has_comment_matching(r'// int printf\(.*char.*\*.*...\);')
        assert self.out_c.has_comment_matching(r'// int scanf\(.*char.*\*.*...\);')

    def test_imported_functions_are_used(self):
        assert self.out_c.funcs['main'].calls('printf')
        assert self.out_c.funcs['main'].calls('scanf')

class CloseTest(Test):
    """_close function is used in the original source code. __close symbol is
    used in binary.
    Tests that _close function is used in the decompiled source code.
    Tests that the name of used function is the same as comment for import.
    """

    settings = TestSettings(
        input='test.x86-mingw-O2.exe'
    )

    def test_imported_close_function(self):
        assert self.out_c.has_comment_matching(r'// int __cdecl _close\(.*int.*\);')

    def test_imported_close_function_is_used(self):
        assert self.out_c.funcs['main'].calls('_close')
