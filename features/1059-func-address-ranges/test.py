from regression_tests import *

class WithDebugInfo(Test):
    """Tests the emission and use of address ranges when debug info is present (#1059)."""

    settings = TestSettings(
        input='with-debug.elf'
    )

    def test_address_ranges_are_emitted(self):
        # As of commit 2373564, we do not use line info from debug information
        # to obtain address ranges. The following address ranges are thus not
        # obtained from debug information. Addresses ranges from debug
        # information are:
        #
        #     0x80484e0 - 0x80484f1
        #     0x8048500 - 0x8048511
        #     0x8048520 - 0x8048531
        #     0x8048540 - 0x8048551
        #     0x8048380 - 0x804839c
        #
        assert self.out_c.has_comment_matching(r'// Address range: 0x80484e0 - 0x80484f2')
        assert self.out_c.has_comment_matching(r'// Address range: 0x8048500 - 0x8048512')
        assert self.out_c.has_comment_matching(r'// Address range: 0x8048520 - 0x8048532')
        assert self.out_c.has_comment_matching(r'// Address range: 0x8048540 - 0x8048552')
        assert self.out_c.has_comment_matching(r'// Address range: 0x8048380 - 0x804839d')

    def test_funcs_are_emitted_in_order_by_address_ranges(self):
        self.assertEqual(self.out_c.func_names, ['func1', 'func2', 'func3', 'func4', 'main'])

class WithoutDebugInfo(Test):
    """Tests the emission of address ranges when debug info is not present (#1059)."""

    settings = TestSettings(
        input='without-debug.elf'
    )

    def test_address_ranges_are_emitted(self):
        assert self.out_c.has_comment_matching(r'// Address range: *0x8048380 - 0x804839d')
        assert self.out_c.has_comment_matching(r'// Address range: *0x80484e0 - 0x80484f2')
        assert self.out_c.has_comment_matching(r'// Address range: *0x8048500 - 0x8048512')
        assert self.out_c.has_comment_matching(r'// Address range: *0x8048520 - 0x8048532')
        assert self.out_c.has_comment_matching(r'// Address range: *0x8048540 - 0x8048552')

    def test_funcs_are_emitted_in_order_by_line_numbers_from_debug_info(self):
        self.assertEqual(self.out_c.func_names, ['main', 'func1', 'func2', 'func3', 'func4'])
