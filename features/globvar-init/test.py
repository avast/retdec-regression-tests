from regression_tests import *

class Crc32Test(Test):
    """Ensures that global variables are initialized with constant values
    present in the binary at the address of global variable.
    """

    settings = TestSettings(
        input='crc_32.x86.gcc.O0.g.exe',
    )

    def test_original_func_names_are_used(self):
        self.assertEqual(self.out_c.func_names, ['crc32buf', 'main'])

    def test_global_variable_types_names_values(self):
        buf = self.out_c.global_vars['buf']
        self.assertTrue(buf.type.is_array())
        self.assertEqual(4, buf.type.element_count)
        self.assertTrue(buf.type.element_type.is_int(32))
        self.assertEqual(buf.initializer, [5, 2, 8, 4])

        crc = self.out_c.global_vars['crc_32_tab']
        self.assertTrue(crc.type.is_array())
        self.assertEqual(256, crc.type.element_count)
        self.assertTrue(crc.type.element_type.is_int(32))
        assert self.out_c.contains('{0, 0x77073096, -0x11f19ed4, .*, 0x5a05df1b, 0x2d02ef8d}')
