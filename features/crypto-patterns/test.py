from regression_tests import *

class Crc32Test(Test):
    """Ensures that crypto patterns detected by fileinfo are used while
    creating global variables.
    """

    settings = TestSettings(
        input='crc_32.x86.gcc.O2.exe',
    )

    def test_crc_32_global_variable_properties(self):
        crc = self.out_c.global_vars['CRC_32_IEEE_802_3_poly_0x04C11DB7_at_409060']
        self.assertTrue(crc.type.is_array())
        self.assertEqual(256, crc.type.element_count)
        self.assertTrue(crc.type.element_type.is_int(32))
        self.assertTrue(self.out_c.contains('{0, 0x77073096, -0x11f19ed4, .*, 0x5a05df1b, 0x2d02ef8d}'))

    def test_crypto_comments_for_globalvar_and_function(self):
        self.assertTrue(self.out_c.has_comment_matching('// Detected cryptographic pattern: CRC_32_IEEE_802_3_poly_0x04C11DB7 \(32-bit, little endian\)'))
        self.assertTrue(self.out_c.has_comment_matching('// Used cryptographic patterns:'))
        self.assertTrue(self.out_c.has_comment_matching('//  - CRC_32_IEEE_802_3_poly_0x04C11DB7 \(32-bit, little endian\)'))

class Crc32WithDebugTest(Test):
    """Ensures that crypto patterns detected by fileinfo are used only for
    comments when debug info is also present.
    """

    settings = TestSettings(
        input='crc_32.x86.gcc.O2.g.exe',
    )

    def test_crc_32_global_variable_properties(self):
        crc = self.out_c.global_vars['crc_32_tab'] # name from debug info, not crypto pattern match
        self.assertTrue(crc.type.is_array())
        self.assertEqual(256, crc.type.element_count)
        self.assertTrue(crc.type.element_type.is_int(32))
        self.assertTrue(self.out_c.contains('{0, 0x77073096, -0x11f19ed4, .*, 0x5a05df1b, 0x2d02ef8d}'))

    def test_crypto_comments_for_globalvar_and_function(self):
        self.assertTrue(self.out_c.has_comment_matching('// Detected cryptographic pattern: CRC_32_IEEE_802_3_poly_0x04C11DB7 \(32-bit, little endian\)'))
        self.assertTrue(self.out_c.has_comment_matching('// Used cryptographic patterns:'))
        self.assertTrue(self.out_c.has_comment_matching('//  - CRC_32_IEEE_802_3_poly_0x04C11DB7 \(32-bit, little endian\)'))
