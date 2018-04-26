from regression_tests import *

class libndmComponents(Test):

	settings = TestSettings(
		input='libndmComponents.so',
		args='-k'
	)

	def test_for_some_functions(self):
		assert self.out_c.has_func( '_ftext' ) # entry_point
		assert self.out_c.has_func( '_ZNK7Command7RequestixERK7CString' )
		assert self.out_c.has_func( '_ZN4HTTP2IO8DirectFd8WriteAllEPKvj' )
		assert self.out_c.has_func( '_ZN3Xml8Document12AllocateNodeENS_4Node5TypeTERK7CStringS5_' )
		assert self.out_c.has_func( '_ZN4HTTP2IO8DirectFd7ReadAllEPvj' )
		assert self.out_c.has_func( '_ZN5Event8ProgressC1ERK7CStringm7RebootT' )
		assert self.out_c.has_func( '_ZN6Thread9SetStatusEP6Status' )
		assert self.out_c.has_func( '_ZN9StatusLogC1E7ReturnTN3Log6LevelTEPKcS4_P6Status' )
		assert self.out_c.has_func( '_ZNK3Xml4Node9FirstNodeERK7CString' )
		assert self.out_c.has_func( '_ZNK7Command4Base12ConfiguratorEv' )
		assert self.out_c.has_func( '_ZNK9StringMap4SizeEv' )

class x86_elf_60b7c56f174faf4b617af4d724fda88d(Test):

	settings = TestSettings(
		input='x86-elf-60b7c56f174faf4b617af4d724fda88d',
		args='-k'
	)

	def test_for_all_functions(self):
		assert self.out_c.has_func( 'function_8048074' )
		assert self.out_c.has_func( 'entry_point' )
		assert self.out_c.has_func( 'function_8048115' )
		assert self.out_c.has_func( 'function_8048122' )
		assert self.out_c.has_func( 'function_8048185' )
