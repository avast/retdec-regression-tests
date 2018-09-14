from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='sed-strip',
        args='-k'
    )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal('sed: RE too long: %s\\n')
        assert self.out_c.has_string_literal('sed: garbled command %s\\n')
        assert self.out_c.has_string_literal('sed: undefined label %s\\n')
        assert self.out_c.has_string_literal('sed: too much text: %s\\n')
        assert self.out_c.has_string_literal('sed: first RE must be non-null\\n')
        assert self.out_c.has_string_literal('sed: no such command as %s\\n')
        assert self.out_c.has_string_literal('sed: cannot open command-file %s\\n')
        assert self.out_c.has_string_literal('sed: too many {\'s\\n')
        assert self.out_c.has_string_literal('sed: RE error, %o\\n')
        assert self.out_c.has_string_literal('sed: line too long\\n')
        assert self.out_c.has_string_literal('%02x')
        assert self.out_c.has_string_literal('sed: ')
        assert self.out_c.has_string_literal('line %D')
        assert self.out_c.has_string_literal('hold space')
        assert self.out_c.has_string_literal(' truncated to %d characters\\n')
        assert self.out_c.has_string_literal('r')
        assert self.out_c.has_string_literal('%ld\\n')
        assert self.out_c.has_string_literal('sed: too many appends after line %ld\\n')
        assert self.out_c.has_string_literal('sed: too many reads after line %ld\\n')
        assert self.out_c.has_string_literal('%s\\n')
        assert self.out_c.has_string_literal('sed: can\'t open %s\\n')

    # Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
    #
    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( 'function_8900018' )  # _init
        assert self.out_c.has_func( 'entry_point' )  # function_890003c _start
        assert self.out_c.has_func( 'function_8900180' )  # _main
        assert self.out_c.has_func( 'function_89002f8' )  # frame_dummy
        assert self.out_c.has_func( 'function_8900368' )  # rhscomp
        assert self.out_c.has_func( 'function_89005d0' )  # resolve
        assert self.out_c.has_func( 'function_890068c' )  # recomp
        assert self.out_c.has_func( 'function_8900b98' )  # address
        assert self.out_c.has_func( 'function_8900c98' )  # compile
        assert self.out_c.has_func( 'function_8901010' )  # search
        assert self.out_c.has_func( 'main' )  # main
        assert self.out_c.has_func( 'function_8902890' )  # advance
        assert self.out_c.has_func( 'function_8902c28' )  # match
        assert self.out_c.has_func( 'function_8903704' )  # selected
        assert self.out_c.has_func( 'function_890252c' )  # place
        assert self.out_c.has_func( 'function_89025f4' )  # dosub
        assert self.out_c.has_func( 'function_8902d70' )  # substitute
        assert self.out_c.has_func( 'function_8901ffc' )  # listto
        assert self.out_c.has_func( 'function_8902804' )  # truncated
        assert self.out_c.has_func( 'function_8901cb0' )  # readout
        assert self.out_c.has_func( 'function_8902e04' )  # command
        assert self.out_c.has_func( 'function_890386c' )  # execute
        assert self.out_c.has_func( 'function_8901e6c' )  # getline
        assert self.out_c.has_func( 'function_8901ee0' )  # dumpto
        assert self.out_c.has_func( 'function_89004b4' )  # ycomp
        assert self.out_c.has_func( 'function_8900354' )  # call_frame_dummy
        assert self.out_c.has_func( 'function_890107c' )  # cmdline
        assert self.out_c.has_func( 'function_8901230' )  # cmdcomp
