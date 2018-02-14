
from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='x86-elf-gcc4.6.3-O0-g--cat',
		args='-k'
	)

	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( '' )
		assert self.out_c.has_string_literal( '      --help     display this help and exit\\n' )
		assert self.out_c.has_string_literal( '      --version  output version information and exit\\n' )
		assert self.out_c.has_string_literal( '  -t                       equivalent to -vT\\n  -T, --show-tabs          display TAB characters as ^I\\n  -u                       (ignored)\\n  -v, --show-nonprinting   use ^ and M- notation, except for LFD and TAB\\n' )
		assert self.out_c.has_string_literal( '%50s %50s' )
		assert self.out_c.has_string_literal( '%s' )
		assert self.out_c.has_string_literal( '%s %s\\n' )
		assert self.out_c.has_string_literal( '%s (%s)' )
		assert self.out_c.has_string_literal( '%s (%s) %s\\n' )
		assert self.out_c.has_string_literal( '%s home page: <%s>\\n' )
		assert self.out_c.has_string_literal( '%s home page: <http://www.gnu.org/software/%s/>\\n' )
		assert self.out_c.has_string_literal( '%s: %s' )
		assert self.out_c.has_string_literal( '(C)' )
		assert self.out_c.has_string_literal( "*iter->cur.ptr == '\\\\0'" )
		assert self.out_c.has_string_literal( '/.libs/' )
		#assert self.out_c.has_string_literal( '/usr/local/lib' )
		assert self.out_c.has_string_literal( '/usr/local/share/locale' )
		assert self.out_c.has_string_literal( 'A NULL argv[0] was passed through an exec system call.\\n' )
		assert self.out_c.has_string_literal( 'ASCII' )
		assert self.out_c.has_string_literal( 'CHARSETALIASDIR' )
		assert self.out_c.has_string_literal( 'Concatenate FILE(s), or standard input, to standard output.\\n\\n  -A, --show-all           equivalent to -vET\\n  -b, --number-nonblank    number nonempty output lines, overrides -n\\n  -e                       equivalent to -vE\\n  -E, --show-ends          display $ at end of each line\\n  -n, --number             number all output lines\\n  -s, --squeeze-blank      suppress repeated empty output lines\\n' )
		assert self.out_c.has_string_literal( 'Copyright %s %d Free Software Foundation, Inc.' )
		assert self.out_c.has_string_literal( "For complete documentation, run: info coreutils '%s invocation'\\n" )
		assert self.out_c.has_string_literal( 'GNU coreutils' )
		assert self.out_c.has_string_literal( 'General help using GNU software: <http://www.gnu.org/gethelp/>\\n' )
		assert self.out_c.has_string_literal( 'Report %s translation bugs to <http://translationproject.org/team/>\\n' )
		assert self.out_c.has_string_literal( 'Torbjorn Granlund' )
		assert self.out_c.has_string_literal( "Try `%s --help' for more information.\\n" )
		assert self.out_c.has_string_literal( 'UTF-8' )
		assert self.out_c.has_string_literal( 'Usage: %s [OPTION]... [FILE]...\\n' )
		assert self.out_c.has_string_literal( 'Written by %s and %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, %s,\\n%s, %s, %s, %s,\\n%s, %s, and others.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, %s,\\n%s, %s, %s, %s,\\n%s, and %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, %s,\\n%s, %s, %s, %s,\\nand %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, %s,\\n%s, %s, %s, and %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, %s,\\n%s, %s, and %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, %s,\\n%s, and %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, %s,\\nand %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s, %s, and %s.\\n' )
		assert self.out_c.has_string_literal( 'Written by %s.\\n' )
		assert self.out_c.has_string_literal( "\\nExamples:\\n  %s f - g  Output f's contents, then standard input, then g's contents.\\n  %s        Copy standard input to standard output.\\n" )
		assert self.out_c.has_string_literal( '\\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.\\nThis is free software: you are free to change and redistribute it.\\nThere is NO WARRANTY, to the extent permitted by law.\\n\\n' )
		assert self.out_c.has_string_literal( '\\nReport %s bugs to %s\\n' )
		assert self.out_c.has_string_literal( '\\nReport bugs to: %s\\n' )
		assert self.out_c.has_string_literal( '\\nWith no FILE, or when FILE is -, read standard input.\\n' )
		assert self.out_c.has_string_literal( 'benstuvAET' )
		assert self.out_c.has_string_literal( 'cannot do ioctl on %s' )
		assert self.out_c.has_string_literal( 'cat' )
		assert self.out_c.has_string_literal( 'closing standard input' )
		assert self.out_c.has_string_literal( 'coreutils' )
		assert self.out_c.has_string_literal( 'en_' )
		assert self.out_c.has_string_literal( 'iter->cur.wc == 0' )
		assert self.out_c.has_string_literal( 'lt-' )
		assert self.out_c.has_string_literal( 'mbiter.h' )
		assert self.out_c.has_string_literal( 'mbiter_multi_next' )
		assert self.out_c.has_string_literal( 'mbsinit (&iter->state)' )
		assert self.out_c.has_string_literal( 'mbuiter.h' )
		assert self.out_c.has_string_literal( 'mbuiter_multi_next' )
		assert self.out_c.has_string_literal( 'memory exhausted' )
		assert self.out_c.has_string_literal( 'standard output' )
		assert self.out_c.has_string_literal( 'write error' )

	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( '_init' )  #
		assert self.out_c.has_func( '_start' )  #
		assert self.out_c.has_func( '__do_global_dtors_aux' )  #
		assert self.out_c.has_func( 'frame_dummy' )  #
		assert self.out_c.has_func( 'ptr_align' )  #
		assert self.out_c.has_func( 'emit_ancillary_info' )  #
		assert self.out_c.has_func( 'io_blksize' )  #
		assert self.out_c.has_func( 'usage' )  #
		assert self.out_c.has_func( 'next_line_num' )  #
		assert self.out_c.has_func( 'simple_cat' )  #
		assert self.out_c.has_func( 'write_pending' )  #
		assert self.out_c.has_func( 'cat' )  #
		assert self.out_c.has_func( 'main' )  #
		assert self.out_c.has_func( 'ignore_value' )  #
		assert self.out_c.has_func( 'fdadvise' )  #
		assert self.out_c.has_func( 'fadvise' )  #
		assert self.out_c.has_func( 'full_write' )  #
		assert self.out_c.has_func( 'set_program_name' )  #
		assert self.out_c.has_func( 'is_basic' )  #
		assert self.out_c.has_func( 'mbuiter_multi_next' )  #
		assert self.out_c.has_func( 'mbsstr_trimmed_wordbounded' )  #
		assert self.out_c.has_func( 'proper_name' )  #
		assert self.out_c.has_func( 'proper_name_utf8' )  #
		assert self.out_c.has_func( 'strnlen1' )  #
		assert self.out_c.has_func( 'is_basic2' )  #
		assert self.out_c.has_func( 'mbiter_multi_next' )  #
		assert self.out_c.has_func( 'trim2' )  #
		assert self.out_c.has_func( 'version_etc_arn' )  #
		assert self.out_c.has_func( 'version_etc_ar' )  #
		assert self.out_c.has_func( 'version_etc_va' )  #
		assert self.out_c.has_func( 'version_etc' )  #
		assert self.out_c.has_func( 'emit_bug_reporting_address' )  #
		assert self.out_c.has_func( 'xalloc_die' )  #
		assert self.out_c.has_func( 'xmem_cd_iconv' )  #
		assert self.out_c.has_func( 'xstr_cd_iconv' )  #
		assert self.out_c.has_func( 'xstr_iconv' )  #
		assert self.out_c.has_func( 'last_component' )  #
		assert self.out_c.has_func( 'base_len' )  #
		assert self.out_c.has_func( 'close_stdout_set_file_name' )  #
		assert self.out_c.has_func( 'close_stdout_set_ignore_EPIPE' )  #
		assert self.out_c.has_func( 'close_stdout' )  #
		assert self.out_c.has_func( 'quote_n' )  #
		assert self.out_c.has_func( 'quote' )  #
		assert self.out_c.has_func( 'xcharalloc' )  #
		assert self.out_c.has_func( 'clone_quoting_options' )  #
		assert self.out_c.has_func( 'get_quoting_style' )  #
		assert self.out_c.has_func( 'set_quoting_style' )  #
		assert self.out_c.has_func( 'set_char_quoting' )  #
		assert self.out_c.has_func( 'set_quoting_flags' )  #
		assert self.out_c.has_func( 'set_custom_quoting' )  #
		assert self.out_c.has_func( 'quoting_options_from_style' )  #
		assert self.out_c.has_func( 'gettext_quote' )  #
		assert self.out_c.has_func( 'quotearg_buffer_restyled' )  #
		assert self.out_c.has_func( 'quotearg_buffer' )  #
		assert self.out_c.has_func( 'quotearg_alloc' )  #
		assert self.out_c.has_func( 'quotearg_alloc_mem' )  #
		assert self.out_c.has_func( 'quotearg_free' )  #
		assert self.out_c.has_func( 'quotearg_n_options' )  #
		assert self.out_c.has_func( 'quotearg_n' )  #
		assert self.out_c.has_func( 'quotearg_n_mem' )  #
		assert self.out_c.has_func( 'quotearg' )  #
		assert self.out_c.has_func( 'quotearg_mem' )  #
		assert self.out_c.has_func( 'quotearg_n_style' )  #
		assert self.out_c.has_func( 'quotearg_n_style_mem' )  #
		assert self.out_c.has_func( 'quotearg_style' )  #
		assert self.out_c.has_func( 'quotearg_style_mem' )  #
		assert self.out_c.has_func( 'quotearg_char_mem' )  #
		assert self.out_c.has_func( 'quotearg_char' )  #
		assert self.out_c.has_func( 'quotearg_colon' )  #
		assert self.out_c.has_func( 'quotearg_colon_mem' )  #
		assert self.out_c.has_func( 'quotearg_n_custom' )  #
		assert self.out_c.has_func( 'quotearg_n_custom_mem' )  #
		assert self.out_c.has_func( 'quotearg_custom' )  #
		assert self.out_c.has_func( 'quotearg_custom_mem' )  #
		assert self.out_c.has_func( 'safe_read' )  #
		assert self.out_c.has_func( 'safe_write' )  #
		assert self.out_c.has_func( 'x2nrealloc' )  #
		assert self.out_c.has_func( 'xmalloc' )  #
		assert self.out_c.has_func( 'xrealloc' )  #
		assert self.out_c.has_func( 'x2realloc' )  #
		assert self.out_c.has_func( 'xzalloc' )  #
		assert self.out_c.has_func( 'xcalloc' )  #
		assert self.out_c.has_func( 'xmemdup' )  #
		assert self.out_c.has_func( 'xstrdup' )  #
		assert self.out_c.has_func( 'c_strcasecmp' )  #
		assert self.out_c.has_func( 'get_charset_aliases' )  #
		assert self.out_c.has_func( 'locale_charset' )  #
		assert self.out_c.has_func( 'mb_copy' )  #
		assert self.out_c.has_func( 'is_basic3' )  #
		assert self.out_c.has_func( 'is_basic4' )  #
		assert self.out_c.has_func( 'mbuiter_multi_next2' )  #
		assert self.out_c.has_func( 'mbuiter_multi_next3' )  #
		assert self.out_c.has_func( 'knuth_morris_pratt_unibyte' )  #
		assert self.out_c.has_func( 'knuth_morris_pratt_multibyte' )  #
		assert self.out_c.has_func( 'mbsstr' )  #
		assert self.out_c.has_func( 'mem_cd_iconv' )  #
		assert self.out_c.has_func( 'str_cd_iconv' )  #
		assert self.out_c.has_func( 'str_iconv' )  #
		assert self.out_c.has_func( 'close_stream' )  #
		assert self.out_c.has_func( 'c_isascii' )  #
		assert self.out_c.has_func( 'c_isalnum' )  #
		assert self.out_c.has_func( 'c_isalpha' )  #
		assert self.out_c.has_func( 'c_isblank' )  #
		assert self.out_c.has_func( 'c_iscntrl' )  #
		assert self.out_c.has_func( 'c_isdigit' )  #
		assert self.out_c.has_func( 'c_islower' )  #
		assert self.out_c.has_func( 'c_isgraph' )  #
		assert self.out_c.has_func( 'c_isprint' )  #
		assert self.out_c.has_func( 'c_ispunct' )  #
		assert self.out_c.has_func( 'c_isspace' )  #
		assert self.out_c.has_func( 'c_isupper' )  #
		assert self.out_c.has_func( 'c_isxdigit' )  #
		assert self.out_c.has_func( 'c_tolower' )  #
		assert self.out_c.has_func( 'c_toupper' )  #
		assert self.out_c.has_func( 'mmalloca' )  #
		assert self.out_c.has_func( 'freea' )  #
		assert self.out_c.has_func( 'mbslen' )  #
		assert self.out_c.has_func( '__libc_csu_init' )  #
		assert self.out_c.has_func( '__libc_csu_fini' )  #
		assert self.out_c.has_func( '__i686_get_pc_thunk_bx' )  #
		assert self.out_c.has_func( '__do_global_ctors_aux' )  #
		assert self.out_c.has_func( '_fini' )  #

	def test_problem_reported_in_1177_xmalloc(self):
		xmalloc = self.out_c.funcs['xmalloc']
		assert xmalloc.calls('malloc', 'xalloc_die')

		assert xmalloc.has_just_params('n')
		assert xmalloc.params['n'].type.is_int(32)

		assert xmalloc.return_type.is_pointer()
		assert xmalloc.return_type.pointed_type.is_char()

		assert xmalloc.has_var_def_stmts('int * mem = malloc(n)')
		assert xmalloc.has_return_stmts('return (char *)mem')

	def test_the_same_problem_from_xmalloc_in_xrealloc(self):
		xrealloc = self.out_c.funcs['xrealloc']
		assert xrealloc.calls('realloc', 'xalloc_die')

		assert xrealloc.has_just_params('p', 'n')
		assert xrealloc.params['p'].type.is_pointer()
		assert xrealloc.params['p'].type.pointed_type.is_char()
		assert xrealloc.params['n'].type.is_int(32)

		assert xrealloc.return_type.is_pointer()
		assert xrealloc.return_type.pointed_type.is_char()

		assert xrealloc.has_var_def_stmts('int * mem = realloc((int *) p, n)')
		assert xrealloc.has_return_stmts('return (char *)mem')
