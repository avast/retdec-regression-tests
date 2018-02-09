
from regression_tests import *

class TestMips(Test):
	settings = TestSettings(
		input='mips-elf-e8e3b30ff295c1eac0cc06e1c8b1dc5e',
		args='-k'
	)

	def test_check_for_currently_detected_strings(self):
		assert self.out_c.has_string_literal( 'MLPOIKUJNBHYTGVCFZEDXSRQAWOIUATMQEXKYDSLRFZGNJVCPBWHTRQVCKGUJFSAWMZNXLPOIHBEDYGQMKNHOIUATVEJBWXCDZPSLRFYLRZXJBUFSYGQNPCDITMVAHEOKWYMPNWXKSDTLBQEGHCJVRFZOIUA' )
		assert self.out_c.has_string_literal( 'loginSIGTERM signo:%d\\n' )
		assert self.out_c.has_string_literal( 'initMsgque: login command thread starts up,pid:%d,tid:%d,qname:%s\\n' )
		assert self.out_c.has_string_literal( 'initMsgque: can not create login message que %d\\n' )
		assert self.out_c.has_string_literal( 'initMsgque: get inetd msg queue\\n' )
		assert self.out_c.has_string_literal( 'initMsgque: inetdMsgQue has not been created : %m  \\n' )
		assert self.out_c.has_string_literal( 'getLoginAcess: pCmd malloc failed \\n' )
		assert self.out_c.has_string_literal( 'getLoginAcess: get loginaccess from inetd thread,qname:%s\\n' )
		assert self.out_c.has_string_literal( 'getLoginAcess: send login access cmd\\n' )
		assert self.out_c.has_string_literal( 'getLoginAcess: receive login access value \\n' )
		assert self.out_c.has_string_literal( 'getLoginAcess,loginAccess:%d \\n' )
		assert self.out_c.has_string_literal( 'getLoginAcess: error receiving status response : %m \\n' )
		assert self.out_c.has_string_literal( '%s could not open /dev/tty0 to operate\\n' )
		assert self.out_c.has_string_literal( 'User \\"%s\\" logged in.\\n' )
		assert self.out_c.has_string_literal( 'SHELL=%s' )
		assert self.out_c.has_string_literal( 'HOME=%s' )
		assert self.out_c.has_string_literal( 'USER=%s' )
		assert self.out_c.has_string_literal( 'LOGNAME=%s' )
		assert self.out_c.has_string_literal( 'User \\"%s\\" login failure!\\n' )
		assert self.out_c.has_string_literal( '/etc/passwd' )
		assert not self.out_c.has_string_literal( '' )

	def test_check_for_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_200118' )
		assert self.out_c.has_func( 'function_200708' )
		assert self.out_c.has_func( 'function_2007c8' )
		assert self.out_c.has_func( 'function_200904' )
		assert self.out_c.has_func( 'function_200a5c' )
		assert self.out_c.has_func( 'function_202834' )
		assert self.out_c.has_func( 'function_202dc8' )

	def test_check_functions_call_fprintf(self):
		fnc = self.out_c.funcs['function_200708']
		assert fnc.calls('function_202dc8')
		fnc = self.out_c.funcs['function_2007c8']
		assert fnc.calls('function_202dc8')
		fnc = self.out_c.funcs['function_200904']
		assert fnc.calls('function_202dc8')
		fnc = self.out_c.funcs['function_200a5c']
		assert fnc.calls('function_202dc8')


