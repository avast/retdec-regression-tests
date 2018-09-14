from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='gzip-strip',
        args='-k'  # TODO: matula, not sure if some functions are not called, or we just do not detect it.
    )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal( 'corrupted input -- file name too large' )
        assert self.out_c.has_string_literal( 'read from' )
        assert self.out_c.has_string_literal( '.gz' )
        assert self.out_c.has_string_literal( '\\n%s: %s: not in gzip format\\n' )
        assert self.out_c.has_string_literal( 'de' )
        assert self.out_c.has_string_literal( 'argc<=0' )
        assert self.out_c.has_string_literal( '.tgz' )
        assert self.out_c.has_string_literal( '\\n%s: %s: %s\\n' )
        assert self.out_c.has_string_literal( '.tar' )
        assert self.out_c.has_string_literal( '%s: %s is encrypted -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: not a valid zip file\\n' )
        assert self.out_c.has_string_literal( 'out of memory' )
        assert self.out_c.has_string_literal( '%s: %s: warning, name truncated\\n' )
        assert self.out_c.has_string_literal( '%s: %s is a a multi-part gzip file -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( '%9ld %9ld ' )
        assert self.out_c.has_string_literal( 'compressed  uncompr. ratio uncompressed_name' )
        assert self.out_c.has_string_literal( 'name too short' )
        assert self.out_c.has_string_literal( '.exe' )
        assert self.out_c.has_string_literal( '%s: %s: unknown suffix -- ignored\\n' )
        assert self.out_c.has_string_literal( 'usage: %s [-%scdfhlLnN%stvV19] [-S suffix] [file ...]\\n' )
        assert self.out_c.has_string_literal( '%s: %s has flags 0x%x -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( ' %s\\n' )
        assert self.out_c.has_string_literal( "%s: incorrect suffix '%s'\\n" )
        assert self.out_c.has_string_literal( 'gzcat' )
        assert self.out_c.has_string_literal( '.taz' )
        assert self.out_c.has_string_literal( '%s: %s has %d other link%c -- unchanged\\n' )
        assert self.out_c.has_string_literal( ' incomplete literal tree\\n' )
        assert self.out_c.has_string_literal( "can't recover suffix\\n" )
        assert self.out_c.has_string_literal( 'For help, type: %s -h\\n' )
        assert self.out_c.has_string_literal( '%s: ' )
        assert self.out_c.has_string_literal( '\\n%s: ' )
        assert self.out_c.has_string_literal( '%2ld.%1ld%%' )
        assert self.out_c.has_string_literal( '%s: %s: warning: %s%s\\n' )
        assert self.out_c.has_string_literal( 'bad pack level' )
        assert self.out_c.has_string_literal( '\\n%s: %s: decompression OK, trailing garbage ignored\\n' )
        assert self.out_c.has_string_literal( '%s: %s already has %s suffix -- unchanged\\n' )
        assert self.out_c.has_string_literal( 'gun' )
        assert self.out_c.has_string_literal( '%s: %s is a directory -- ignored\\n' )
        assert self.out_c.has_string_literal( '%s: %s: unknown method %d -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( 'un' )
        assert self.out_c.has_string_literal( '%s: %s is not a directory or a regular file - ignored\\n' )
        assert self.out_c.has_string_literal( 'fstat(stdin)' )
        assert self.out_c.has_string_literal( ' incomplete distance tree\\n' )
        assert self.out_c.has_string_literal( '%s: compressed data not %s a terminal. Use -f to force %scompression.\\n' )
        assert self.out_c.has_string_literal( 'written to' )
        assert self.out_c.has_string_literal( 'ab:cdfhH?lLmMnNqrS:tvVZ123456789' )
        assert self.out_c.has_string_literal( '%s: %s compressed to %s\\n' )
        assert self.out_c.has_string_literal( '\\tnot overwritten\\n' )
        assert self.out_c.has_string_literal( 'internal error in shorten_name' )
        assert self.out_c.has_string_literal( '%s: unexpected end of file\\n' )

    # Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
    #
    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( 'function_10000a9c' )  #
        assert self.out_c.has_func( 'entry_point' )  # function_10000af0
        assert self.out_c.has_func( 'function_10000b14' )  #
        assert self.out_c.has_func( 'function_10000bbc' )  #
        assert self.out_c.has_func( 'function_10000bd8' )  #
        assert self.out_c.has_func( 'function_10000c20' )  #
        assert self.out_c.has_func( 'function_10000c3c' )  #
        assert self.out_c.has_func( 'function_10000c7c' )  #
        assert self.out_c.has_func( 'function_10000cf8' )  #
        assert self.out_c.has_func( 'function_10000d44' )  #
        assert self.out_c.has_func( 'function_10000d8c' )  #
        assert self.out_c.has_func( 'function_10000f04' )  #
        assert self.out_c.has_func( 'function_10000f54' )  #
        assert self.out_c.has_func( 'function_10000ff8' )  #
        assert self.out_c.has_func( 'function_100011d0' )  #
        assert self.out_c.has_func( 'function_10001d1c' )  #
        assert self.out_c.has_func( 'function_1000208c' )  #
        assert self.out_c.has_func( 'main' )  #
        assert self.out_c.has_func( 'function_10003f88' )  #
        assert self.out_c.has_func( 'function_10004128' )  #
        assert self.out_c.has_func( 'function_100042c4' )  #
        assert self.out_c.has_func( 'function_10004550' )  #
        assert self.out_c.has_func( 'function_10004b24' )  #
        assert self.out_c.has_func( 'function_10004bc0' )  #
        assert self.out_c.has_func( 'function_10004ce8' )  #
        assert self.out_c.has_func( 'function_10004e80' )  #
        assert self.out_c.has_func( 'function_100050a4' )  #
        assert self.out_c.has_func( 'function_10005270' )  #
        assert self.out_c.has_func( 'function_10005328' )  #
        assert self.out_c.has_func( 'function_10005870' )  #
        assert self.out_c.has_func( 'function_10005b58' )  #
        assert self.out_c.has_func( 'function_10005ed8' )  #
        assert self.out_c.has_func( 'function_100060c8' )  #
        assert self.out_c.has_func( 'function_10006100' )  #
        assert self.out_c.has_func( 'function_10006240' )  #
        assert self.out_c.has_func( 'function_10006278' )  #
        assert self.out_c.has_func( 'function_10006398' )  #
        assert self.out_c.has_func( 'function_10006548' )  #
        assert self.out_c.has_func( 'function_10006c70' )  #
        assert self.out_c.has_func( 'function_10006cb4' )  #
        assert self.out_c.has_func( 'function_10007344' )  #
        assert self.out_c.has_func( 'function_1000785c' )  #
        assert self.out_c.has_func( 'function_10007ad4' )  #
        assert self.out_c.has_func( 'function_10007c30' )  #
        assert self.out_c.has_func( 'function_1000845c' )  #
        assert self.out_c.has_func( 'function_100085e0' )  #
        assert self.out_c.has_func( 'function_100086bc' )  #
        assert self.out_c.has_func( 'function_10008718' )  #
        assert self.out_c.has_func( 'function_10008748' )  #
        assert self.out_c.has_func( 'basename' )  #
        assert self.out_c.has_func( 'function_100087fc' )  #
        assert self.out_c.has_func( 'error' )  #
        assert self.out_c.has_func( 'warn' )  #
        assert self.out_c.has_func( 'function_10008920' )  #
        assert self.out_c.has_func( 'function_100089a0' )  #
        assert self.out_c.has_func( 'function_10008a94' )  #
        assert self.out_c.has_func( 'function_10008ae0' )  #
        assert self.out_c.has_func( 'function_10008b5c' )  #
        assert self.out_c.has_func( 'function_10008be0' )  # flush_outbuf
        assert self.out_c.has_func( 'function_10008c40' )  # copy
        assert self.out_c.has_func( 'function_10008d54' )  # display_ratio
        assert self.out_c.has_func( 'function_10008e2c' )  #
        assert self.out_c.has_func( 'function_10008e6c' )  #
        assert self.out_c.has_func( 'function_10009de8' )  #
        assert self.out_c.has_func( 'function_10009f18' )  #
        assert self.out_c.has_func( 'function_10009f54' )  #
        assert self.out_c.has_func( 'function_1000a268' )  #
        assert self.out_c.has_func( 'function_1000aa48' )  #
        assert self.out_c.has_func( 'function_100090a0' )  # lzw
        assert self.out_c.has_func( 'function_10009120' )  # unlzw
        assert self.out_c.has_func( 'function_100097a0' )  # unpack
        assert self.out_c.has_func( 'function_1000a46c' )  # unlzh
