from regression_tests import *

class Test_x64elf(Test):
    settings = TestSettings(
        input=files_in_dir('bin')
    )
    def test_main_calls_new(self):
        main = self.out_c.funcs['main']
        assert main.calls('_Znwm')

class Test_x64elf_opt_out(Test):
    settings = TestSettings(
        # The new and deref was optimized out.
        input=files_in_dir('optout')
    )
    def test_main_calls_new(self):
        main = self.out_c.funcs['main']
        assert (not main.calls('_Znwm'))
