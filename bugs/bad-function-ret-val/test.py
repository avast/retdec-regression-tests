from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='three-funcs.arm.clang.O1.elf',
	)

	def test_all_funcs(self):
		assert self.out_c.has_just_funcs( 'main', 'man', 'dan', 'zan' )

		main = self.out_c.funcs['main']
		assert main.return_type.is_int()
		assert main.has_just_params('argc', 'argv')
		assert main.calls('rand', 'man', 'dan', 'zan')

		man = self.out_c.funcs['man']
		assert man.return_type.is_int()
		assert man.has_just_params('a1', 'a2')
		assert man.params['a1'].type.is_int(32)
		assert man.params['a2'].type.is_int(32)

		dan = self.out_c.funcs['dan']
		assert dan.return_type.is_int()
		assert dan.has_just_params('a1', 'a2')
		assert dan.params['a1'].type.is_int(32)
		assert dan.params['a2'].type.is_int(32)

		zan = self.out_c.funcs['zan']
		assert zan.return_type.is_int()
		assert zan.has_just_params('a1', 'a2')
		assert zan.params['a1'].type.is_int(32)
		assert zan.params['a2'].type.is_int(32)
