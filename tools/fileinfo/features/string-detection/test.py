from regression_tests import *

class StringTest(Test):
    def check_string(self, index, offset, string_type, section_name, content):
        string=self.fileinfo.output['strings']['strings'][index]
        self.assertEqual(string['fileOffset'], offset)
        self.assertEqual(string['type'], string_type)
        self.assertEqual(string['sectionName'], section_name)
        self.assertEqual(string['content'], content)

class Test1(StringTest):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --strings',
        input='dotnet_gui.ex'
    )

    def test_contains_certain_strings(self):
        self.assertEqual(self.fileinfo.output['strings']['numberOfStrings'], '103')
        self.check_string(67, '0x1852a', 'wide', '.rsrc', 'VS_VERSION_INFO')
        self.check_string(79, '0x186d0', 'wide', '.rsrc', 'dotnet_gui.exe')
        self.check_string(92, '0x18863', 'ascii', '.rsrc', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        self.check_string(98, '0x189b9', 'ascii', '.rsrc', '        <requestedExecutionLevel level="asInvoker" uiAccess="false"/>')

class Test2(StringTest):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --strings',
        input='pi-O2-g0.ex'
    )

    def test_contains_certain_strings(self):
        self.assertEqual(self.fileinfo.output['strings']['numberOfStrings'], '86')
        self.check_string(0, '0x3c58', 'ascii', 'DATA', 'Error')
        self.check_string(1, '0x3c60', 'ascii', 'DATA', 'Runtime error     at 00000000')
        self.check_string(49, '0x422e', 'ascii', '.idata', 'GetModuleHandleA')
        self.check_string(82, '0x4a98', 'wide', '.rsrc', 'PACKAGEINFO')

class Test3(StringTest):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --strings',
        input='rubic_d-O2-g0.ex'
    )

    def test_contains_certain_strings(self):
        self.assertEqual(self.fileinfo.output['strings']['numberOfStrings'], '162')
        self.check_string(0, '0x3c50', 'ascii', 'DATA', 'Error')
        self.check_string(1, '0x3c58', 'ascii', 'DATA', 'Runtime error     at 00000000')
        self.check_string(41, '0x46cc', 'ascii', '.idata', 'GetModuleHandleA')
        self.check_string(153, '0x5498', 'wide', '.rsrc', 'PACKAGEINFO')

class Test4(StringTest):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --strings',
        input='x86-macho-0cdc7e671dc5a3816d6768ca84821bcb'
    )

    def test_contains_certain_strings(self):
        self.assertEqual(self.fileinfo.output['strings']['numberOfStrings'], '62')
        self.check_string(14, '0x5aed', 'ascii', '__cstring', 'Cannot open script file \'%s\'')
        self.check_string(33, '0x5bdc', 'ascii', '__cstring', 'ob/wW/dD/qQ  byte (oct,hex), word, dword, qword (lil, big endian)')
        self.check_string(61, '0x5fa8', 'ascii', '__cstring', '[0x%08llx]> ')

class Test5(StringTest):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --strings',
        input='main'
    )

    def test_contains_certain_strings(self):
        self.assertEqual(self.fileinfo.output['strings']['numberOfStrings'], '72')
        self.check_string(0, '0x238', 'ascii', '.interp', '/lib64/ld-linux-x86-64.so.2')
        self.check_string(7, '0x670', 'ascii', '.rodata', 'This is just example program')
        self.check_string(40, '0x18fa', 'ascii', '.strtab', 'main')
        self.check_string(44, '0x193a', 'ascii', '.shstrtab', '.symtab')

class Test6(StringTest):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --strings',
        input='main-g'
    )

    def test_contains_certain_strings(self):
        self.assertEqual(self.fileinfo.output['strings']['numberOfStrings'], '142')
        self.check_string(0, '0x238', 'ascii', '.interp', '/lib64/ld-linux-x86-64.so.2')
        self.check_string(7, '0x670', 'ascii', '.rodata', 'This is just example program')
        self.check_string(11, '0x14ff', 'ascii', '.debug_line', '/usr/lib/gcc/x86_64-redhat-linux/6.3.1/include')
        self.check_string(25, '0x15e8', 'ascii', '.debug_str', 'GNU C11 6.3.1 20161221 (Red Hat 6.3.1-1) -mtune=generic -march=x86-64 -g -std=c11')
        self.check_string(105, '0x212a', 'ascii', '.strtab', 'main')
        self.check_string(109, '0x216a', 'ascii', '.shstrtab', '.symtab')
