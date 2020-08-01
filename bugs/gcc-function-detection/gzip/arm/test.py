from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='gzip-strip',
        args='-k'  # TODO: matula, not sure if some functions are not called, or we just do not detect it.
    )

    def test_check_for_all_currently_detected_strings(self):
        #assert self.out_c.has_string_literal( '' )
        assert self.out_c.has_string_literal( '                            %9lu %9lu ' )
        assert self.out_c.has_string_literal( '   Copyright (C) 1992-1993 Jean-loup Gailly' )
        assert self.out_c.has_string_literal( '   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.' )
        assert self.out_c.has_string_literal( '   GNU General Public License for more details.' )
        assert self.out_c.has_string_literal( '   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the' )
        assert self.out_c.has_string_literal( '   This program is distributed in the hope that it will be useful,' )
        assert self.out_c.has_string_literal( '   This program is free software; you can redistribute it and/or modify' )
        assert self.out_c.has_string_literal( '   You should have received a copy of the GNU General Public License' )
        assert self.out_c.has_string_literal( '   along with this program; if not, write to the Free Software' )
        assert self.out_c.has_string_literal( '   any later version.' )
        assert self.out_c.has_string_literal( '   but WITHOUT ANY WARRANTY; without even the implied warranty of' )
        assert self.out_c.has_string_literal( '   it under the terms of the GNU General Public License as published by' )
        assert self.out_c.has_string_literal( '   the Free Software Foundation; either version 2, or (at your option)' )
        assert self.out_c.has_string_literal( ' %s\\n' )
        assert self.out_c.has_string_literal( ' (totals)' )
        assert self.out_c.has_string_literal( ' -1 --fast        compress faster' )
        assert self.out_c.has_string_literal( ' -9 --best        compress better' )
        assert self.out_c.has_string_literal( ' -L --license     display software license' )
        assert self.out_c.has_string_literal( ' -N --name        save or restore the original name and time stamp' )
        assert self.out_c.has_string_literal( ' -S .suf  --suffix .suf     use suffix .suf on compressed files' )
        assert self.out_c.has_string_literal( ' -V --version     display version number' )
        assert self.out_c.has_string_literal( ' -c --stdout      write on standard output, keep original files unchanged' )
        assert self.out_c.has_string_literal( ' -d --decompress  decompress' )
        assert self.out_c.has_string_literal( ' -f --force       force overwrite of output file and compress links' )
        assert self.out_c.has_string_literal( ' -h --help        give this help' )
        assert self.out_c.has_string_literal( ' -l --list        list compressed file contents' )
        assert self.out_c.has_string_literal( ' -n --no-name     do not save or restore the original name and time stamp' )
        assert self.out_c.has_string_literal( ' -q --quiet       suppress all warnings' )
        assert self.out_c.has_string_literal( ' -t --test        test compressed file integrity' )
        assert self.out_c.has_string_literal( ' -v --verbose     verbose mode' )
        assert self.out_c.has_string_literal( ' \\t' )
        assert self.out_c.has_string_literal( ' do you wish to overwrite (y or n)? ' )
        assert self.out_c.has_string_literal( ' file...          files to (de)compress. If none given, use standard input.' )
        # The following two strings are not found in the generated C after a
        # switch to LLVM 3.6. The reason is that opt generates slightly
        # different code that back-end does not restructure correctly. We
        # should improve the structuring, but this is a task for a more time
        # than we have at the moment.
        assert self.out_c.has_string_literal( ' incomplete distance tree\\n' )
        assert self.out_c.has_string_literal( ' incomplete literal tree\\n' )
        assert self.out_c.has_string_literal( '%2ld.%1ld%%' )
        assert self.out_c.has_string_literal( '%5s %08lx %11s ' )
        assert self.out_c.has_string_literal( '%9ld %9ld ' )
        assert self.out_c.has_string_literal( '%s %s (%s)\\n' )
        assert self.out_c.has_string_literal( '%s: %s already exists;' )
        assert self.out_c.has_string_literal( '%s: %s compressed to %s\\n' )
        assert self.out_c.has_string_literal( '%s: %s has flags 0x%x -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( '%s: %s has more than one entry -- unchanged\\n' )
        assert self.out_c.has_string_literal( '%s: %s has more than one entry--rest ignored\\n' )
        assert self.out_c.has_string_literal( '%s: %s is a a multi-part gzip file -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( '%s: %s is encrypted -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( '%s: %s: extra field of %u bytes ignored\\n' )
        assert self.out_c.has_string_literal( '%s: %s: part number %u\\n' )
        assert self.out_c.has_string_literal( '%s: %s: unknown method %d -- get newer version of gzip\\n' )
        assert self.out_c.has_string_literal( '%s: %s: warning, name truncated\\n' )
        assert self.out_c.has_string_literal( '%s: %s: warning: %s%s\\n' )
        assert self.out_c.has_string_literal( '%s: -Z not supported in this version\\n' )
        assert self.out_c.has_string_literal( '%s: -r not supported on this system\\n' )
        assert self.out_c.has_string_literal( '%s: compressed data not %s a terminal. Use -f to force %scompression.\\n' )
        assert self.out_c.has_string_literal( '%s: illegal option -- %c\\n' )
        assert self.out_c.has_string_literal( "%s: option `%c%s' doesn't allow an argument\\n" )
        assert self.out_c.has_string_literal( "%s: option `%s' is ambiguous\\n" )
        assert self.out_c.has_string_literal( "%s: option `%s' requires an argument\\n" )
        assert self.out_c.has_string_literal( "%s: option `--%s' doesn't allow an argument\\n" )
        assert self.out_c.has_string_literal( '%s: unexpected end of file\\n' )
        assert self.out_c.has_string_literal( "%s: unrecognized option `%c%s'\\n" )
        assert self.out_c.has_string_literal( "%s: unrecognized option `--%s'\\n" )
        assert self.out_c.has_string_literal( '%s:\\t%s' )
        assert self.out_c.has_string_literal( '%s\\n' )
        assert self.out_c.has_string_literal( '--' )
        assert self.out_c.has_string_literal( '.' )
        assert self.out_c.has_string_literal( '.exe' )
        assert self.out_c.has_string_literal( '.gz' )
        assert self.out_c.has_string_literal( '.tar' )
        assert self.out_c.has_string_literal( '.taz' )
        assert self.out_c.has_string_literal( '.tgz' )
        assert self.out_c.has_string_literal( '1.2.4' )
        assert self.out_c.has_string_literal( '18 Aug 93' )
        assert self.out_c.has_string_literal( 'Compilation options:\\n%s %s ' )
        assert self.out_c.has_string_literal( 'For help, type: %s -h\\n' )
        assert self.out_c.has_string_literal( 'GZIP' )
        assert self.out_c.has_string_literal( 'HAVE_UNISTD_H ' )
        assert self.out_c.has_string_literal( 'NO_DIR' )
        assert self.out_c.has_string_literal( 'NO_MEMORY_H ' )
        assert self.out_c.has_string_literal( 'POSIXLY_CORRECT' )
        assert self.out_c.has_string_literal( 'UTIME' )
        assert self.out_c.has_string_literal( '\\n%s: ' )
        assert self.out_c.has_string_literal( '\\n%s: %s: %s\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: compressed with %d bits, can only handle %d bits\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: decompression OK, trailing garbage ignored\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: encrypted file -- use unzip\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: first entry not deflated or stored -- use unzip\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: not a valid zip file\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: not in gzip format\\n' )
        assert self.out_c.has_string_literal( '\\n%s: %s: warning, unknown flags 0x%x\\n' )
        assert self.out_c.has_string_literal( '\\tnot overwritten\\n' )
        assert self.out_c.has_string_literal( 'cat' )
        assert self.out_c.has_string_literal( 'compr' )
        assert self.out_c.has_string_literal( 'compressed  uncompr. ratio uncompressed_name' )
        assert self.out_c.has_string_literal( 'corrupted input -- file name too large' )
        assert self.out_c.has_string_literal( 'de' )
        assert self.out_c.has_string_literal( 'defla' )
        assert self.out_c.has_string_literal( 'gun' )
        assert self.out_c.has_string_literal( 'gzcat' )
        assert self.out_c.has_string_literal( 'internal error, invalid method' )
        assert self.out_c.has_string_literal( 'invalid compressed data--format violated' )
        assert self.out_c.has_string_literal( 'invalid compressed data--length mismatch' )
        assert self.out_c.has_string_literal( 'len %ld, siz %ld\\n' )
        assert self.out_c.has_string_literal( 'lzh  ' )
        assert self.out_c.has_string_literal( 'out of memory' )
        assert self.out_c.has_string_literal( 'output in compress .Z format not supported\\n' )
        assert self.out_c.has_string_literal( 'pack ' )
        assert self.out_c.has_string_literal( 'store' )
        assert self.out_c.has_string_literal( 'un' )
        assert self.out_c.has_string_literal( 'usage: %s [-%scdfhlLnN%stvV19] [-S suffix] [file ...]\\n' )
        assert self.out_c.has_string_literal( 'z' )
        assert self.out_c.has_string_literal( 'ab:cdfhH?lLmMnNqrS:tvVZ123456789' )

    # Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
    #
    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( '_init' )  # function_8000
        assert self.out_c.has_func( 'function_8020' )  #
        assert self.out_c.has_func( 'function_80b0' )  #
        assert self.out_c.has_func( 'entry_point' )  # function_810c
        assert self.out_c.has_func( 'function_8218' )  #
        assert self.out_c.has_func( 'function_82a8' )  #
        assert self.out_c.has_func( 'function_831c' )  #
        assert self.out_c.has_func( 'function_835c' )  #
        assert self.out_c.has_func( 'function_83a0' )  #
        assert self.out_c.has_func( 'function_84b0' )  #
        assert self.out_c.has_func( 'function_84d8' )  #
        assert self.out_c.has_func( 'function_8560' )  #
        assert self.out_c.has_func( 'function_86ec' )  #
        assert self.out_c.has_func( 'function_917c' )  #
        assert self.out_c.has_func( 'function_94a8' )  #
        assert self.out_c.has_func( 'main' )  #
        assert self.out_c.has_func( 'function_ae48' )  #
        assert self.out_c.has_func( 'function_b268' )  #
        assert self.out_c.has_func( 'function_b4d4' )  #
        assert self.out_c.has_func( 'function_b670' )  #
        assert self.out_c.has_func( 'function_bbdc' )  #
        assert self.out_c.has_func( 'function_bd50' )  #
        assert self.out_c.has_func( 'function_bdf4' )  #
        assert self.out_c.has_func( 'function_bf0c' )  #
        assert self.out_c.has_func( 'function_c060' )  #
        assert self.out_c.has_func( 'function_c23c' )  #
        assert self.out_c.has_func( 'function_c404' )  #
        assert self.out_c.has_func( 'function_c57c' )  #
        assert self.out_c.has_func( 'function_c620' )  #
        assert self.out_c.has_func( 'function_cb2c' )  #
        assert self.out_c.has_func( 'function_ce64' )  #
        assert self.out_c.has_func( 'function_d1a8' )  #
        assert self.out_c.has_func( 'function_d1dc' )  #
        assert self.out_c.has_func( 'function_d204' )  #
        assert self.out_c.has_func( 'function_d304' )  #
        assert self.out_c.has_func( 'function_d46c' )  #
        assert self.out_c.has_func( 'function_d57c' )  #
        assert self.out_c.has_func( 'function_dbd4' )  #
        assert self.out_c.has_func( 'function_de00' )  #
        assert self.out_c.has_func( 'function_e2d0' )  #
        assert self.out_c.has_func( 'function_e2f8' )  #
        assert self.out_c.has_func( 'function_ea28' )  #
        assert self.out_c.has_func( 'function_f1d8' )  #
        assert self.out_c.has_func( 'function_f360' )  #
        assert self.out_c.has_func( 'function_f49c' )  #
        assert self.out_c.has_func( 'function_f544' )  #
        assert self.out_c.has_func( 'function_f5ac' )  #
        assert self.out_c.has_func( 'function_f5f0' )  #
        assert self.out_c.has_func( 'function_f640' )  #
        assert self.out_c.has_func( 'function_f874' )  #
        assert self.out_c.has_func( 'function_f8b4' )  #
        assert self.out_c.has_func( 'function_f900' )  #
        assert self.out_c.has_func( 'function_f920' )  #
        assert self.out_c.has_func( 'function_f990' )  #
        assert self.out_c.has_func( 'function_fb84' )  #
        assert self.out_c.has_func( 'function_fba4' )  #
        assert self.out_c.has_func( 'function_fbe8' )  #
        assert self.out_c.has_func( 'function_fc64' )  #
        assert self.out_c.has_func( 'function_fcbc' )  #
        assert self.out_c.has_func( 'function_10a18' )  #
        assert self.out_c.has_func( 'function_10adc' )  #
        assert self.out_c.has_func( 'function_10b00' )  #
        assert self.out_c.has_func( 'function_10d94' )  #
        assert self.out_c.has_func( 'function_11364' )  #
        assert self.out_c.has_func( 'function_1138c' )  #
        assert self.out_c.has_func( 'function_113c0' )  #
        assert self.out_c.has_func( 'function_11484' )  #
        assert self.out_c.has_func( 'function_1a6b4' )  #
        assert self.out_c.has_func( 'function_1ec3c' )  #
        assert self.out_c.has_func( 'function_ade0' )  # file_read
        assert self.out_c.has_func( 'function_d718' )  # unzip
        assert self.out_c.has_func( 'function_f7fc' )  # warn
        assert self.out_c.has_func( 'function_fb44' )  # make_simple_name
        assert self.out_c.has_func( 'function_fd84' )  # copy
        assert self.out_c.has_func( 'function_fe40' )  # lzw
        assert self.out_c.has_func( 'function_fea8' )  # unlzw
        assert self.out_c.has_func( 'function_10518' )  # unpack
        assert self.out_c.has_func( 'function_10f10' )  # unlzh
        #assert self.out_c.has_func( 'function_11cf0' )  # statically linked
        #assert self.out_c.has_func( 'function_1210c' )  # statically linked
        #assert self.out_c.has_func( 'function_1211c' )  # statically linked __errno
        #assert self.out_c.has_func( 'function_14218' )  #
        #assert self.out_c.has_func( 'function_149dc' )  #
        #assert self.out_c.has_func( 'function_162a8' )  #
        #assert self.out_c.has_func( 'function_162e4' )  # statically linked
        #assert self.out_c.has_func( 'function_1a020' )  # statically linked __env_lock
        #assert self.out_c.has_func( 'function_1a024' )  #
