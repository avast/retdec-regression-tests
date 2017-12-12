from regression_tests import *

class Test1893MipsRelocations(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=['ioftell-le.o', 'ioftell-be.o']
    )

    def test_fileinfo_does_correctly_interpet_mips64_relocs(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['numberOfRelocations'], '14');
        self.assertEqual(
            self.fileinfo.output['relocationTables'][0]['relocations'][0]['symbolName'],
            '_IO_ftell'
        );
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['type'], '7');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['offset'], '0xc');
        self.assertEqual(
            self.fileinfo.output['relocationTables'][0]['relocations'][1]['symbolName'],
            '_IO_ftell'
        );
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['type'], '24');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['offset'], '0xc');
        self.assertEqual(
            self.fileinfo.output['relocationTables'][0]['relocations'][2]['symbolName'],
            '_IO_ftell'
        );
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['type'], '5');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['offset'], '0xc');
        self.assertEqual(
            self.fileinfo.output['relocationTables'][0]['relocations'][3]['symbolName'],
            '_IO_ftell'
        );
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][3]['type'], '7');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][3]['offset'], '0x24');
        self.assertEqual(
            self.fileinfo.output['relocationTables'][0]['relocations'][4]['symbolName'],
            '_IO_ftell'
        );
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][4]['type'], '24');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][4]['offset'], '0x24');
        self.assertEqual(
            self.fileinfo.output['relocationTables'][0]['relocations'][5]['symbolName'],
            '_IO_ftell'
        );
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][5]['type'], '6');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][5]['offset'], '0x24');

class Test1897DynsymBug(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='dynsym'
    )

    def test_fileinfo_does_correctly_interpet_mips64_relocs(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['type'], '3');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][0]['offset'], '0x10ff0');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['type'], '18');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][1]['offset'], '0x10ff0');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['type'], '3');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][2]['offset'], '0x11000');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][3]['type'], '18');
        self.assertEqual(self.fileinfo.output['relocationTables'][0]['relocations'][3]['offset'], '0x11000');
