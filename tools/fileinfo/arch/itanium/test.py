from regression_tests import *

class TestIA64(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='srv_drvr.101'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['File format'], 'ELF')
        self.assertEqual(self.fileinfo.output['File class'], '32-bit')
        self.assertEqual(self.fileinfo.output['File type'], 'Executable file')
        self.assertEqual(self.fileinfo.output['Architecture'], 'IA-64 (Intel Itanium)')
        self.assertEqual(self.fileinfo.output['Endianness'], 'Big endian')
        self.assertEqual(self.fileinfo.output['Entry point address'], '0x31a80')
        self.assertEqual(self.fileinfo.output['Entry point offset'], '0x31a80')
        self.assertEqual(self.fileinfo.output['Entry point section name'], '.text')
        self.assertEqual(self.fileinfo.output['Entry point section index'], '20')
        self.assertEqual(self.fileinfo.output['Detected tool'], 'HP C++ (compiler), section table heuristic')
        self.assertEqual(self.fileinfo.output['Original language'], 'C++')
        self.assertEqual(self.fileinfo.output['Overlay offset'], '0x1c3534')
        self.assertEqual(self.fileinfo.output['Overlay size'], '0x1e')

# https://github.com/avast/retdec/issues/142
# While this is not a core file, it contains note sections that has slightly
# different behaviour that common ELF files so we will test it aswell
class TestELFNotes(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='srv_drvr.101',
        args='--json --verbose'
    )

    def test_correctly_analyzes_elf_notes(self):
        assert self.fileinfo.succeeded
        out = self.fileinfo.output
        self.assertEqual(out['elfNotes'][0]['name'], '.note.hpux_options')
        self.assertEqual(out['elfNotes'][0]['numberOfNotes'], 1)
        self.assertEqual(out['elfNotes'][0]['offset'], 0x11b4)
        self.assertEqual(out['elfNotes'][0]['size'], 60)
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['owner'], 'HP')
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][0]['dataOffset'],
            0x000011c4
        )
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['dataSize'], 44)
        self.assertEqual(out['elfNotes'][0]['noteEntries'][0]['type'], 7)
        self.assertEqual(
            out['elfNotes'][0]['noteEntries'][0]['description'],
            'NT_HP_UX_OPTIONS'
        )
        self.assertEqual(out['elfNotes'][1]['name'], '.note')
        self.assertEqual(out['elfNotes'][1]['numberOfNotes'], 75)
        self.assertEqual(out['elfNotes'][1]['offset'], 0x7d77c)
        self.assertEqual(out['elfNotes'][1]['size'], 34036)
        self.assertEqual(out['elfNotes'][1]['noteEntries'][74]['owner'], 'HP')
        self.assertEqual(
            out['elfNotes'][1]['noteEntries'][74]['dataOffset'],
            0x00085be8
        )
        self.assertEqual(out['elfNotes'][1]['noteEntries'][74]['dataSize'], 136)
        self.assertEqual(out['elfNotes'][1]['noteEntries'][74]['type'], 5)
        self.assertEqual(
            out['elfNotes'][1]['noteEntries'][74]['description'],
            'NT_HP_LINKER'
        )
