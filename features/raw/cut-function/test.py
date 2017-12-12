from regression_tests import *

# Not all raw decompilations can pass this test.
#
class FullTest(Test):

	called_fnc=''

	def test_ack_function(self):
		assert self.out_c.has_funcs( 'entry_point' )
		fnc = self.out_c.funcs['entry_point']

		assert fnc.return_type.is_int()
		assert fnc.has_just_params('a1', 'a2')
		assert fnc.params['a1'].type.is_int(32)
		assert fnc.params['a2'].type.is_int(32)
		assert fnc.calls(self.called_fnc, 'entry_point')

class TestArmClangElf(Test):
	settings = TestSettings(
		input='ack-arm-elf-little-clang-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='arm',
		args='-k --endian little --raw-section-vma 0x85a4 --raw-entry-point 0x85a4'
	)

	def test_function(self):
		assert self.out_c.has_just_funcs( 'entry_point' )
		fnc = self.out_c.funcs['entry_point']

		assert fnc.return_type.is_int()
		assert fnc.calls('unknown_844c', 'entry_point')

class TestArmGccElf(FullTest):
	settings = TestSettings(
		input='ack-arm-elf-little-gcc-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='arm',
		args='-k --endian little --raw-section-vma 0x85a4 --raw-entry-point 0x85a4'
	)

	called_fnc='unknown_844c'

class TestArmGccExe(FullTest):
	settings = TestSettings(
		input='ack-arm-pe-little-gcc-O0.bin.exe-fnc.raw',
		mode='raw',
		arch='arm',
		args='-k --endian little --raw-section-vma 0x11054 --raw-entry-point 0x11054'
	)

	called_fnc='unknown_1171c'

class TestMipsClangElf(FullTest):
	settings = TestSettings(
		input='ack-mips-elf-big-clang-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='mips',
		args='-k --endian big --raw-section-vma 0x400710 --raw-entry-point 0x400710'
	)

	called_fnc='unknown_400aa0'

class TestMipsGccElf(FullTest):
	settings = TestSettings(
		input='ack-mips-elf-little-gcc-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='mips',
		args='-k --endian little --raw-section-vma 0x8900368 --raw-entry-point 0x8900368'
	)

	called_fnc='unknown_89005e4'

class TestPic32GccElf(Test):
	settings = TestSettings(
		input='ack-pic32-elf-little-gcc-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='pic32',
		args='-k --endian little --raw-section-vma 0x9d001bf4 --raw-entry-point 0x9d001bf4'
	)

	def test_function(self):
		assert self.out_c.has_funcs( 'entry_point' )
		fnc = self.out_c.funcs['entry_point']

		assert fnc.return_type.is_int()
		assert fnc.has_params('a1', 'a2')
		assert fnc.params['a1'].type.is_int(32)
		assert fnc.params['a2'].type.is_int(32)
		assert fnc.calls('unknown_9d0028dc', 'entry_point')

class TestPowerpcClangElf(Test):
	settings = TestSettings(
		input='ack-powerpc-elf-big-clang-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='powerpc',
		args='-k --endian big --raw-section-vma 0x100004dc --raw-entry-point 0x100004dc'
	)

	def test_function(self):
		assert self.out_c.has_funcs( 'entry_point' )
		fnc = self.out_c.funcs['entry_point']

		assert fnc.return_type.is_int()
		assert fnc.calls('unknown_10000810', 'entry_point')

class TestPowerpcGccElf(FullTest):
	settings = TestSettings(
		input='ack-powerpc-elf-big-gcc-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='powerpc',
		args='-k --endian big --raw-section-vma 0x100004dc --raw-entry-point 0x100004dc'
	)

	called_fnc='unknown_100007d0'

class TestThumbClangElf(Test):
	settings = TestSettings(
		input='ack-thumb-elf-little-clang-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='thumb',
		args='-k --endian little --raw-section-vma 0x85a4 --raw-entry-point 0x85a5'
	)

	def test_function(self):
		assert self.out_c.has_funcs( 'entry_point' )
		fnc = self.out_c.funcs['entry_point']

		assert fnc.calls('unknown_844c', 'entry_point')

class TestThumbGccElf(Test):
	settings = TestSettings(
		input='ack-thumb-elf-little-gcc-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='thumb',
		args='-k --endian little --raw-section-vma 0x85b0 --raw-entry-point 0x85b1'
	)

	def test_function(self):
		assert self.out_c.has_funcs( 'entry_point' )
		fnc = self.out_c.funcs['entry_point']

		assert fnc.calls('unknown_8450', 'entry_point')

class TestX86ClangElf(FullTest):
	settings = TestSettings(
		input='ack-x86-elf-little-clang-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='x86',
		args='-k --endian little --raw-section-vma 0x8048550 --raw-entry-point 0x8048550'
	)

	called_fnc='unknown_80483f0'

class TestX86ClangExe(FullTest):
	settings = TestSettings(
		input='ack-x86-pe-little-clang-O0.bin.exe-fnc.raw',
		mode='raw',
		arch='x86',
		args='-k --endian little --raw-section-vma 0x401560 --raw-entry-point 0x401560'
	)

	called_fnc='unknown_407598'

class TestX86GccElf(FullTest):
	settings = TestSettings(
		input='ack-x86-elf-little-gcc-O0.bin.elf-fnc.raw',
		mode='raw',
		arch='x86',
		args='-k --endian little --raw-section-vma 0x804854c --raw-entry-point 0x804854c'
	)

	called_fnc='unknown_80483f0'

class TestX86GccExe(FullTest):
	settings = TestSettings(
		input='ack-x86-pe-little-gcc-O0.bin.exe-fnc.raw',
		mode='raw',
		arch='x86',
		args='-k --endian little --raw-section-vma 0x401560 --raw-entry-point 0x401560'
	)

	called_fnc='unknown_407558'
