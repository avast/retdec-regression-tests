from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='628d',
		args='-k'
	)

	def test_check_reg_names_in_dsm(self):

		assert self.out_dsm.contains('0x8048343:\s*53\s*push ebx')
		assert self.out_dsm.contains('0x8048378:\s*ff 14 85 34 96 04 08\s*call dword ptr \[eax\*4 \+ 0x8049634\]')
		assert self.out_dsm.contains('0x80483ee:\s*88 10\s*mov byte ptr \[eax\], dl')
		assert self.out_dsm.contains('0x8048428:\s*88 44 1c 20\s*mov byte ptr \[esp \+ ebx \+ 0x20\], al')
		assert self.out_dsm.contains('0x8048436:\s*89 44 24 38\s*mov dword ptr \[esp \+ 0x38\], eax')
		assert self.out_dsm.contains('0x804844d:\s*8b 5d fc\s*mov ebx, dword ptr \[ebp \- 4\]')
		assert self.out_dsm.contains('0x80484ab:\s*ff 94 b3 20 ff ff ff\s*call dword ptr \[ebx \+ esi\*4 \- 0xe0\]')