class TestMipsSegmentAtZeroAddress(Test):
	settings = TestSettings(
		input='mips-elf-df0691c3563daddf77f7ac9189475e08',
		args='-k'
	)

	def test_check_for_all_currently_detected_functions(self):
		#assert self.out_c.has_func( 'function_0' )
		#assert self.out_c.has_func( 'function_424' )
		#assert self.out_c.has_func( 'function_1b14' )
		#assert self.out_c.has_func( 'function_1b20' )
		#assert self.out_c.has_func( 'function_1b40' )
		#assert self.out_c.has_func( 'function_1c40' )
		#assert self.out_c.has_func( 'function_1ce0' )
		#assert self.out_c.has_func( 'function_1d54' )
		#assert self.out_c.has_func( 'function_4fac' )
		#assert self.out_c.has_func( 'function_4fd4' )
		assert self.out_c.has_func( '_ftext' ) # entry_point
		#assert self.out_c.has_func( 'function_507c' )
		#assert self.out_c.has_func( 'function_50b4' )
		#assert self.out_c.has_func( 'function_5108' )
		#assert self.out_c.has_func( 'function_5194' )
		#assert self.out_c.has_func( 'function_5224' )
		#assert self.out_c.has_func( 'function_5274' )
		#assert self.out_c.has_func( 'function_5884' )
		#assert self.out_c.has_func( 'function_5b0c' )
		#assert self.out_c.has_func( 'function_5b3c' )
		#assert self.out_c.has_func( 'function_5b64' )
		#assert self.out_c.has_func( 'function_5ba4' )
		#assert self.out_c.has_func( 'function_5bd0' )
		#assert self.out_c.has_func( 'function_5c38' )
		#assert self.out_c.has_func( 'function_5c9c' )
		#assert self.out_c.has_func( 'function_5d00' )
		#assert self.out_c.has_func( 'function_5d68' )
		#assert self.out_c.has_func( 'function_5ddc' )
		#assert self.out_c.has_func( 'function_5e74' )
		#assert self.out_c.has_func( 'function_5ed0' )
		#assert self.out_c.has_func( 'function_5ef4' )
		#assert self.out_c.has_func( 'function_5f4c' )
		#assert self.out_c.has_func( 'function_5f94' )
		#assert self.out_c.has_func( 'function_6464' )
		#assert self.out_c.has_func( 'function_6498' )
		#assert self.out_c.has_func( 'function_6590' )
		#assert self.out_c.has_func( 'function_6608' )
		#assert self.out_c.has_func( 'function_6688' )
		#assert self.out_c.has_func( 'function_66c0' )
		#assert self.out_c.has_func( 'function_67e8' )
		#assert self.out_c.has_func( 'function_6824' )
		#assert self.out_c.has_func( 'function_6884' )
		#assert self.out_c.has_func( 'function_6940' )
		#assert self.out_c.has_func( 'function_6980' )
		#assert self.out_c.has_func( 'function_69bc' )
		#assert self.out_c.has_func( 'function_69d8' )
		#assert self.out_c.has_func( 'function_6dec' )
		#assert self.out_c.has_func( 'function_6e98' )
		#assert self.out_c.has_func( 'function_6ec4' )
		#assert self.out_c.has_func( 'function_6f8c' )
		#assert self.out_c.has_func( 'function_6fc0' )
		#assert self.out_c.has_func( 'function_7114' )
		#assert self.out_c.has_func( 'function_7148' )
		#assert self.out_c.has_func( 'function_7228' )
		#assert self.out_c.has_func( 'function_7260' )
		#assert self.out_c.has_func( 'function_7298' )
		#assert self.out_c.has_func( 'function_7430' )
		#assert self.out_c.has_func( 'function_7490' )
		#assert self.out_c.has_func( 'function_76b0' )
		#assert self.out_c.has_func( 'function_7a44' )
		#assert self.out_c.has_func( 'function_7ad4' )
		#assert self.out_c.has_func( 'function_7dc8' )
		#assert self.out_c.has_func( 'function_7f74' )
		#assert self.out_c.has_func( 'function_7fac' )
		#assert self.out_c.has_func( 'function_83dc' )
		#assert self.out_c.has_func( 'function_8790' )
		#assert self.out_c.has_func( 'function_87c4' )
		#assert self.out_c.has_func( 'function_88e8' )
		#assert self.out_c.has_func( 'function_89fc' )
		#assert self.out_c.has_func( 'function_8c1c' )
		#assert self.out_c.has_func( 'function_8f8c' )
		#assert self.out_c.has_func( 'function_910c' )
		#assert self.out_c.has_func( 'function_919c' )
		#assert self.out_c.has_func( 'function_921c' )
		#assert self.out_c.has_func( 'function_92d4' )
		#assert self.out_c.has_func( 'function_9390' )
		#assert self.out_c.has_func( 'function_95a8' )
		#assert self.out_c.has_func( 'function_9840' )
		#assert self.out_c.has_func( 'function_a098' )
		#assert self.out_c.has_func( 'function_b398' )
		#assert self.out_c.has_func( 'function_bdc0' )
		#assert self.out_c.has_func( 'function_ca40' )
		#assert self.out_c.has_func( 'function_ca9c' )
		#assert self.out_c.has_func( 'function_caf8' )
		#assert self.out_c.has_func( 'function_cb54' )
		#assert self.out_c.has_func( 'function_cbb0' )
		#assert self.out_c.has_func( 'function_cc0c' )
		#assert self.out_c.has_func( 'function_cc68' )
		#assert self.out_c.has_func( 'function_ccc4' )
		#assert self.out_c.has_func( 'function_cd20' )
		#assert self.out_c.has_func( 'function_cdf0' )
		#assert self.out_c.has_func( 'function_cf8c' )
		#assert self.out_c.has_func( 'function_d02c' )
		#assert self.out_c.has_func( 'function_d08c' )
		#assert self.out_c.has_func( 'function_d0ec' )
		#assert self.out_c.has_func( 'function_d14c' )
		#assert self.out_c.has_func( 'function_d270' )
		#assert self.out_c.has_func( 'function_d394' )
		#assert self.out_c.has_func( 'function_d4bc' )
		#assert self.out_c.has_func( 'function_d5e0' )
		#assert self.out_c.has_func( 'function_d704' )
		#assert self.out_c.has_func( 'function_d83c' )
		#assert self.out_c.has_func( 'function_dca8' )
		#assert self.out_c.has_func( 'function_de4c' )
		#assert self.out_c.has_func( 'function_e0d8' )
		#assert self.out_c.has_func( 'function_e43c' )
		#assert self.out_c.has_func( 'function_e70c' )
		#assert self.out_c.has_func( 'function_e7ac' )
		#assert self.out_c.has_func( 'function_e860' )
		#assert self.out_c.has_func( 'function_e88c' )
		#assert self.out_c.has_func( 'function_e92c' )
		#assert self.out_c.has_func( 'function_ea1c' )
		#assert self.out_c.has_func( 'function_eb1c' )
		#assert self.out_c.has_func( 'function_ec54' )
		#assert self.out_c.has_func( 'function_ed40' )
		#assert self.out_c.has_func( 'function_f054' )
		#assert self.out_c.has_func( 'function_f2e4' )
		#assert self.out_c.has_func( 'function_f88c' )
		#assert self.out_c.has_func( 'function_f92c' )
		#assert self.out_c.has_func( 'function_f9cc' )
		#assert self.out_c.has_func( 'function_f9d0' )
		#assert self.out_c.has_func( 'function_fa28' )
		#assert self.out_c.has_func( 'function_10654' )
		#assert self.out_c.has_func( 'function_10688' )

