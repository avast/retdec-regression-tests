from regression_tests import *

class PDBTest(Test):
    """Checks basic handling of debug information from PDB files."""

    settings = CriticalTestSettings(
        input='manyvars.ex',
        pdb='manyvars.pdb'
    )

    def test_debug_info_was_used(self):
        # Function names.
        assert self.out_c.has_func('nejaka_funkce')
        assert self.out_c.has_func('volaci_funkce')
        assert self.out_c.has_func('smichana_funkce')

        # Address ranges.
        # As of commit 2373564, we do not use line info from debug information
        # to obtain address ranges. The following address ranges are thus not
        # obtained from debug information. Addresses ranges from debug
        # information are:
        #
        #     0x11000 - 0x11147
        #     0x11234 - 0x1130b
        #     0x11328 - 0x1154c
        #
        assert self.out_c.has_comment_matching(r'// Address range:\s*0x11000 - 0x1113b')
        assert self.out_c.has_comment_matching(r'// Address range:\s*0x11234 - 0x1130f')
        assert self.out_c.has_comment_matching(r'// Address range:\s*0x11328 - 0x114bf')

        # Line ranges.
        assert self.out_c.has_comment_matching(r'// Line range:\s*7 - 29')
        assert self.out_c.has_comment_matching(r'// Line range:\s*45 - 53')

        # Module names.
        assert self.out_c.has_comment_matching(r'// From module:\s*c:\\cpp\\manyvars\\manyvars\\windows mobile 6 standard sdk \(armv4i\)\\debug\\manyvars.obj')

        # Parameter names.
        self.assertEqual(self.out_c.funcs['nejaka_funkce'].params[0].name, 'aa')
        self.assertEqual(self.out_c.funcs['nejaka_funkce'].params[1].name, 'bb')
        self.assertEqual(self.out_c.funcs['nejaka_funkce'].params[2].name, 'str')
        self.assertEqual(self.out_c.funcs['nejaka_funkce'].params[3].name, 'cc')
        self.assertEqual(self.out_c.funcs['nejaka_funkce'].params[4].name, 'dd')
        self.assertEqual(self.out_c.funcs['nejaka_funkce'].params[5].name, 'ee')

        # Local-variable names.
        assert self.out_c.contains(r'v1')
        assert self.out_c.contains(r'v2')
        assert self.out_c.contains(r'v3')

    # rand = function_114d0
    # puts = function_11530
    def test_bug_1227(self):
        main = self.out_c.funcs['main']
        assert main.calls('nejaka_funkce', 'volaci_funkce', 'function_114d0')

        volaci_funkce = self.out_c.funcs['volaci_funkce']
        assert volaci_funkce.calls('function_114d0', 'smichana_funkce', 'printf', 'function_11530', '_itod', '_addd', '_dtos')

        smichana_funkce = self.out_c.funcs['smichana_funkce']
        assert smichana_funkce.calls('printf', '_stod', '_muld', '_itod', '_addd', '_dtoi')

        nejaka_funkce = self.out_c.funcs['nejaka_funkce']
        assert nejaka_funkce.calls('function_114d0', 'printf')
