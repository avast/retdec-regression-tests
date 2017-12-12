from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='gzip-strip',
		args='-k'  # TODO: matula, not sure if some functions are not called, or we just do not detect it.
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( '                            %9lu %9lu ' )
		assert self.out_c.has_string_literal( '   Copyright (C) 1992-1993 Jean-loup Gailly' )
		assert self.out_c.has_string_literal( '   This program is free software; you can redistribute it and/or modify' )
		assert self.out_c.has_string_literal( '   any later version.' )
		assert self.out_c.has_string_literal( '   it under the terms of the GNU General Public License as published by' )
		assert self.out_c.has_string_literal( '   the Free Software Foundation; either version 2, or (at your option)' )
		assert self.out_c.has_string_literal( ' %s\\n' )
		assert self.out_c.has_string_literal( ' (totals)' )
		assert self.out_c.has_string_literal( ' -- replaced with %s' )
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
		assert self.out_c.has_string_literal( ' OK' )
		assert self.out_c.has_string_literal( ' OK\\n' )
		assert self.out_c.has_string_literal( ' do you wish to overwrite (y or n)? ' )
		assert self.out_c.has_string_literal( ' file...          files to (de)compress. If none given, use standard input.' )
		assert self.out_c.has_string_literal( '%2ld.%1ld%%' )
		assert self.out_c.has_string_literal( '%5s %08lx %11s ' )
		assert self.out_c.has_string_literal( '%9ld %9ld ' )
		assert self.out_c.has_string_literal( '%s %s (%s)\\n' )
		assert self.out_c.has_string_literal( '%s: ' )
		assert self.out_c.has_string_literal( '%s: %s already exists;' )
		assert self.out_c.has_string_literal( '%s: %s already has %s suffix -- unchanged\\n' )
		assert self.out_c.has_string_literal( '%s: %s and %s are the same file\\n' )
		assert self.out_c.has_string_literal( '%s: %s compressed to %s\\n' )
		assert self.out_c.has_string_literal( '%s: %s has %d other link%c -- unchanged\\n' )
		assert self.out_c.has_string_literal( '%s: %s has flags 0x%x -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( '%s: %s has more than one entry -- unchanged\\n' )
		assert self.out_c.has_string_literal( '%s: %s has more than one entry--rest ignored\\n' )
		assert self.out_c.has_string_literal( '%s: %s is a a multi-part gzip file -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( '%s: %s is a directory -- ignored\\n' )
		assert self.out_c.has_string_literal( '%s: %s is encrypted -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( '%s: %s is not a directory or a regular file - ignored\\n' )
		assert self.out_c.has_string_literal( '%s: %s: cannot %scompress onto itself\\n' )
		assert self.out_c.has_string_literal( '%s: %s: extra field of %u bytes ignored\\n' )
		assert self.out_c.has_string_literal( '%s: %s: part number %u\\n' )
		assert self.out_c.has_string_literal( '%s: %s: unknown method %d -- get newer version of gzip\\n' )
		assert self.out_c.has_string_literal( '%s: %s: unknown suffix -- ignored\\n' )
		assert self.out_c.has_string_literal( '%s: %s: warning, name truncated\\n' )
		assert self.out_c.has_string_literal( '%s: %s: warning: %s%s\\n' )
		assert self.out_c.has_string_literal( '%s: -Z not supported in this version\\n' )
		assert self.out_c.has_string_literal( '%s: -r not supported on this system\\n' )
		assert self.out_c.has_string_literal( '%s: compressed data not %s a terminal. Use -f to force %scompression.\\n' )
		assert self.out_c.has_string_literal( '%s: time stamp restored\\n' )
		assert self.out_c.has_string_literal( '%s:\\t%s' )
		assert self.out_c.has_string_literal( '%s\\n' )
		assert self.out_c.has_string_literal( '.exe' )
		assert self.out_c.has_string_literal( '.tar' )
		assert self.out_c.has_string_literal( '.taz' )
		assert self.out_c.has_string_literal( '.tgz' )
		assert self.out_c.has_string_literal( '1.2.4' )
		assert self.out_c.has_string_literal( '18 Aug 93' )
		assert self.out_c.has_string_literal( 'Bad table\\n' )
		assert self.out_c.has_string_literal( 'Compilation options:\\n%s %s ' )
		assert self.out_c.has_string_literal( 'For help, type: %s -h\\n' )
		assert self.out_c.has_string_literal( 'HAVE_UNISTD_H ' )
		assert self.out_c.has_string_literal( 'NO_DIR' )
		assert self.out_c.has_string_literal( 'NO_MEMORY_H ' )
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
		assert self.out_c.has_string_literal( 'ab:cdfhH?lLmMnNqrS:tvVZ123456789' )
		assert self.out_c.has_string_literal( 'argc<=0' )
		assert self.out_c.has_string_literal( 'bad pack level' )
		assert self.out_c.has_string_literal( "can't recover suffix\\n" )
		assert self.out_c.has_string_literal( 'compressed  uncompr. ratio uncompressed_name' )
		assert self.out_c.has_string_literal( 'corrupt input.' )
		assert self.out_c.has_string_literal( 'corrupt input. Use zcat to recover some data.' )
		assert self.out_c.has_string_literal( 'corrupted input -- file name too large' )
		assert self.out_c.has_string_literal( 'fstat(stdin)' )
		assert self.out_c.has_string_literal( 'internal error, invalid method' )
		assert self.out_c.has_string_literal( 'invalid compressed data -- Huffman code > 32 bits' )
		assert self.out_c.has_string_literal( 'invalid compressed data--crc error' )
		assert self.out_c.has_string_literal( 'invalid compressed data--format violated' )
		assert self.out_c.has_string_literal( 'invalid compressed data--length error' )
		assert self.out_c.has_string_literal( 'invalid compressed data--length mismatch' )
		assert self.out_c.has_string_literal( 'len %ld, siz %ld\\n' )
		assert self.out_c.has_string_literal( 'method  crc     date  time  ' )
		assert self.out_c.has_string_literal( 'name too short' )
		assert self.out_c.has_string_literal( 'out of memory' )
		assert self.out_c.has_string_literal( 'output in compress .Z format not supported\\n' )
		assert self.out_c.has_string_literal( 'read from' )
		assert self.out_c.has_string_literal( 'stdout' )
		assert self.out_c.has_string_literal( 'too many leaves in Huffman tree' )
		assert self.out_c.has_string_literal( 'un' )
		assert self.out_c.has_string_literal( 'usage: %s [-%scdfhlLnN%stvV19] [-S suffix] [file ...]\\n' )
		assert self.out_c.has_string_literal( '%s: unexpected end of file\\n' )
		assert self.out_c.has_string_literal( 'internal error in shorten_name' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_804897c' )  #
		assert self.out_c.has_func( 'entry_point' )  #
		assert self.out_c.has_func( 'function_8048c70' )  #
		assert self.out_c.has_func( 'function_8048c80' )  #
		assert self.out_c.has_func( 'function_8048cb0' )  #
		assert self.out_c.has_func( 'function_8048cf0' )  #
		assert self.out_c.has_func( 'function_8048d50' )  #
		assert self.out_c.has_func( 'function_8048d80' )  #
		assert self.out_c.has_func( 'function_8048da1' )  #
		assert self.out_c.has_func( 'function_8048e00' )  #
		assert self.out_c.has_func( 'function_8048e2f' )  #
		assert self.out_c.has_func( 'function_8048e64' )  #
		assert self.out_c.has_func( 'function_8048f64' )  #
		assert self.out_c.has_func( 'function_8049019' )  #
		assert self.out_c.has_func( 'function_8049053' )  #
		assert self.out_c.has_func( 'function_80491c9' )  #
		assert self.out_c.has_func( 'function_8049a5e' )  #
		assert self.out_c.has_func( 'function_8049d3d' )  #
		assert self.out_c.has_func( 'function_804b368' )  #
		assert self.out_c.has_func( 'function_804b70c' )  #
		assert self.out_c.has_func( 'function_804b829' )  #
		assert self.out_c.has_func( 'function_804b950' )  #
		assert self.out_c.has_func( 'function_804bbf2' )  #
		assert self.out_c.has_func( 'function_804c110' )  #
		assert self.out_c.has_func( 'function_804c19d' )  #
		assert self.out_c.has_func( 'function_804c270' )  #
		assert self.out_c.has_func( 'function_804c350' )  #
		assert self.out_c.has_func( 'function_804c4f5' )  #
		assert self.out_c.has_func( 'function_804c660' )  #
		assert self.out_c.has_func( 'function_804c6cc' )  #
		assert self.out_c.has_func( 'function_804cae5' )  #
		assert self.out_c.has_func( 'function_804cd1c' )  #
		assert self.out_c.has_func( 'function_804cfbe' )  #
		assert self.out_c.has_func( 'function_804d110' )  #
		assert self.out_c.has_func( 'function_804d13d' )  #
		assert self.out_c.has_func( 'function_804d216' )  #
		assert self.out_c.has_func( 'function_804d23a' )  #
		assert self.out_c.has_func( 'function_804d2ff' )  #
		assert self.out_c.has_func( 'function_804d430' )  #
		assert self.out_c.has_func( 'function_804da20' )  #
		assert self.out_c.has_func( 'function_804da4a' )  #
		assert self.out_c.has_func( 'function_804e048' )  #
		assert self.out_c.has_func( 'function_804e43f' )  #
		assert self.out_c.has_func( 'function_804e604' )  #
		assert self.out_c.has_func( 'function_804e7aa' )  #
		assert self.out_c.has_func( 'function_804eeaa' )  #
		assert self.out_c.has_func( 'function_804efa8' )  #
		assert self.out_c.has_func( 'function_804f040' )  #
		assert self.out_c.has_func( 'function_804f081' )  #
		assert self.out_c.has_func( 'function_804f0b4' )  #
		assert self.out_c.has_func( 'basename' )  #
		assert self.out_c.has_func( 'function_804f111' )  #
		assert self.out_c.has_func( 'error' )  #
		assert self.out_c.has_func( 'warn' )  #
		assert self.out_c.has_func( 'function_804f1de' )  #
		assert self.out_c.has_func( 'function_804f23d' )  #
		assert self.out_c.has_func( 'function_804f2d5' )  #
		assert self.out_c.has_func( 'function_804f30b' )  #
		assert self.out_c.has_func( 'function_804f34c' )  #
		assert self.out_c.has_func( 'function_804f3a9' )  #
		assert self.out_c.has_func( 'function_804f3e8' )  #
		assert self.out_c.has_func( 'function_804f47c' )  #
		assert self.out_c.has_func( 'function_804f52f' )  #
		assert self.out_c.has_func( 'function_804f558' )  #
		assert self.out_c.has_func( 'function_8050180' )  #
		assert self.out_c.has_func( 'function_8050220' )  #
		assert self.out_c.has_func( 'function_8050240' )  #
		assert self.out_c.has_func( 'function_8050478' )  #
		assert self.out_c.has_func( 'function_8050a60' )  #

	# Functions reported in #1050 as not detected.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		assert self.out_c.has_func( 'function_804b6b3' )  # file_read
		assert self.out_c.has_func( 'function_804d592' )  # unzip
		assert self.out_c.has_func( 'function_804f734' )  # lzw
		assert self.out_c.has_func( 'function_804f7a0' )  # unlzw
		assert self.out_c.has_func( 'function_804fd94' )  # unpack
		assert self.out_c.has_func( 'function_80505eb' )  # unlzh
