from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--verbose',
        input='mips-elf-8706f342137d7f21c3e4131ebd9d4989'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded

        self.assertEqual(self.fileinfo.output['File format'], 'ELF')
        self.assertEqual(self.fileinfo.output['File class'], '32-bit')
        self.assertEqual(self.fileinfo.output['File type'], 'Executable file')
        self.assertEqual(self.fileinfo.output['Architecture'], 'MIPS (MIPS I Architecture)')
        self.assertEqual(self.fileinfo.output['Endianness'], 'Little endian')

        assert self.fileinfo.output.contains(r'Size of one entry in table of segments : 0x20')
        assert self.fileinfo.output.contains(r'Size of table of segments              : 0x100')
        assert self.fileinfo.output.contains(r'Declared number of segments            : 8')
        assert self.fileinfo.output.contains(r'0     PHDR                rx        0x0034     0x0100     0x400034   0x400034   0x0100     0x00004')
        assert self.fileinfo.output.contains(r'1     INTERP              r         0x0134     0x000d     0x400134   0x400134   0x000d     0x00001')
        assert self.fileinfo.output.contains(r'2     Processor-specific  r         0x0164     0x0018     0x400164   0x400164   0x0018     0x00004')
        assert self.fileinfo.output.contains(r'3     LOADABLE            rx        0          0xa2d4     0x400000   0x400000   0xa2d4     0x10000')
        assert self.fileinfo.output.contains(r'4     LOADABLE            rw        0xa2d4     0x03d4     0x41a2d4   0x41a2d4   0xa494     0x10000')
        assert self.fileinfo.output.contains(r'5     DYNAMIC             rwx       0x017c     0x00e0     0x40017c   0x40017c   0x00e0     0x00004')
        assert self.fileinfo.output.contains(r'6     NOTE                r         0x0144     0x0020     0x400144   0x400144   0x0020     0x00004')
        assert self.fileinfo.output.contains(r'7     NULL                          0          0          0          0          0          0x00004')
