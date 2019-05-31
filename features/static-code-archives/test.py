from regression_tests import *

class DecompileWithSignaturesFromSigfile(Test):

    settings = TestSettings(
        input='test.elf',
        static_code_sigfile='lib.yara'
    )

    def test_check_correct_static_functions_detection(self):
        assert self.out_config.is_statically_linked('ackermann', 134513831)
        assert self.out_config.is_statically_linked('factorial', 134513923)
        assert self.out_config.is_statically_linked('my_strlen', 134513966)

    def test_check_correct_static_functions_calls(self):
        assert self.out_c.funcs['main'].calls('ackermann')
        assert self.out_c.funcs['main'].calls('factorial')
        assert self.out_c.funcs['main'].calls('my_strlen')

class DecompileWithSignaturesFromArchive(Test):

    settings = TestSettings(
        input='test.elf',
        static_code_archive='lib .a'
    )

    def test_check_correct_static_functions_detection(self):
        assert self.out_config.is_statically_linked('ackermann', 134513831)
        assert self.out_config.is_statically_linked('factorial', 134513923)
        assert self.out_config.is_statically_linked('my_strlen', 134513966)

    def test_check_correct_static_functions_calls(self):
        assert self.out_c.funcs['main'].calls('ackermann')
        assert self.out_c.funcs['main'].calls('factorial')
        assert self.out_c.funcs['main'].calls('my_strlen')

class DecompileWithSignaturesFromArchiveInvalidArchive(Test):

    settings = TestSettings(
        input='test.elf',
        static_code_archive='lib.yara'
    )

    def test_check_correct_warning(self):
        assert self.decompiler.log.contains(r'Warning: Failed extracting signatures from file \'.*\'')
