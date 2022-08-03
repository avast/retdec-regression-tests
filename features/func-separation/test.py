import re

from regression_tests import *

class UserAndLinkedTest(Test):
    """Tests that the generated functions are recognized as "user-defined",
    "statically linked", and "dynamically linked", and put into proper sections
    in the generated C file.

    Also, we check that a correct separation is done in the generated DSM file.
    """

    settings = TestSettings(
        input='wide-strings.ex'
    )

    def test_funcs_are_separated_in_c_into_user_defined_dynamically_linked_and_statically_linked(self):
        expected_code_re = re.compile("""
                -\ Dynamically\ Linked\ Functions\ Without\ Header\ -
                .*
                _wfopen
                .*
                -\ Functions\ -
                .*
                main
                .*
                -\ Statically\ Linked\ Functions\ -
                .*
                ___main
                .*
            """,
            flags=re.VERBOSE | re.DOTALL
        )
        assert self.out_c.contains(expected_code_re)

    def test_funcs_are_correctly_marked_in_dsm(self):
        assert self.out_dsm.contains(r'; *function: main')
        assert self.out_dsm.contains(r'; *statically linked function: ___multadd_D2A')
        assert self.out_dsm.contains(r'; *statically linked function: ___main')

class UserAndSyscallTest(Test):
    """Tests that the generated functions are recognized as "user-defined" and
    "syscall", an put into proper sections in the generated C file.
    """

    settings = TestSettings(
        input='732-sample-1991.elf'
    )

    def test_funcs_are_separated_in_c_into_user_defined_and_syscalls(self):
        expected_code_re = re.compile("""
                -\ Functions\ -
                .*
                entry_point
                .*
                -\ System-Call\ Functions\ -
                .*
                accept
                .*
            """,
            flags=re.VERBOSE | re.DOTALL
        )
        assert self.out_c.contains(expected_code_re)

#class IdiomFromFrontendTest(Test):
    #"""Tests that the generated functions are recognized "idiom" by frontend,
    #an put into proper sections in the generated C file.
    #"""

    #settings = TestSettings(
        #input='idioms.arm.gcc.O0.exe',
    #)

    #def test_funcs_are_separated_into_idioms(self):
        #expected_code_re = re.compile("""
                #-\ Instruction-Idiom\ Functions\ -
                #.*
                #fabsf
                #.*
            #""",
            #flags=re.VERBOSE | re.DOTALL
        #)
        #assert self.out_c.contains(expected_code_re)
