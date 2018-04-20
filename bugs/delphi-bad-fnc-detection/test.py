
from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='87aa7cdd066541293ffd6761e07b3dad',
		args='-k'
	)

	# Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
	#
	def test_check_for_all_currently_detected_functions(self):
		assert self.out_c.has_func( 'GetStdHandle2' )  # _GetStdHandle
		assert self.out_c.has_func( 'UnhandledExceptionFilter2' )  #
		assert self.out_c.has_func( 'WriteFile2' )  #
		assert self.out_c.has_func( 'ExitProcess2' )  #
		assert self.out_c.has_func( 'function_401e84' )  #
		assert self.out_c.has_func( 'FreeLibrary2' )  #
		assert self.out_c.has_func( 'function_401040' )  #
		assert self.out_c.has_func( 'GetStartupInfo' )  #
		assert self.out_c.has_func( 'RegCloseKey2' )  #
		assert self.out_c.has_func( 'RegOpenKeyEx' )  #
		assert self.out_c.has_func( 'RegQueryValueEx' )  #
		assert self.out_c.has_func( 'function_401068' )  #
		assert self.out_c.has_func( 'LocalFree2' )  #
		assert self.out_c.has_func( 'VirtualFree2' )  #
		assert self.out_c.has_func( 'EnterCriticalSection2' )  #
		assert self.out_c.has_func( 'LeaveCriticalSection2' )  #
		assert self.out_c.has_func( 'DeleteCriticalSection2' )  #
		assert self.out_c.has_func( 'MakeEmpty' )  #
		assert self.out_c.has_func( 'GetKeyboardType2' )  #
		assert self.out_c.has_func( '_40_FpuInit' )  #
		assert self.out_c.has_func( 'function_401ad4' )  #
		assert self.out_c.has_func( 'function_401b90' )  #
		assert self.out_c.has_func( 'GetModuleHandle' )  #

		assert self.out_c.has_func( 'function_401cf4' )  #
		assert self.out_c.has_func( 'TlsGetValue2' )  #
		assert self.out_c.has_func( 'TlsSetValue2' )  #
		assert self.out_c.has_func( 'AllocTlsBuffer' )  #
		assert self.out_c.has_func( 'InitializeModule' )  #
		assert self.out_c.has_func( 'function_401e24' )  #
		assert self.out_c.has_func( 'function_401e5c' )  #
		assert self.out_c.has_func( 'function_401e64' )  #
		assert self.out_c.has_func( 'function_401e6c' )  #
		assert self.out_c.has_func( 'function_401e74' )  #
		assert self.out_c.has_func( 'function_401e7c' )  #
		assert self.out_c.has_func( 'function_401e84' )  #
		assert self.out_c.has_func( 'function_401e8c' )  #
		assert self.out_c.has_func( 'function_401ec4' )  #
		assert self.out_c.has_func( 'function_401efc' )  #
		assert self.out_c.has_func( 'function_401f04' )  #
