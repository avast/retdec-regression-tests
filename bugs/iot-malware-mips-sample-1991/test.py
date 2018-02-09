#
# Tests sample 19911CB32B0B58D49D1FF694D4AEB979 from #732.
# Tests mainly detection of functions called by syscall, but also same other importat things.
#

from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='1991',
		args='-k'
	)

	# Syscalled functions are added as linked and should be dumpped as comments in "External Functions" section.
	#
	def test_external_fncs_from_syscalls(self):
		assert self.out_c.has_comment_matching(r'.*int.*bind\(.*\);')
		assert self.out_c.has_comment_matching(r'.*getpid\(void\);')
		assert self.out_c.has_comment_matching(r'.*int ioctl\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int kill\(.*pid, int sig\);')
		assert self.out_c.has_comment_matching(r'.*int.*listen\(.*\);')
		assert self.out_c.has_comment_matching(r'.*void.*\*.*mmap\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int nanosleep\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int rmdir\(.*\);')          # in getpid's function_4151f0()
		assert self.out_c.has_comment_matching(r'.*int.*setsockopt\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int sigprocmask\(.*\);')
		assert self.out_c.has_comment_matching(r'.*int unlink\(.*\);')         # in mmap's function_415010()
		assert self.out_c.has_comment_matching(r'.*ssize_t write\(.*\);')      # in mmap's function_415010()

	# Right now, we can not check if function X calls function Y, so we just check presence of functions calling syscalls.
	# Note: this is after my (Matula) modification of MIPS syscall analysis, there is not import creation, stub fnc are generated.
	#
	def test_has_functions_using_syscalls(self):
		assert self.out_c.has_func( 'function_4152b0' ) # bind()
		#assert self.out_c.has_func( 'function_4151f0' ) # getpid()
		assert self.out_c.has_func( 'function_4152d0' ) # ioctl()
		#assert self.out_c.has_func( 'function_415150' ) # kill()
		#assert self.out_c.has_func( 'function_414e40' ) # listen()
		#assert self.out_c.has_func( 'function_415010' ) # mmap()
		#assert self.out_c.has_func( 'function_4152f0' ) # nanosleep()
		assert self.out_c.has_func( 'function_415230' ) # setsockopt()
		#assert self.out_c.has_func( 'function_417750' ) # sigprocmask()
