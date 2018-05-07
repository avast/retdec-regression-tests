from regression_tests import *


# https://github.com/avast-tl/retdec/issues/142
# https://github.com/avast-tl/retdec/issues/244
class TestELFNotesExe(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='89a53f828765f29bc8689267da6c1d5f358f5ef8c0d75388ddadd7b2e068a421',
        args='--json --verbose'
    )

    def test_correctly_analyzes_elf_notes(self):
        assert self.fileinfo.succeeded
        out = self.fileinfo.output
        self.assertEqual(out['elfNotes'][0]['name'], '.note.tag')
        self.assertEqual(out['elfNotes'][0]['numberOfNotes'], 2)
        self.assertEqual(out['elfNotes'][0]['offset'], 0x218)
        self.assertEqual(out['elfNotes'][0]['size'], 48)
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][0]['owner'],
            'FreeBSD'
        )
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][0]['dataOffset'],
            0x0000022c
        )
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['dataSize'], 4)
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['type'], 1)
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][0]['description'],
            'NT_FREEBSD_ABI_TAG'
        )
        # Second entry
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][1]['owner'],
            'FreeBSD'
        )
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][1]['dataOffset'],
            0x00000244
        )
        self.assertEqual(out['elfNotes'][0]['noteEntries'][1]['dataSize'], 4)
        self.assertEqual(out['elfNotes'][0]['noteEntries'][1]['type'], 2)
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][1]['description'],
            'NT_FREEBSD_NOINIT_TAG'
        )

    def test_correctly_analyzes_freebsd_osabi_notes(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['osOrAbi'], 'FreeBSD')
        self.assertEqual(self.fileinfo.output['osOrAbiVersion'], '11.1.506')


# https://github.com/avast-tl/retdec/issues/244
class TestELFNotesGnu(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='d446ac335663141b888807cfef5a9a73f0c2297f2fc807127bfe6e23af286021',
        args='--json --verbose'
    )

    def test_correctly_analyzes_osabi_notes(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['osOrAbi'], 'Linux')
        self.assertEqual(self.fileinfo.output['osOrAbiVersion'], '2.6.32')


# https://github.com/avast-tl/retdec/issues/244
class TestELFNotesAndroid(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='3505f8faec50203f0b177d008e645b3bec88b79c89a9ef2185e2b9c82055976e',
        args='--json --verbose'
    )

    def test_correctly_analyzes_osabi_notes(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['osOrAbi'], 'Android')
        self.assertEqual(self.fileinfo.output['osOrAbiVersion'], '19')


# https://github.com/avast-tl/retdec/issues/142
class TestELFNotesCore(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='63ba46429deccb915362680868c44a396bfc55106664371517e3ba97baa57952',
        args='--json --verbose'
    )

    def test_correctly_analyzes_elf_notes(self):
        assert self.fileinfo.succeeded
        out = self.fileinfo.output
        self.assertEqual(out['elfNotes'][0]['numberOfNotes'], 8)
        self.assertEqual(out['elfNotes'][0]['offset'], 0xd4)
        self.assertEqual(out['elfNotes'][0]['size'], 2312)
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['owner'], 'CORE')
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][0]['dataOffset'],
            0x000000e8
        )
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['dataSize'], 144)
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['type'], 1)
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][0]['description'],
            'NT_PRSTATUS'
        )
        # Second entry
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][7]['owner'],
            'LINUX'
        )
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][7]['dataOffset'],
            0x0000069c
        )
        self.assertEqual(out['elfNotes'][0]['noteEntries'][7]['dataSize'], 832)
        self.assertEqual(out['elfNotes'][0]['noteEntries'][7]['type'], 0x202)
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][7]['description'],
            'NT_X86_XSTATE'
        )

    def test_correctly_analyzes_elf_core_structs(self):
        assert self.fileinfo.succeeded
        out = self.fileinfo.output
        self.assertEqual(out['elfCore']['numberOfAuxVectorEntries'], 20)
        self.assertEqual(out['elfCore']['auxVector'][0]['name'], 'AT_SYSINFO')
        self.assertEqual(out['elfCore']['auxVector'][0]['value'], 4151790800)
        self.assertEqual(out['elfCore']['auxVector'][19]['name'], 'AT_NULL')
        self.assertEqual(out['elfCore']['auxVector'][19]['value'], 0)
        # File map
        self.assertEqual(out['elfCore']['numberOfFileMapEntries'], 1)
        self.assertEqual(out['elfCore']['fileMap'][0]['address'], 134512640)
        self.assertEqual(out['elfCore']['fileMap'][0]['page'], 0)
        self.assertEqual(out['elfCore']['fileMap'][0]['size'], 4096)
        self.assertEqual(
            out['elfCore']['fileMap'][0]['path'],
            "/usr/local/google/home/labath/ll/lldb/packages/Python/lldbsuite/"
            "test/functionalities/unwind/noreturn/module-end/test.out"
        )
