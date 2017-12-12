from regression_tests import *

class TinyElfHelloWorldTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='hello_world.elf'
	)

	def test_tiny_elf_hello_world(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 1)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0x84)

class TinyElfTwoSegmentsTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='two_segments.elf'
	)

	def test_tiny_elf_two_segments(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 2)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0x96)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], 'seg0001')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['address'], 16), 0x401000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['size'], 16), 0x0e)

class TinyElfOverlappingSegmentsTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='overlapping_segments.elf'
	)

	def test_tiny_elf_overlapping_segments(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 3)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0xb6)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], 'seg0002')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['address'], 16), 0x401000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['size'], 16), 0x05)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['name'], 'seg0001')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][2]['address'], 16), 0x401005)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][2]['size'], 16), 0x09)

class TinyElfSegmentsCloseTogetherTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='segments_close_together.elf'
	)

	def test_tiny_elf_overlapping_segments(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 3)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0xa0)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], 'seg0001')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['address'], 16), 0x4000a0)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['size'], 16), 0x0e)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['name'], 'seg0002')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][2]['address'], 16), 0x4000ae)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][2]['size'], 16), 0xf52)

class TinyElfUnalignedSegmentTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='unaligned_segment.elf'
	)

	def test_tiny_elf_unaligned_segment(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 2)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], 'seg0000')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x400000)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0xa4)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], 'seg0001')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['address'], 16), 0x401010)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['size'], 16), 0x20)

class TinyElfHelloWorldWithSectionsTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='hello_world_with_sections.elf'
	)

	def test_hello_world_with_sections(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x400054)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 2)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '.text')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x400054)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0x22)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '.data')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['address'], 16), 0x400076)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['size'], 16), 0x0e)

class GccElfHelloWorldTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='gcc_elf_hello_world'
	)

	def test_gcc_elf_hello_world(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x8048134)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 24)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][11]['name'], '.text')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][11]['address'], 16), 0x80482f0)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][11]['size'], 16), 0x20c)

class MipsElfInvalidLoadableSectionsTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='mips-elf-6342ef9c64f685f8c8bff75c0bd95a0a'
	)

	def test_mips_elf_invalid_loadable_sections(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x0)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 1)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '.reginfo')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x0)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0x18)

class x86ElfRelSectionsWithInvalidOffsetTest(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--json --verbose',
		input='x86-elf-1a2ed6de27220fc97ecf51632568cbcf'
	)

	def test_x86_elf_rel_sections_with_invalid_offset(self):
		assert self.fileinfo.succeeded
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['baseAddress'], 16), 0x100)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['numberOfSegments']), 3)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][0]['name'], '.text')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['address'], 16), 0x100)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][0]['size'], 16), 0x222)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][1]['name'], '.data')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['address'], 16), 0x330)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][1]['size'], 16), 0x547)

		self.assertEqual(self.fileinfo.output['loaderInfo']['segments'][2]['name'], '.bss')
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][2]['address'], 16), 0x880)
		self.assertEqual(int(self.fileinfo.output['loaderInfo']['segments'][2]['size'], 16), 0x26)

class ArmElfLoadableSegmentContainsJustOneBssSection(Test):
	settings = TestSettings(
		tool='fileinfo',
		args='--verbose',
		input='arm-elf-0192a0865465dd3be7984cf3735b8ee4'
	)

	def test_output_contains_warning(self):
		assert self.fileinfo.succeeded
		assert self.fileinfo.output.contains(r'Warning: Segment with single BSS section mapped to it. This may cause problems with instruction decoding.')
