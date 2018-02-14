from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='rubic_d-O0-g0.exe'
    )

    #def test_statically_linked_delphi_functions_are_generated_with_correct_types(self):
        #assert self.out_c.has_comment_matching(r'// void Sysinit__InitExe\(char \* a1\);')
        #assert self.out_c.has_comment_matching(r'// void System__FillChar\(char \* a1, int32_t a2, char a3\);')
        #assert self.out_c.has_comment_matching(r'// void System__Halt0\(int32_t a1\);')
        #assert self.out_c.has_comment_matching(r'// void System__Randomize\(int32_t a1\);')
