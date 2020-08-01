from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='sgrep-strip',
        args='-k'
    )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal( '                  ' )
        assert self.out_c.has_string_literal( '                              \\r' )
        assert self.out_c.has_string_literal( '  %-18s%6.2fs %6.2fs %6.2fs\\n' )
        assert self.out_c.has_string_literal( '  -----------------------------------------\\n' )
        assert self.out_c.has_string_literal( ' %d gc blocks used, %d gc blocks allocated.\\n' )
        assert self.out_c.has_string_literal( ' %d gc lists, %d gc lists allocated\\n' )
        assert self.out_c.has_string_literal( ' %d same phrases\\n' )
        assert self.out_c.has_string_literal( ' %d sorts optimized\\n' )
        assert self.out_c.has_string_literal( ' %dK nest stack size, %dK inner tablesize\\n' )
        assert self.out_c.has_string_literal( ' -%c %s' )
        assert self.out_c.has_string_literal( ' Longest list size was %d regions.\\n' )
        assert self.out_c.has_string_literal( " ] 'expr' [<files...>]\\n" )
        assert self.out_c.has_string_literal( '%-18s%8s%8s%8s\\n' )
        assert self.out_c.has_string_literal( '%15s:%-4d%6s:%-4d%5s:%-4d%5s:%-4d%11s:%-4d%4s:%-4d\\n' )
        assert self.out_c.has_string_literal( '%15s:%-4d%6s:%-4d\\n' )
        assert self.out_c.has_string_literal( '%d' )
        assert self.out_c.has_string_literal( '%d\\n' )
        assert self.out_c.has_string_literal( '%s %d%% done%s\\r' )
        assert self.out_c.has_string_literal( '%s ( > %d ) %s %d\\n%s\\n%s\\n' )
        assert self.out_c.has_string_literal( '%s: short read\\n' )
        assert self.out_c.has_string_literal( '%s\\n' )
        assert self.out_c.has_string_literal( "'not' must be followed by 'in', 'containing' or 'equal'" )
        assert self.out_c.has_string_literal( '( expected' )
        assert self.out_c.has_string_literal( ') expected' )
        assert self.out_c.has_string_literal( '-' )
        assert self.out_c.has_string_literal( '-%c requires an argument\\n' )
        assert self.out_c.has_string_literal( '--' )
        assert self.out_c.has_string_literal( '------------- #%n %f: %l (%s,%e : %i,%j)\\\\n%r\\\\n' )
        assert self.out_c.has_string_literal( '/use/local/lib/sgreprc' )
        assert self.out_c.has_string_literal( '0.99' )
        assert self.out_c.has_string_literal( '<input exceeded>' )
        assert self.out_c.has_string_literal( '<stdin>' )
        assert self.out_c.has_string_literal( 'Aug 28 2014' )
        assert self.out_c.has_string_literal( 'Basic expression expected\\n' )
        assert self.out_c.has_string_literal( 'Command file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'Copyright (C) 1996  University of Helsinki' )
        assert self.out_c.has_string_literal( 'Either you have forgotten the quote  at the end of phrase or' )
        assert self.out_c.has_string_literal( 'Empty command file %s\\n' )
        assert self.out_c.has_string_literal( 'Empty phrase' )
        assert self.out_c.has_string_literal( 'Empty stdin\\n' )
        assert self.out_c.has_string_literal( 'Empty style file %s\\n' )
        assert self.out_c.has_string_literal( 'Expression too long (>%d)\\n' )
        assert self.out_c.has_string_literal( 'File %s truncated before search\\n' )
        assert self.out_c.has_string_literal( 'HOME' )
        assert self.out_c.has_string_literal( 'If no files are given stdin is used instead.' )
        assert self.out_c.has_string_literal( 'Illegal option -%c\\n' )
        assert self.out_c.has_string_literal( 'Inbuilt preprocessor not implemented yet.\\n' )
        assert self.out_c.has_string_literal( 'Invalid SGREPOPT (SGREPOPT=%s)\\n' )
        assert self.out_c.has_string_literal( 'Invalid character' )
        assert self.out_c.has_string_literal( 'Memory allocation failed.\\n' )
        assert self.out_c.has_string_literal( 'Memory:\\n %dK memory allocated, %d realloc operations\\n' )
        assert self.out_c.has_string_literal( 'No files or expressions allowed in SGREPOPT\\n' )
        assert self.out_c.has_string_literal( 'No valid files\\n' )
        assert self.out_c.has_string_literal( 'Operations:\\n%15s:%-4d%6s:%-4d%5s:%-4d%5s:%-4d%11s:%-4d%3s:%-4d\\n' )
        assert self.out_c.has_string_literal( 'Operator expected' )
        assert self.out_c.has_string_literal( 'Operator tree size was %d, optimized %d\\n' )
        assert self.out_c.has_string_literal( 'Options can also be specified with SGREPOPT environment variable' )
        assert self.out_c.has_string_literal( 'Output list size was %d regions.\\n' )
        assert self.out_c.has_string_literal( 'Parse error on line %d column %d :\\n\\t%s\\n%s\\n' )
        assert self.out_c.has_string_literal( 'Phrase length exceeds' )
        assert self.out_c.has_string_literal( "Premature end of parsing. ( This shouldn't happen!! )\\n" )
        assert self.out_c.has_string_literal( 'Read command file' )
        assert self.out_c.has_string_literal( 'SGREPOPT' )
        assert self.out_c.has_string_literal( 'Scanned %d files, having total of %dK size finding %d phrases.\\n' )
        assert self.out_c.has_string_literal( "Stdin already read, Can't read expressions from stdin\\n" )
        assert self.out_c.has_string_literal( 'Strange expression type\\n' )
        assert self.out_c.has_string_literal( 'Things done:\\n %d %s, %d %s, %d %s\\n %d %s, %d %s\\n' )
        assert self.out_c.has_string_literal( 'Too complex SGREPOPT\\n' )
        assert self.out_c.has_string_literal( "Too many )'s" )
        assert self.out_c.has_string_literal( 'Unexpected end of expression' )
        assert self.out_c.has_string_literal( 'Unknown word' )
        assert self.out_c.has_string_literal( 'Unprintable character in phrase' )
        assert self.out_c.has_string_literal( 'Unsupported operation in parse tree (%d)\\n' )
        assert self.out_c.has_string_literal( 'Unterminated phrase' )
        assert self.out_c.has_string_literal( 'Unterminated phrase string' )
        assert self.out_c.has_string_literal( "Usage: sgrep <options> 'region expression' [<files...>]" )
        assert self.out_c.has_string_literal( 'Warning: region end point greater than input size detected\\n' )
        assert self.out_c.has_string_literal( 'Warning: region start point greater than input size detected\\n' )
        assert self.out_c.has_string_literal( "You have to give an expression line if you don't use -f or -e switch.\\n" )
        assert self.out_c.has_string_literal( '\\nCopyright (C) 1996 University of Helsinki. Use sgrep -C for details,\\n' )
        assert self.out_c.has_string_literal( '\\noptions are:' )
        assert self.out_c.has_string_literal( '\\t%s\\n' )
        assert self.out_c.has_string_literal( '\\t-%c %s\\t%s\\n' )
        assert self.out_c.has_string_literal( '\\t--\\t\\tno more options' )
        assert self.out_c.has_string_literal( 'acsearch' )
        assert self.out_c.has_string_literal( 'common.c' )
        assert self.out_c.has_string_literal( 'concat' )
        assert self.out_c.has_string_literal( 'containing' )
        assert self.out_c.has_string_literal( 'equal' )
        assert self.out_c.has_string_literal( 'eval.c' )
        assert self.out_c.has_string_literal( 'evaluating' )
        assert self.out_c.has_string_literal( 'extracting' )
        assert self.out_c.has_string_literal( 'fork' )
        assert self.out_c.has_string_literal( 'gc lists scanned' )
        assert self.out_c.has_string_literal( 'in' )
        assert self.out_c.has_string_literal( 'inner' )
        assert self.out_c.has_string_literal( 'invalid constant region list' )
        assert self.out_c.has_string_literal( 'join' )
        assert self.out_c.has_string_literal( 'join expected comma: join(NUMBER,expression)' )
        assert self.out_c.has_string_literal( 'join needs a number: join(NUMBER,expression)' )
        assert self.out_c.has_string_literal( 'join number must be >= 1' )
        assert self.out_c.has_string_literal( 'lseek %s: %s\\n' )
        assert self.out_c.has_string_literal( 'lseek <stdin>' )
        assert self.out_c.has_string_literal( 'lseek style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'not containing' )
        assert self.out_c.has_string_literal( 'not equal' )
        assert self.out_c.has_string_literal( 'not in' )
        assert self.out_c.has_string_literal( 'on line' )
        assert self.out_c.has_string_literal( 'open %s: %s\\n' )
        assert self.out_c.has_string_literal( 'open style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'or' )
        assert self.out_c.has_string_literal( 'order' )
        assert self.out_c.has_string_literal( 'outer' )
        assert self.out_c.has_string_literal( 'output' )
        assert self.out_c.has_string_literal( 'output.c' )
        assert self.out_c.has_string_literal( 'parsing' )
        assert self.out_c.has_string_literal( 'pmatch.c' )
        assert self.out_c.has_string_literal( 'preproc.c' )
        assert self.out_c.has_string_literal( 'preprocessor' )
        assert self.out_c.has_string_literal( 'quote' )
        assert self.out_c.has_string_literal( 'read %s: %s\\n' )
        assert self.out_c.has_string_literal( 'read <stdin>' )
        assert self.out_c.has_string_literal( 'read style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'regions created' )
        assert self.out_c.has_string_literal( 'regions scanned' )
        assert self.out_c.has_string_literal( 'sgrep -h for help\\n' )
        assert self.out_c.has_string_literal( 'sgrep time usage' )
        assert self.out_c.has_string_literal( 'sgrep version %s compiled at %s\\n' )
        assert self.out_c.has_string_literal( 'sgrep version 0.99 - search a file for structured pattern' )
        assert self.out_c.has_string_literal( 'sgrep: %s: %s\\n' )
        assert self.out_c.has_string_literal( 'sgrep: lseek tmpfile' )
        assert self.out_c.has_string_literal( 'short read <stdin>' )
        assert self.out_c.has_string_literal( 'sorts by end point' )
        assert self.out_c.has_string_literal( 'sorts by start point' )
        assert self.out_c.has_string_literal( 'sys' )
        assert self.out_c.has_string_literal( 'too many expressions. (-e and -f options more than %d)\\n' )
        assert self.out_c.has_string_literal( 'total' )
        assert self.out_c.has_string_literal( 'usr' )
        assert self.out_c.has_string_literal( 'you have to recompile with greater MAX_PHRASE_LENGTH.' )
        assert self.out_c.has_string_literal( 'optimize.c' )

    # Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
    #
    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( 'function_8900018' )  #
        assert self.out_c.has_func( 'entry_point' )  # function_890003c
        assert self.out_c.has_func( 'function_8900180' )  #
        assert self.out_c.has_func( 'function_8900228' )  #
        assert self.out_c.has_func( 'function_89002e4' )  #
        assert self.out_c.has_func( 'function_89002f8' )  #
        assert self.out_c.has_func( 'function_8900354' )  #
        assert self.out_c.has_func( 'function_8902878' )  #
        assert self.out_c.has_func( 'function_89028d4' )  #
        assert self.out_c.has_func( 'function_8902930' )  #
        assert self.out_c.has_func( 'function_8902a0c' )  #
        assert self.out_c.has_func( 'function_8902d3c' )  #
        assert self.out_c.has_func( 'function_8902dd0' )  #
        assert self.out_c.has_func( 'function_8902e84' )  #
        assert self.out_c.has_func( 'function_8903118' )  #
        assert self.out_c.has_func( 'function_8903244' )  #
        assert self.out_c.has_func( 'function_8903498' )  #
        assert self.out_c.has_func( 'function_890360c' )  #
        assert self.out_c.has_func( 'function_89037f4' )  #
        assert self.out_c.has_func( 'function_890381c' )  #
        assert self.out_c.has_func( 'function_890398c' )  #
        assert self.out_c.has_func( 'function_8903a10' )  #
        assert self.out_c.has_func( 'function_8903ab8' )  #
        assert self.out_c.has_func( 'function_8903ec0' )  #
        assert self.out_c.has_func( 'function_8904040' )  #
        assert self.out_c.has_func( 'function_890418c' )  #
        assert self.out_c.has_func( 'main' )  #
        assert self.out_c.has_func( 'function_8904a44' )  #
        assert self.out_c.has_func( 'function_8904b24' )  #
        assert self.out_c.has_func( 'function_8904c44' )  #
        assert self.out_c.has_func( 'function_8904f90' )  #
        assert self.out_c.has_func( 'function_8905180' )  #
        assert self.out_c.has_func( 'function_8905304' )  #
        assert self.out_c.has_func( 'function_89053c4' )  #
        assert self.out_c.has_func( 'function_8905574' )  #
        assert self.out_c.has_func( 'function_89055f8' )  #
        assert self.out_c.has_func( 'function_890565c' )  #
        assert self.out_c.has_func( 'function_89056d0' )  #
        assert self.out_c.has_func( 'function_8905768' )  #
        assert self.out_c.has_func( 'function_8905800' )  #
        assert self.out_c.has_func( 'function_8905864' )  #
        assert self.out_c.has_func( 'function_8905aa0' )  #
        assert self.out_c.has_func( 'function_8905af4' )  #
        assert self.out_c.has_func( 'function_8905b94' )  #
        assert self.out_c.has_func( 'function_8905c18' )  #
        assert self.out_c.has_func( 'function_8905c4c' )  #
        assert self.out_c.has_func( 'function_8905ca8' )  #
        assert self.out_c.has_func( 'function_8905d30' )  #
        assert self.out_c.has_func( 'function_8905d84' )  #
        assert self.out_c.has_func( 'function_8905dd8' )  #
        assert self.out_c.has_func( 'function_8905f14' )  #
        assert self.out_c.has_func( 'function_8906684' )  #
        assert self.out_c.has_func( 'function_890685c' )  #
        assert self.out_c.has_func( 'function_8906a60' )  #
        assert self.out_c.has_func( 'function_8906adc' )  #
        assert self.out_c.has_func( 'function_8906e3c' )  #
        assert self.out_c.has_func( 'function_8906ef8' )  #
        assert self.out_c.has_func( 'function_8906f60' )  #
        assert self.out_c.has_func( 'function_890702c' )  #
        assert self.out_c.has_func( 'function_890712c' )  #
        assert self.out_c.has_func( 'function_89071f0' )  #
        assert self.out_c.has_func( 'function_8907214' )  #
        assert self.out_c.has_func( 'function_89074c0' )  #
        assert self.out_c.has_func( 'function_89075a0' )  #
        assert self.out_c.has_func( 'function_8907768' )  #
        assert self.out_c.has_func( 'function_89077c4' )  #
        assert self.out_c.has_func( 'function_8907824' )  #
        assert self.out_c.has_func( 'function_8907994' )  #
        assert self.out_c.has_func( 'function_89079fc' )  #
        assert self.out_c.has_func( 'function_8907b78' )  #
        assert self.out_c.has_func( 'function_8907c08' )  #
        assert self.out_c.has_func( 'function_8907e60' )  #
        assert self.out_c.has_func( 'function_89081b0' )  #
        assert self.out_c.has_func( 'function_8908308' )  #
        assert self.out_c.has_func( 'function_8908398' )  #
        assert self.out_c.has_func( 'function_89083f8' )  #
        assert self.out_c.has_func( 'function_89086c4' )  #
        assert self.out_c.has_func( 'function_8908944' )  #
        assert self.out_c.has_func( 'function_8908aa0' )  #
        assert self.out_c.has_func( 'function_8908e54' )  #
        assert self.out_c.has_func( 'function_89091a8' )  #
        assert self.out_c.has_func( 'function_8909550' )  #
        assert self.out_c.has_func( 'function_890987c' )  #
        assert self.out_c.has_func( 'function_8909aa4' )  #
        assert self.out_c.has_func( 'function_8909f44' )  #
        assert self.out_c.has_func( 'function_890a2cc' )  #
        assert self.out_c.has_func( 'function_890a468' )  #
        assert self.out_c.has_func( 'function_890a61c' )  #
        assert self.out_c.has_func( 'function_890a840' )  #
        assert self.out_c.has_func( 'function_890ae6c' )  #
        assert self.out_c.has_func( 'function_890af20' )  #
        assert self.out_c.has_func( 'function_890b02c' )  #
        assert self.out_c.has_func( 'function_890b358' )  #
        assert self.out_c.has_func( 'function_890b440' )  #
        assert self.out_c.has_func( 'function_890b818' )  #
        assert self.out_c.has_func( 'function_891c0b0' )  #
        assert self.out_c.has_func( 'function_891c100' )  #
        assert self.out_c.has_func( 'function_891c114' )  #
        assert self.out_c.has_func( 'function_891c188' )  #
        assert self.out_c.has_func( 'function_891c190' )  #
        assert self.out_c.has_func( 'sceIoDopen' )  # function_891c130
        assert self.out_c.has_func( 'function_8904b6c' )  # end_first
        assert self.out_c.has_func( 'function_8904bd8' )  # start_first
        assert self.out_c.has_func( 'function_8904e84' )  # give_oper_name

    def test_check_for_all_currently_detected_statically_linked_functions(self):
        assert self.out_config.is_statically_linked('atexit', 0x8900368)
        assert self.out_config.is_statically_linked('__errno', 0x8900cb8)
        assert self.out_config.is_statically_linked('realloc', 0x890e01c)
