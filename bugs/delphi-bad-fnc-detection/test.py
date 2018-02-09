
from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='87aa7cdd066541293ffd6761e07b3dad',
		args='-k'
	)

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'function_401000' )  # _GetStdHandle
		assert self.out_c.has_func( '_UnhandledExceptionFilter' )  #
		assert self.out_c.has_func( '_WriteFile' )  #
		assert self.out_c.has_func( '_ExitProcess' )  #
		assert self.out_c.has_func( '_MessageBoxA' )  #
		assert self.out_c.has_func( '_FreeLibrary' )  #
		assert self.out_c.has_func( '_GetCommandLineA' )  #
		assert self.out_c.has_func( '_GetStartupInfoA' )  #
		assert self.out_c.has_func( '_RegCloseKey' )  #
		assert self.out_c.has_func( '_RegOpenKeyExA' )  #
		assert self.out_c.has_func( '_RegQueryValueExA' )  #
		assert self.out_c.has_func( '_GetCurrentThreadId' )  #
		assert self.out_c.has_func( '_LocalFree' )  #
		assert self.out_c.has_func( '_VirtualFree' )  #
		assert self.out_c.has_func( '_EnterCriticalSection' )  #
		assert self.out_c.has_func( '_LeaveCriticalSection' )  #
		assert self.out_c.has_func( '_DeleteCriticalSection' )  #
		assert self.out_c.has_func( 'function_4010bc' )  #
		assert self.out_c.has_func( '_GetKeyboardType' )  #
		assert self.out_c.has_func( 'function_40136c' )  #
		assert self.out_c.has_func( 'function_401799' )  #
		assert self.out_c.has_func( 'function_401ad4' )  #
		assert self.out_c.has_func( 'function_401b90' )  #
		assert self.out_c.has_func( '_GetModuleHandleA' )  #
		assert self.out_c.has_func( '_LocalAlloc' )  #
		assert self.out_c.has_func( '_TlsGetValue' )  #
		assert self.out_c.has_func( '_TlsSetValue' )  #
		assert self.out_c.has_func( 'function_401d0c' )  #
		assert self.out_c.has_func( 'function_401da4' )  #
		assert self.out_c.has_func( 'function_401e22' )  # function_401e24
		assert self.out_c.has_func( 'function_401e5a' )  # function_401e5c
		assert self.out_c.has_func( '_CompareStringA' )  #
		assert self.out_c.has_func( '_FindWindowA' )  #
		assert self.out_c.has_func( '_FindWindowExA' )  #
		assert self.out_c.has_func( '_GetClassNameA' )  #
		assert self.out_c.has_func( '_MessageBoxA' )  #
		assert self.out_c.has_func( '_SendMessageA' )  #
		assert self.out_c.has_func( 'function_401ec2' )  # function_401ec4
		assert self.out_c.has_func( 'function_401efa' )  # function_401efc
		assert self.out_c.has_func( 'function_401f04' )  #
		assert self.out_c.has_func( 'entry_point' )  #
