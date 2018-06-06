from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='bzip2-strip',
		# Disable CopyPropagation because it runs too long. Since we are
		# testing only string literals and functions, this should have not any
		# visible effect on the test outputs.
		args='-k --backend-disabled-opts CopyPropagation'  # TODO: matula, not sure if some functions are not called, or we just do not detect it.
	)

	def test_check_for_all_currently_detected_strings(self):
		#assert self.out_c.has_string_literal( '%s: WARNING: deletion of output file suppressed\\n' )
		assert self.out_c.has_string_literal( ' {0x%08x, 0x%08x}' )
		assert self.out_c.has_string_literal( '--stdout' )
		assert self.out_c.has_string_literal( '  %s: ' )
		assert self.out_c.has_string_literal( '%s: Input file %s has %d other link%s.\\n' )
		assert self.out_c.has_string_literal( 'testf: bad modes\\n' )
		assert self.out_c.has_string_literal( "%s: Can't open input file %s:%s.\\n" )
		assert self.out_c.has_string_literal( "\\n%s: Caught a SIGSEGV or SIGBUS whilst decompressing.\\n\\n   Possible causes are (most likely first):\\n   (1) The compressed data is corrupted, and bzip2's usual checks\\n       failed to detect this.  Try bzip2 -tvv my_file.bz2.\\n   (2) This computer has unreliable memory or cache hardware\\n       (a surprisingly common problem; try a different machine.)\\n   (3) A bug in the compiler used to create this executable\\n       (unlikely, if you didn't compile bzip2 yourself.)\\n   (4) A real bug in bzip2 -- I hope this should never be the case.\\n   The user's manual, Section 4.3, has more info on (2) and (3).\\n   \\n   If you suspect this is a bug in bzip2, or are unsure about (2)\\n   or (3), feel free to report it to me at: jseward@bzip.org.\\n   Section 4.3 of the user's manual describes the info a useful\\n   bug report should have.  If the manual is available on your\\n   system, please try and read it before mailing me.  If you don't\\n   have the manual or can't be bothered to read it, mail me anyway.\\n\\n" )
		assert self.out_c.has_string_literal( 'selectors %d, ' )
		assert self.out_c.has_string_literal( "%s: Bad flag `%s'\\n" )
		assert self.out_c.has_string_literal( '--repetitive-best' )
		assert self.out_c.has_string_literal( 'UNZIP' )
		#assert self.out_c.has_string_literal( "%s:    `%s' may be incomplete.\\n" )
		assert self.out_c.has_string_literal( "\\nYou can use the `bzip2recover' program to attempt to recover\\ndata from undamaged sections of corrupted files.\\n\\n" )
		assert self.out_c.has_string_literal( '        main sort initialise ...\\n' )
		assert self.out_c.has_string_literal( 'file ends unexpectedly\\n' )
		assert self.out_c.has_string_literal( '%s: WARNING: some files have not been processed:\\n%s:    %d specified on command line, %d not processed yet.\\n\\n' )
		assert self.out_c.has_string_literal( 'ok\\n' )
		assert self.out_c.has_string_literal( '%s: %s is not a bzip2 file.\\n' )
		assert self.out_c.has_string_literal( '--fast' )
		assert self.out_c.has_string_literal( '\\n%s: I/O or other error, bailing out.  Possible reason follows.\\n' )
		assert self.out_c.has_string_literal( 'codes %d\\n' )
		assert self.out_c.has_string_literal( '%s: Input file %s is a directory.\\n' )
		assert self.out_c.has_string_literal( "%s: For help, type: `%s --help'.\\n" )
		#assert self.out_c.has_string_literal( '%s:    since input file no longer exists.  Output file\\n' )
		assert self.out_c.has_string_literal( '--force' )
		assert self.out_c.has_string_literal( '\\n%s: %s: trailing garbage after EOF ignored\\n' )
		assert self.out_c.has_string_literal( '      %d in block, %d after MTF & 1-2 coding, %d+2 syms in use\\n' )
		assert self.out_c.has_string_literal( 'rt+rld' )
		assert self.out_c.has_string_literal( '(stdout)' )
		assert self.out_c.has_string_literal( '        reconstructing block ...\\n' )
		assert self.out_c.has_string_literal( 'compress: bad modes\\n' )
		assert self.out_c.has_string_literal( '\\n%s: Control-C or similar caught, quitting.\\n' )
		assert self.out_c.has_string_literal( '--' )
		assert self.out_c.has_string_literal( "\\n%s: couldn't allocate enough memory\\n" )
		assert self.out_c.has_string_literal( '\\n    [%d: huff+mtf ' )
		assert self.out_c.has_string_literal( '--exponential' )
		assert self.out_c.has_string_literal( 'zcat' )
		assert self.out_c.has_string_literal( 'uncompress: bad srcMode' )
		assert self.out_c.has_string_literal( '%s: Input file %s is not a normal file.\\n' )
		assert self.out_c.has_string_literal( '%6.3f:1, %6.3f bits/byte, %5.2f%% saved, %s in, %s out.\\n' )
		assert self.out_c.has_string_literal( '--keep' )
		assert self.out_c.has_string_literal( 'decompress:bzReadGetUnused' )
		assert self.out_c.has_string_literal( '%s: Output file %s already exists.\\n' )
		assert self.out_c.has_string_literal( '      initial group %d, [%d .. %d], has %d syms (%4.1f%%)\\n' )
		assert self.out_c.has_string_literal( '--help' )
		assert self.out_c.has_string_literal( '        bucket sorting ...\\n' )
		assert self.out_c.has_string_literal( '(stdin)' )
		assert self.out_c.has_string_literal( '      bytes: mapping %d, ' )
		#assert self.out_c.has_string_literal( '%s:    I suggest doing an integrity test (bzip2 -tv) of it.\\n' )
		assert self.out_c.has_string_literal( "%s: Can't open input file %s: %s.\\n" )
		assert self.out_c.has_string_literal( ' no data compressed.\\n' )
		assert self.out_c.has_string_literal( 'done\\n' )
		assert self.out_c.has_string_literal( "bzip2, a block-sorting file compressor.  Version %s.\\n\\n   usage: %s [flags and input files in any order]\\n\\n   -h --help           print this message\\n   -d --decompress     force decompression\\n   -z --compress       force compression\\n   -k --keep           keep (don't delete) input files\\n   -f --force          overwrite existing output files\\n   -t --test           test compressed file integrity\\n   -c --stdout         output to standard out\\n   -q --quiet          suppress noncritical error messages\\n   -v --verbose        be verbose (a 2nd -v gives more)\\n   -L --license        display software version & license\\n   -V --version        display software version & license\\n   -s --small          use less memory (at most 2500k)\\n   -1 .. -9            set block size to 100k .. 900k\\n   --fast              alias for -1\\n   --best              alias for -9\\n\\n   If invoked as `bzip2', default action is to compress.\\n              as `bunzip2',  default action is to decompress.\\n              as `bzcat', default action is to decompress to stdout.\\n\\n   If no file names are given, bzip2 compresses or decompresses\\n   from standard input to standard output.  You can combine\\n   short flags, so `-v -4' means the same as -v4 or -4v, &c.\\n\\n" )
		#assert self.out_c.has_string_literal( '        depth %6d has ' )
		assert self.out_c.has_string_literal( '(none)' )
		assert self.out_c.has_string_literal( 'BZIP2' )
		assert self.out_c.has_string_literal( '%s: %s: ' )
		assert self.out_c.has_string_literal( '    final combined CRC = 0x%08x\\n   ' )
		assert self.out_c.has_string_literal( '--repetitive-fast' )
		assert self.out_c.has_string_literal( '\\tInput file = %s, output file = %s\\n' )
		assert self.out_c.has_string_literal( '        %d pointers, %d sorted, %d scanned\\n' )
		assert self.out_c.has_string_literal( "bzip2: I'm not configured correctly for this platform!\\n\\tI require Int32, Int16 and Char to have sizes\\n\\tof 4, 2 and 1 bytes to run properly, and they don't.\\n\\tProbably you can fix this by defining them correctly,\\n\\tand recompiling.  Bye!\\n" )
		assert self.out_c.has_string_literal( "%s: Can't create output file %s: %s.\\n" )
		assert self.out_c.has_string_literal( '      %d work, %d block, ratio %5.2f\\n' )
		assert self.out_c.has_string_literal( "%s: I won't write compressed data to a terminal.\\n" )
		assert self.out_c.has_string_literal( '1.0.6, 6-Sept-2010' )
		assert self.out_c.has_string_literal( 'bzip2, a block-sorting file compressor.  Version %s.\\n   \\n   Copyright (C) 1996-2010 by Julian Seward.\\n   \\n   This program is free software; you can redistribute it and/or modify\\n   it under the terms set out in the LICENSE file, which is included\\n   in the bzip2-1.0.6 source distribution.\\n   \\n   This program is distributed in the hope that it will be useful,\\n   but WITHOUT ANY WARRANTY; without even the implied warranty of\\n   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\\n   LICENSE file for more details.\\n   \\n' )
		assert self.out_c.has_string_literal( '--best' )
		assert self.out_c.has_string_literal( '    block %d: crc = 0x%08x, combined CRC = 0x%08x, size = %d\\n' )
		assert self.out_c.has_string_literal( '\\n%s: Compressed file ends unexpectedly;\\n\\tperhaps it is corrupted?  *Possible* reason follows.\\n' )
		assert self.out_c.has_string_literal( 'ZCAT' )
		assert self.out_c.has_string_literal( '\\n    combined CRCs: stored = 0x%08x, computed = 0x%08x' )
		assert self.out_c.has_string_literal( "%s: I won't read compressed data from a terminal.\\n" )
		#assert self.out_c.has_string_literal( 'r' )
		assert self.out_c.has_string_literal( 'test:bzReadGetUnused' )
		assert self.out_c.has_string_literal( '\\n\\nbzip2/libbzip2: internal error number %d.\\nThis is a bug in bzip2/libbzip2, %s.\\nPlease report it to me at: jseward@bzip.org.  If this happened\\nwhen you were using some program which uses libbzip2 as a\\ncomponent, you should also report this bug to the author(s)\\nof that program.  Please make an effort to report this bug;\\ntimely and accurate bug reports eventually lead to higher\\nquality software.  Thanks.  Julian Seward, 10 December 2007.\\n\\n' )
		assert self.out_c.has_string_literal( '%s: Input file %s already has %s suffix.\\n' )
		#assert self.out_c.has_string_literal( '        qsort [0x%x, 0x%x]   done %d   this %d\\n' )
		assert self.out_c.has_string_literal( '%s: -c and -t cannot be used together.\\n' )
		assert self.out_c.has_string_literal( "bzip2: file name\\n`%s'\\nis suspiciously (more than %d chars) long.\\nTry using a reasonable file name instead.  Sorry! :-)\\n" )
		assert self.out_c.has_string_literal( '\\n%s: PANIC -- internal consistency error:\\n\\t%s\\n\\tThis is a BUG.  Please report it to me at:\\n\\tjseward@bzip.org\\n' )
		assert self.out_c.has_string_literal( 'bad magic number (file not created by bzip2)\\n' )
		assert self.out_c.has_string_literal( '    too repetitive; using fallback sorting algorithm\\n' )
		assert self.out_c.has_string_literal( 'rb' )
		assert self.out_c.has_string_literal( 'z2cat' )
		#assert self.out_c.has_string_literal( '%6d unresolved strings\\n' )
		assert self.out_c.has_string_literal( 'compress: bad srcMode' )
		assert self.out_c.has_string_literal( "\\n*** A special note about internal error number 1007 ***\\n\\nExperience suggests that a common cause of i.e. 1007\\nis unreliable memory or other hardware.  The 1007 assertion\\njust happens to cross-check the results of huge numbers of\\nmemory reads/writes, and so acts (unintendedly) as a stress\\ntest of your memory system.\\n\\nI suggest the following: try compressing the file again,\\npossibly monitoring progress in detail with the -vv flag.\\n\\n* If the error cannot be reproduced, and/or happens at different\\n  points in compression, you may have a flaky memory system.\\n  Try a memory-test program.  I have used Memtest86\\n  (www.memtest86.com).  At the time of writing it is free (GPLd).\\n  Memtest86 tests memory much more thorougly than your BIOSs\\n  power-on test, and may find failures that the BIOS doesn't.\\n\\n* If the error can be repeatably reproduced, this is a bug in\\n  bzip2, and I would very much like to hear about it.  Please\\n  let me know, and, ideally, save a copy of the file causing the\\n  problem -- without which I will be unable to investigate it.\\n\\n" )
		assert self.out_c.has_string_literal( 'w' )
		assert self.out_c.has_string_literal( 'uncompress: bad modes\\n' )
		assert self.out_c.has_string_literal( 'BZIP' )
		assert self.out_c.has_string_literal( '--verbose' )
		assert self.out_c.has_string_literal( '%s: %s is redundant in versions 0.9.5 and above\\n' )
		assert self.out_c.has_string_literal( '--compress' )
		assert self.out_c.has_string_literal( '\\n%s: Data integrity error when decompressing.\\n' )
		assert self.out_c.has_string_literal( 'Z2CAT' )
		assert self.out_c.has_string_literal( 'trailing garbage after EOF ignored\\n' )
		assert self.out_c.has_string_literal( '--test' )
		assert self.out_c.has_string_literal( "\\n%s: Caught a SIGSEGV or SIGBUS whilst compressing.\\n\\n   Possible causes are (most likely first):\\n   (1) This computer has unreliable memory or cache hardware\\n       (a surprisingly common problem; try a different machine.)\\n   (2) A bug in the compiler used to create this executable\\n       (unlikely, if you didn't compile bzip2 yourself.)\\n   (3) A real bug in bzip2 -- I hope this should never be the case.\\n   The user's manual, Section 4.3, has more info on (1) and (2).\\n   \\n   If you suspect this is a bug in bzip2, or are unsure about (1)\\n   or (2), feel free to report it to me at: jseward@bzip.org.\\n   Section 4.3 of the user's manual describes the info a useful\\n   bug report should have.  If the manual is available on your\\n   system, please try and read it before mailing me.  If you don't\\n   have the manual or can't be bothered to read it, mail me anyway.\\n\\n" )
		assert self.out_c.has_string_literal( "%s: Can't open input %s: %s.\\n" )
		#assert self.out_c.has_string_literal( 's' )
		assert self.out_c.has_string_literal( "\\nIt is possible that the compressed file(s) have become corrupted.\\nYou can use the -tvv option to test integrity of such files.\\n\\nYou can use the `bzip2recover' program to attempt to recover\\ndata from undamaged sections of corrupted files.\\n\\n" )
		assert self.out_c.has_string_literal( '--decompress' )
		assert self.out_c.has_string_literal( 'unzip' )
		assert self.out_c.has_string_literal( "%s: Can't guess original name for %s -- using %s\\n" )
		assert self.out_c.has_string_literal( 'data integrity (CRC) error in data\\n' )

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_8900018' )  #
		assert self.out_c.has_func( 'entry_point' )  # function_890003c
		assert self.out_c.has_func( 'function_8900180' )  #
		assert self.out_c.has_func( 'function_8900228' )  #
		assert self.out_c.has_func( 'function_89002e4' )  #
		assert self.out_c.has_func( 'function_89002f8' )  #
		assert self.out_c.has_func( 'function_8900354' )  # call_frame_dummy
		assert self.out_c.has_func( 'function_8902878' )  #
		assert self.out_c.has_func( 'function_89028b4' )  #
		assert self.out_c.has_func( 'function_89029a4' )  #
		assert self.out_c.has_func( 'function_8902a84' )  #
		assert self.out_c.has_func( 'function_8902aa4' )  #
		assert self.out_c.has_func( 'function_8902ac0' )  #
		assert self.out_c.has_func( 'function_8902ae4' )  #
		assert self.out_c.has_func( 'function_8902aec' )  #
		assert self.out_c.has_func( 'function_8902b54' )  #
		assert self.out_c.has_func( 'function_8902b9c' )  #
		assert self.out_c.has_func( 'function_8902bd0' )  #
		assert self.out_c.has_func( 'function_8902c08' )  #
		assert self.out_c.has_func( 'function_8902c48' )  #
		assert self.out_c.has_func( 'function_8902cc8' )  #
		assert self.out_c.has_func( 'function_8902e74' )  #
		assert self.out_c.has_func( 'function_8902ea8' )  #
		assert self.out_c.has_func( 'function_8902ed0' )  #
		assert self.out_c.has_func( 'function_8902f70' )  #
		assert self.out_c.has_func( 'function_89030c4' )  #
		#assert self.out_c.has_func( 'function_89030fc' )  # mySignalCatcher, missing in #1050
		#assert self.out_c.has_func( 'function_8903128' )  # mySIGSEGVorSIGBUScatcher, missing in #1050
		assert self.out_c.has_func( 'function_89031b0' )  #
		assert self.out_c.has_func( 'function_89031ec' )  #
		assert self.out_c.has_func( 'function_8903238' )  #
		assert self.out_c.has_func( 'function_8903274' )  #
		assert self.out_c.has_func( 'function_89032dc' )  #
		assert self.out_c.has_func( 'function_8903358' )  #
		assert self.out_c.has_func( 'function_8903398' )  #
		assert self.out_c.has_func( 'function_89033d8' )  #
		assert self.out_c.has_func( 'function_8903404' )  #
		assert self.out_c.has_func( 'function_89037b8' )  #
		assert self.out_c.has_func( 'function_8903efc' )  #
		assert self.out_c.has_func( 'function_890422c' )  #
		assert self.out_c.has_func( 'function_89045b0' )  #
		assert self.out_c.has_func( 'function_8904a08' )  #
		assert self.out_c.has_func( 'main' )  #
		assert self.out_c.has_func( 'function_8905e3c' )  #
		assert self.out_c.has_func( 'function_8905e44' )  #
		assert self.out_c.has_func( 'function_8905e80' )  #
		assert self.out_c.has_func( 'function_8905e90' )  #
		assert self.out_c.has_func( 'function_8905eb0' )  #
		assert self.out_c.has_func( 'function_89060e0' )  #
		assert self.out_c.has_func( 'function_8906298' )  #
		assert self.out_c.has_func( 'function_8906340' )  #
		assert self.out_c.has_func( 'function_8906440' )  #
		assert self.out_c.has_func( 'function_8906480' )  #
		assert self.out_c.has_func( 'function_8906528' )  #
		assert self.out_c.has_func( 'function_89065b0' )  #
		assert self.out_c.has_func( 'function_89065f4' )  #
		assert self.out_c.has_func( 'function_8906634' )  #
		assert self.out_c.has_func( 'function_89066e0' )  #
		assert self.out_c.has_func( 'function_8906894' )  #
		assert self.out_c.has_func( 'function_8906a00' )  #
		assert self.out_c.has_func( 'function_8906cb0' )  #
		assert self.out_c.has_func( 'function_89080e0' )  #
		assert self.out_c.has_func( 'function_8908360' )  #
		assert self.out_c.has_func( 'function_8908834' )  #
		assert self.out_c.has_func( 'function_8908b2c' )  #
		assert self.out_c.has_func( 'function_8908d98' )  #
		assert self.out_c.has_func( 'function_8908e68' )  #
		assert self.out_c.has_func( 'function_8909054' )  #
		assert self.out_c.has_func( 'function_89090b0' )  #
		assert self.out_c.has_func( 'function_89090bc' )  #
		assert self.out_c.has_func( 'function_8909138' )  #
		assert self.out_c.has_func( 'function_89091b0' )  #
		assert self.out_c.has_func( 'function_890937c' )  #
		assert self.out_c.has_func( 'function_890dfe0' )  #
		assert self.out_c.has_func( 'function_8911274' )  #
		assert self.out_c.has_func( 'function_8911dbc' )  #
		assert self.out_c.has_func( 'function_8913d84' )  #
		assert self.out_c.has_func( 'function_8913f9c' )  #
		assert self.out_c.has_func( 'function_8914000' )  #
		assert self.out_c.has_func( 'function_89141b4' )  #
		assert self.out_c.has_func( 'function_891f470' )  #
		assert self.out_c.has_func( 'function_891f4c0' )  #
		assert self.out_c.has_func( 'function_891f4d4' )  #
		assert self.out_c.has_func( 'function_891f548' )  #
		assert self.out_c.has_func( 'function_891f550' )  #
		assert self.out_c.has_func( 'sceIoDopen' )  # @ 891f4f0

	def test_check_for_some_static_functions(self):
		assert self.out_config.is_statically_linked('atexit', 0x8900368)
		assert self.out_config.is_statically_linked('__errno', 0x8900cb8)
		assert self.out_config.is_statically_linked('stat', 0x89181d4)

	# Functions reported in #1050 as not detected.
	#
	def test_check_for_functions_not_detected_before_1050_fix(self):
		#assert self.out_c.has_func( 'function_89065bc' )  # BZ2_bzflush, no idea if this should be a function
		assert self.out_c.has_func( 'function_89065c4' )  # BZ2_bzerror
		assert self.out_c.has_func( 'function_89066bc' )  # default_bzfree
		assert self.out_c.has_func( 'function_8906c90' )  # default_bzalloc
		assert self.out_c.has_func( 'function_89089e4' )  # BZ2_bzBuffToBuffCompress
		assert self.out_c.has_func( 'function_8907fac' )  # BZ2_bzBuffToBuffDecompress
		assert self.out_c.has_func( 'function_8906c6c' )  # BZ2_bzopen
		assert self.out_c.has_func( 'function_8906c40' )  # BZ2_bzdopen
		assert self.out_c.has_func( 'function_8908300' )  # BZ2_bzread
		assert self.out_c.has_func( 'function_890900c' )  # BZ2_bzwrite
		assert self.out_c.has_func( 'function_8908dbc' )  # BZ2_bzclose
