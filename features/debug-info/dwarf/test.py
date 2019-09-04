from regression_tests import *

class DWARFTest(Test):
    """Ensures that debug info is detected, stored in the JSON config, and
    properly emitted in the back-end to the resulting C code.
    """

    settings = TestSettings(
        input='debug-info.ex'
    )

    def test_original_func_names_are_used(self):
        self.assertEqual(self.out_c.func_names, ['func', 'main'])

    def test_address_ranges_are_emitted(self):
        assert self.out_c.has_comment_matching(r'// Address range: *0x401560 - 0x401598')
        assert self.out_c.has_comment_matching(r'// Address range: *0x401598 - 0x4015ce')

    def test_line_ranges_are_emitted(self):
        assert self.out_c.has_comment_matching(r'// Line range: *10 - 14')
        assert self.out_c.has_comment_matching(r'// Line range: *16 - 21')

    def test_module_name_is_emitted(self):
        assert self.out_c.has_comment_matching(r'// From module: *.*debug-info.c')

    def test_variables_have_assigned_name_from_debug_info(self):
        # Global variables.
        self.assertTrue(self.out_c.has_global_var('g'))
        # Parameters.
        self.assertEqual(self.out_c.funcs['func'].params[0].name, 'a')
        self.assertEqual(self.out_c.funcs['main'].param_count, 0)

        self.out_c.funcs['main'].calls('func')