class TestPpc(Test):
	settings = TestSettings(
		input='powerpc-elf-aaf798044d8bb50ee8a7cf79ea3de7e4',
		args='-k'
	)

	def test_check_for_currently_detected_functions(self):
		assert self.out_c.has_func( 'factor' )

	def test_dsm_not_empty_bug_1079(self):
		assert self.out_dsm.contains('; section: .text')

		assert self.out_dsm.contains('93 e1 00 1c\s*stw r31, 0x1c\(r1\)')
		assert self.out_dsm.contains('7c 00 49 d6\s*mullw r0, r0, r9')
		assert self.out_dsm.contains('7d 61 5b 78\s*mr r1, r11')
		assert self.out_dsm.contains('4e 80 00 20\s*blr')

class Testx86(Test):
	settings = TestSettings(
		input='x86-elf-60b7c56f174faf4b617af4d724fda88d',
		args='-k'
	)

	def test_check_all_funcs(self):
		assert self.out_c.has_func( 'function_8048074' )
		assert self.out_c.has_func( 'entry_point' )
		assert self.out_c.has_func( 'function_8048115' )
		assert self.out_c.has_func( 'function_8048122' )
		assert self.out_c.has_func( 'function_8048185' )

	def test_check_function_calls(self):
		fnc = self.out_c.funcs[ 'entry_point' ]
		assert fnc.calls( 'function_8048074' )
		assert fnc.calls( 'write' )
		assert fnc.calls( 'function_8048122' )
		assert fnc.calls( 'function_8048185' )
		assert fnc.calls( 'strncmp' ) or fnc.calls( '_strncmp' )
		# fixme
		#fnc = self.out_c.funcs[ 'function_8048115' ]
		#assert fnc.calls( 'sys_write' )

	#def test_check_string_literals(self):
		# fixme
		#assert self.out_c.has_string_literal( 'Crackme 666 Josep\\n' )
		#assert self.out_c.has_string_literal( 'Password: ' )
		#assert self.out_c.has_string_literal( 'No\\n: ' )
		#assert self.out_c.has_string_literal( 'OK\\n: ' )

	def test_check_non_empty_dsm(self):
		assert self.out_dsm.contains( r'0x804807e:\s+31 c0\s+xor eax, eax' )
		# jk: we do not detect the following string in C/dsm because
		# it is stored in a unique way, which is not supported at the moment
		#assert self.out_dsm.contains( r'0x8048096:\s+b9 9a 91 04 08\s+mov ecx, 0x804919a ;\s+"Crackme 666 Josep\\n\\x00"' )
		assert self.out_dsm.contains( r'0x8048096:\s+b9 9a 91 04 08\s+mov ecx, 0x804919a ;.*' )
		assert self.out_dsm.contains( r'0x8048199:\s+c3\s+ret' )
		assert self.out_dsm.contains( r'0x80491ad:.*"Password: "' )

class Testx86SkipSectionsDecompileSegments(Test):
	settings = TestSettings(
		input='x86-elf-55176135365131cf2132d8f0000308c1',
		args='-k'
	)

	def test_check_all_currently_detected_funcs(self):
		assert self.out_c.has_func( 'function_8048600' )
		assert self.out_c.has_func( 'entry_point' )

	def test_check_function_calls(self):
		fnc = self.out_c.funcs[ 'entry_point' ]
		assert fnc.calls( 'function_8048600' )

	def test_check_non_empty_dsm(self):
		assert self.out_dsm.contains( r'0x80486a0:\s+31 ed\s+xor ebp, ebp' )
		assert self.out_dsm.contains( r'0x80486bc:\s+e8 3f ff ff ff\s+call 0x8048600 <function_8048600>' )
