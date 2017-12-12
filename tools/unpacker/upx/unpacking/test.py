from regression_tests import *

class TestLzma(Test):
	settings = TestSettings(
		tool='unpacker',
		input=[
			'x86_pe_gcc_lzma_modified',
			'x86_pe_msvc_lzma_modified',
			'x86_elf_gcc_lzma_modified',
			'mipsLE_elf_gcc_lzma_modified',
			'mipsBE_elf_gcc_lzma_modified',
			'arm_elf_gcc_lzma_modified',
			'ppc_elf_gcc_lzma_modified',
			'x64_elf_gcc_lzma_modified',
			'x86_pedll_msvc_lzma_modified',
			'x64_pe_gcc_lzma_modified',
			'x86_macho_clang_lzma_modified',
			'x64_macho_clang_lzma_modified',
			'arm_macho_clang_lzma_modified',
			'x86_x64_macho_clang_lzma_modified'
		]
	)

	def test_lzma(self):
		assert self.unpacker.succeeded
		assert self.unpacker.output.contains('LZMA')

class TestNrv2b(Test):
	settings = TestSettings(
		tool='unpacker',
		input=[
			'x86_pe_gcc_nrv2b_modified',
			'x86_pe_msvc_nrv2b_modified',
			'x86_elf_gcc_nrv2b_modified',
			'mipsLE_elf_gcc_nrv2b_modified',
			'mipsBE_elf_gcc_nrv2b_modified',
			'arm_elf_gcc_nrv2b_modified',
			'ppc_elf_gcc_nrv2b_modified',
			'x64_elf_gcc_nrv2b_modified',
			'x86_pedll_msvc_nrv2b_modified',
			'x64_pe_gcc_nrv2b_modified',
			'x86_macho_clang_nrv2b_modified',
			'x64_macho_clang_nrv2b_modified',
			'arm_macho_clang_nrv2b_modified',
			'x86_x64_macho_clang_nrv2b_modified'
		]
	)

	def test_nrv2b(self):
		assert self.unpacker.succeeded
		assert self.unpacker.output.contains('NRV2B')

class TestNrv2d(Test):
	settings = TestSettings(
		tool='unpacker',
		input=[
			'x86_pe_gcc_nrv2d_modified',
			'x86_pe_msvc_nrv2d_modified',
			'x86_elf_gcc_nrv2d_modified',
			'mipsLE_elf_gcc_nrv2d_modified',
			'mipsBE_elf_gcc_nrv2d_modified',
			'arm_elf_gcc_nrv2d_modified',
			'ppc_elf_gcc_nrv2d_modified',
			'x64_elf_gcc_nrv2d_modified',
			'x86_pedll_msvc_nrv2d_modified',
			'x64_pe_gcc_nrv2d_modified',
			'x86_macho_clang_nrv2d_modified',
			'x64_macho_clang_nrv2d_modified',
			'arm_macho_clang_nrv2d_modified',
			'x86_x64_macho_clang_nrv2d_modified'
		]
	)

	def test_nrv2d(self):
		assert self.unpacker.succeeded
		assert self.unpacker.output.contains('NRV2D')

class TestNrv2e(Test):
	settings = TestSettings(
		tool='unpacker',
		input=[
			'x86_pe_gcc_nrv2e_modified',
			'x86_pe_msvc_nrv2e_modified',
			'x86_elf_gcc_nrv2e_modified',
			'mipsLE_elf_gcc_nrv2e_modified',
			'mipsBE_elf_gcc_nrv2e_modified',
			'arm_elf_gcc_nrv2e_modified',
			'ppc_elf_gcc_nrv2e_modified',
			'x64_elf_gcc_nrv2e_modified',
			'x86_pedll_msvc_nrv2e_modified',
			'x64_pe_gcc_nrv2e_modified',
			'x86_macho_clang_nrv2e_modified',
			'x64_macho_clang_nrv2e_modified',
			'arm_macho_clang_nrv2e_modified',
			'x86_x64_macho_clang_nrv2e_modified'
		]
	)

	def test_nrv2e(self):
		assert self.unpacker.succeeded
		assert self.unpacker.output.contains('NRV2E')

class TestBruteUltrabrute(Test):
	settings = TestSettings(
		tool='unpacker',
		input=[
			'x86_pe_gcc_brute_modified',
			'x86_pe_gcc_ultrabrute_modified',
			'x86_pe_msvc_brute_modified',
			'x86_pe_msvc_ultrabrute_modified',
			'x86_elf_gcc_brute_modified',
			'x86_elf_gcc_ultrabrute_modified',
			'mipsLE_elf_gcc_brute_modified',
			'mipsLE_elf_gcc_ultrabrute_modified',
			'mipsBE_elf_gcc_brute_modified',
			'mipsBE_elf_gcc_ultrabrute_modified',
			'arm_elf_gcc_brute_modified',
			'arm_elf_gcc_ultrabrute_modified',
			'ppc_elf_gcc_brute_modified',
			'ppc_elf_gcc_ultrabrute_modified',
			'x64_elf_gcc_brute_modified',
			'x64_elf_gcc_ultrabrute_modified',
			'x86_pedll_msvc_brute_modified',
			'x86_pedll_msvc_ultrabrute_modified',
			'x64_pe_gcc_brute_modified',
			'x64_pe_gcc_ultrabrute_modified',
			'x86_macho_clang_brute_modified',
			'x86_macho_clang_ultrabrute_modified',
			'x64_macho_clang_brute_modified',
			'x64_macho_clang_ultrabrute_modified',
			'arm_macho_clang_brute_modified',
			'arm_macho_clang_ultrabrute_modified',
			'x86_x64_macho_clang_brute_modified',
			'x86_x64_macho_clang_ultrabrute_modified'
		]
	)

	def test_brute_ultrabrute(self):
		assert self.unpacker.succeeded
