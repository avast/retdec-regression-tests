from regression_tests import *

class UpxDecompilationTest(Test):
    settings = TestSettings(
        input = [
            'arm_elf_gcc_nrv2b_modified',
            'mipsBE_elf_gcc_nrv2b_modified',
            'mipsLE_elf_gcc_nrv2b_modified',
            'ppc_elf_gcc_nrv2b_modified',
            'x86_elf_gcc_nrv2b_modified',
            'x86_pe_gcc_nrv2b_modified',
            'x86_pe_msvc_nrv2b_modified'
        ]
    )

    def test_upx_decompilation(self):
        assert self.out_c.has_func('main')
        assert self.out_c.has_string_literal('IZP Projekt c.3 - Riesenie osemsmerovky')
