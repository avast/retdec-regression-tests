from regression_tests import *

class Test1(Test):
	settings=TestSettings(
		input='[TO]Mutant.be4660a3'
	)

	def test(self):
		assert self.out_c.has_funcs('entry_point')
		assert self.out_c.funcs['entry_point'].calls('VirtualProtect', 'VirtualAlloc')

class Test2(Test):
	settings = TestSettings(
		args='--backend-disabled-opts CopyPropagation',
		input='ImportDescriptorCrossesPage.ex'
	)

	def test(self):
		assert self.out_c.funcs['function_401ac0'].calls('Sleep', 'GetVersionExA')

class Test_05e86f02582da7e1103b53b6136c1e62(Test):
	settings=TestSettings(
		input='05e86f02582da7e1103b53b6136c1e62.vxe'
	)

	def test(self):
		assert self.out_c.has_funcs('entry_point')
		assert self.out_c.funcs['entry_point'].calls('GetModuleHandleA', 'GetWindowThreadProcessId',
			'OpenProcess', 'FindWindowA', 'VirtualFreeEx', 'VirtualAllocEx', 'CreateRemoteThread',
			'ExitProcess')
		assert r'shell_traywnd' in self.out_c.string_literal_values
		#assert r'http://toptwo.3322.org/img/aa.exe' in self.out_c.string_literal_values

class Test_07143bf9233c29683460adeac4ec5b11(Test):
	settings=TestSettings(
		input='07143bf9233c29683460adeac4ec5b11.vxe'
	)

	def test(self):
		assert self.out_c.has_funcs('entry_point')
		assert self.out_c.funcs['entry_point'].calls('GetModuleHandleA', 'GetProcAddress',
			'FindWindowA', 'GetStartupInfoA', 'CreateProcessA', 'ExitProcess', 'GetWindowThreadProcessId',
			'OpenProcess', 'VirtualAllocEx', 
			# Present in output C, but not found by framework on Windows (probably bad C parsing)
			#'WriteProcessMemory', 'CloseHandle', 'CreateRemoteThread'
			)
		assert r'Kernel32.dll' in self.out_c.string_literal_values
		assert r'C:\\Program Files\\Internet Explorer\\iexplore.exe' in self.out_c.string_literal_values

class Test_074190bfb0a383539f695d885618fd54(Test):
	settings=TestSettings(
		input='074190bfb0a383539f695d885618fd54.vxe'
	)

	def test(self):
		assert self.out_c.has_funcs('entry_point')
		assert self.out_c.funcs['entry_point'].calls('GetTempPathA', 'lstrcatA',
			'memset', 'strcat', 'URLDownloadToFileA', 'CreateProcessA')
		assert r'msarch1.exe' in self.out_c.string_literal_values
		assert r'nordbbs.com/rel/msarch1.exe' in self.out_c.string_literal_values

class Test_0922b80e59bf37eb6dbbb62263f8473e(Test):
	settings=TestSettings(
		input='0922b80e59bf37eb6dbbb62263f8473e.vxe'
	)

	def test(self):
		assert self.out_c.has_funcs('entry_point')
		assert self.out_c.funcs['entry_point'].calls('wsprintfA', '__asm_rep_stosd_memset',
			'ExitProcess', 'inet_ntoa', )
		assert r'microsoft.com' in self.out_c.string_literal_values
		assert r'http://85.255.113.26/hello.php' in self.out_c.string_literal_values
		assert r'IcmpSendEcho' in self.out_c.string_literal_values

class TestOnlyEp(Test):
	settings=TestSettings(
		input=['WINKERNE.EXE---elkern-----elkern---', '2E4BA89B5C529173B2AF2D97245D260A.ex', '66F1225AC976107169EA9CFC103333F2.ex',
			'77757A0F31F7217F706BC510BA427899.ex', '89005A881F694EBBDC072EE74C328801.ex', 'EE383DAF4D9F0774141F9E2FD8E93730.ex', 'F8EEE82B5150B75D4B176CD9804C9F2B.ex']
	)

	def test(self):
		assert self.out_c.has_funcs('entry_point')

class TestEmpty(Test):
    settings=TestSettings(
        input='empty.elf'
    )

    def setUp(self):
        pass

    def test_output_has_no_functions(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'Error: No instructions were decoded')
