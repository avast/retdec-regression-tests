from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='strp-strip',
        args='-k'
    )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal( ' Copyright(c) 1996, 1998 by ' )
        assert self.out_c.has_string_literal( '%s%s%s%s' )
        assert self.out_c.has_string_literal( '0.9' )
        assert self.out_c.has_string_literal( 'Eddie Buckley <eddie@sjfn.nb.ca>\\n' )
        assert self.out_c.has_string_literal( 'Fix line breaks in FILE(s), or standard input to standard output.' )
        assert self.out_c.has_string_literal( "Try `%s -h' for more information.\\n" )
        assert self.out_c.has_string_literal( 'Usage: %s [OPTION] [FILE]...\\n' )
        assert self.out_c.has_string_literal( '\\nIf more than one command line option is present only the first one is used.' )
        assert self.out_c.has_string_literal( '\\nWith no FILE or when FILE is - read from standard input and write to standard\\n output.\\n' )
        assert self.out_c.has_string_literal( '\\n\\t-d\\tmake DOS format (CR-LF)' )
        assert self.out_c.has_string_literal( '\\t-h\\tshow this help and version number' )
        assert self.out_c.has_string_literal( '\\t-m\\tmake MAC/Amiga format (CR)' )
        assert self.out_c.has_string_literal( '\\t-u\\tmake UNIX format (LF)' )
        assert self.out_c.has_string_literal( '\\t-v\\tprint version number and exit' )
        assert self.out_c.has_string_literal( 'strp version ' )
        assert self.out_c.has_string_literal( 'usage %s %s\\n' )

    # Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
    #
    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( 'function_100003e8' )  # _init
        assert self.out_c.has_func( 'entry_point' )  # function_10000440
        assert self.out_c.has_func( 'function_10000528' )  # frame_dummy
        assert self.out_c.has_func( 'function_1000068c' )  # ver
        assert self.out_c.has_func( 'function_100006d8' )  # help
        assert self.out_c.has_func( 'function_1000083c' )  # try
        assert self.out_c.has_func( 'function_10000878' )  # usage
        assert self.out_c.has_func( 'main' )  # main
        assert self.out_c.has_func( 'function_10000a30' )  # __do_global_ctors_aux
        assert self.out_c.has_func( 'function_1000050c' )  # call___do_global_dtors_aux
        assert self.out_c.has_func( 'function_10000570' )  # call_frame_dummy
        assert self.out_c.has_func( 'function_1000058c' )  # to_unix
        assert self.out_c.has_func( 'function_100005dc' )  # to_dos, or function_100005e0
        assert self.out_c.has_func( 'function_10000640' )  # to_mac
        assert self.out_c.has_func( 'function_10000754' )  # arg_parse
        assert self.out_c.has_func( 'function_100007fc' )  # isdir
        assert self.out_c.has_func( 'function_10000978' )  # __libc_csu_init
        assert self.out_c.has_func( 'function_10000a80' )  # call___do_global_ctors_aux
        assert self.out_c.has_func( 'function_10000b90' )  # _fini
