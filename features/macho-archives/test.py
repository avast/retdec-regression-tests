from regression_tests import *
import json


class TestExtractMachOIsArchiveJson(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='archive',
        args='--check-archive'
    )

    def test_check_control_json(self):
        assert 'is a static library.' in self.retdec_macho_extractor.output


class TestExtractMachONotArchiveJson(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='non-archive',
        args='--check-archive'
    )

    def test_check_control_json(self):
        assert 'NOT a static library.' in self.retdec_macho_extractor.output


class TestExtractMachONotArchiveObjectsJson(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='non-archive',
        args='--objects'
    )

    def test_check_control_json(self):
        assert 'is not an archive!' in self.retdec_macho_extractor.output


class TestExtractMachOJson(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='non-archive',
        args='--json'
    )

    def test_check_extract_json(self):
        as_json = json.loads(self.retdec_macho_extractor.output)
        self.assertEqual(as_json['architectures'][0]['name'], 'i386')
        self.assertEqual(as_json['architectures'][0]['index'], 0)
        self.assertEqual(as_json['architectures'][0]['cpuFamily'], 'x86')
        self.assertEqual(as_json['architectures'][1]['name'], 'powerpc')
        self.assertEqual(as_json['architectures'][1]['index'], 1)
        self.assertEqual(as_json['architectures'][1]['cpuFamily'], 'powerpc')


class TestExtractArchiveJson(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='archive',
        args='--json'
    )

    def test_check_extract_json(self):
        as_json = json.loads(self.retdec_macho_extractor.output)
        self.assertEqual(as_json['architectures'][0]['name'], 'armv7')
        self.assertEqual(as_json['architectures'][0]['index'], 0)
        self.assertEqual(as_json['architectures'][0]['cpuFamily'], 'arm')
        self.assertEqual(as_json['architectures'][1]['name'], 'arm64')
        self.assertEqual(as_json['architectures'][1]['index'], 1)
        self.assertEqual(as_json['architectures'][1]['cpuFamily'], 'arm64')


class TestExtractArchiveJsonWithOjects(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='archive',
        args='--json --objects'
    )

    def test_check_extract_json(self):
        as_json = json.loads(self.retdec_macho_extractor.output)
        self.assertEqual(as_json['architectures'][0]['name'], 'armv7')
        self.assertEqual(as_json['architectures'][0]['index'], 0)
        self.assertEqual(as_json['architectures'][0]['cpuFamily'], 'arm')
        self.assertEqual(
            as_json['architectures'][0]['objects'][0]['name'],
            'TatvikMpeg2DemuxBitStreamReader.o'
        )
        self.assertEqual(
            as_json['architectures'][0]['objects'][1]['name'],
            'TatvikMpeg2DemuxPESDecoder.o'
        )
        self.assertEqual(
            as_json['architectures'][0]['objects'][2]['name'],
            'TatvikMpeg2TSDemuxer.o'
        )
        self.assertEqual(
            as_json['architectures'][0]['objects'][3]['name'],
            'TatvikTransportStreamParser.o'
        )
        self.assertEqual(as_json['architectures'][1]['name'], 'arm64')
        self.assertEqual(as_json['architectures'][1]['index'], 1)
        self.assertEqual(as_json['architectures'][1]['cpuFamily'], 'arm64')
        self.assertEqual(
            as_json['architectures'][1]['objects'][0]['name'],
            'TatvikMpeg2DemuxBitStreamReader.o'
        )
        self.assertEqual(
            as_json['architectures'][1]['objects'][1]['name'],
            'TatvikMpeg2DemuxPESDecoder.o'
        )
        self.assertEqual(
            as_json['architectures'][1]['objects'][2]['name'],
            'TatvikMpeg2TSDemuxer.o'
        )
        self.assertEqual(
            as_json['architectures'][1]['objects'][3]['name'],
            'TatvikTransportStreamParser.o'
        )


class TestExtractArchiveWithOjects(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='archive',
        args='--objects'
    )

    def test_check_extract_json(self):
        self.assertIn('0\tarmv7\tarm', self.retdec_macho_extractor.output)
        self.assertIn('1\tarm64\tarm64', self.retdec_macho_extractor.output)
        self.assertIn(
            '0\tTatvikMpeg2DemuxBitStreamReader.o',
            self.retdec_macho_extractor.output
        )
        self.assertIn(
            '1\tTatvikMpeg2DemuxPESDecoder.o',
            self.retdec_macho_extractor.output
        )
        self.assertIn(
            '2\tTatvikMpeg2TSDemuxer.o',
            self.retdec_macho_extractor.output
        )
        self.assertIn(
            '3\tTatvikTransportStreamParser.o',
            self.retdec_macho_extractor.output
        )


class TestExtractArchivePlain(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        input='archive',
        args='--list'
    )

    def test_check_extract_plain(self):
        self.assertIn('0\tarmv7\tarm', self.retdec_macho_extractor.output)
        self.assertIn('1\tarm64\tarm64', self.retdec_macho_extractor.output)


class TestExtractPrintErrorInJson(Test):
    settings = TestSettings(
        tool='retdec-macho-extractor',
        args='--json'
    )

    def setUp(self):
        pass

    def test_check_detection_list(self):
        self.assertNotEqual(self.retdec_macho_extractor.return_code, 0)
        as_json = json.loads(self.retdec_macho_extractor.output)
        self.assertEqual(as_json['error'], 'no input file')


class TestExtractArchiveDecompilationPick(Test):
    settings = TestSettings(
        input='archive',
        args=[ '--cleanup', '--cleanup --arch arm' ]
    )

    def setUp(self):
        pass

    def test_check_objet_list(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        self.assertIn(
            '0\tTatvikMpeg2DemuxBitStreamReader.o',
            self.decompiler.output
        )
        self.assertIn(
            '1\tTatvikMpeg2DemuxPESDecoder.o',
            self.decompiler.output
        )
        self.assertIn(
            '2\tTatvikMpeg2TSDemuxer.o',
            self.decompiler.output
        )
        self.assertIn(
            '3\tTatvikTransportStreamParser.o',
            self.decompiler.output
        )


class TestExtractArchiveDecompilationListArchs(Test):
    settings = TestSettings(
        input='archive',
        args='--cleanup --arch x86'
    )

    def setUp(self):
        pass

    def test_check_arch_list(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        self.assertIn(
            'Invalid --arch option \'x86\'. File contains these architecture families:',
            self.decompiler.output
        )
        self.assertIn('armv7\tarm', self.decompiler.output)
        self.assertIn('arm64\tarm64', self.decompiler.output)


class TestExtractArchiveDecompilation(Test):
    settings = TestSettings(
        input='archive',
        args=[ '--ar-index 3', '--ar-index 3 --arch arm' ]
    )

    def test_check_decompilation(self):
        assert self.out_c.has_func( '_GetPositionCall' )
        assert self.out_c.has_func( '_MovePositionCall' )


class TestExtractDecompileArchiveJson(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.sh',
        input='archive',
        args='--list --json'
    )

    def test_check_list(self):
        as_json = json.loads(self.retdec_archive_decompiler_sh.output)
        self.assertEqual(as_json['architectures'][0]['name'], 'armv7')
        self.assertEqual(as_json['architectures'][0]['index'], 0)
        self.assertEqual(as_json['architectures'][0]['cpuFamily'], 'arm')
        self.assertEqual(
            as_json['architectures'][0]['objects'][0]['name'],
            'TatvikMpeg2DemuxBitStreamReader.o'
        )
        self.assertEqual(
            as_json['architectures'][0]['objects'][1]['name'],
            'TatvikMpeg2DemuxPESDecoder.o'
        )
        self.assertEqual(
            as_json['architectures'][0]['objects'][2]['name'],
            'TatvikMpeg2TSDemuxer.o'
        )
        self.assertEqual(
            as_json['architectures'][0]['objects'][3]['name'],
            'TatvikTransportStreamParser.o'
        )
        self.assertEqual(as_json['architectures'][1]['name'], 'arm64')
        self.assertEqual(as_json['architectures'][1]['index'], 1)
        self.assertEqual(as_json['architectures'][1]['cpuFamily'], 'arm64')
        self.assertEqual(
            as_json['architectures'][1]['objects'][0]['name'],
            'TatvikMpeg2DemuxBitStreamReader.o'
        )
        self.assertEqual(
            as_json['architectures'][1]['objects'][1]['name'],
            'TatvikMpeg2DemuxPESDecoder.o'
        )
        self.assertEqual(
            as_json['architectures'][1]['objects'][2]['name'],
            'TatvikMpeg2TSDemuxer.o'
        )
        self.assertEqual(
            as_json['architectures'][1]['objects'][3]['name'],
            'TatvikTransportStreamParser.o'
        )


class TestExtractDecompileArchivePlainText(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.sh',
        input='archive',
        args='--list'
    )

    def test_check_list(self):
        self.assertIn(
            '0\tarmv7\tarm',
            self.retdec_archive_decompiler_sh.output
        )
        self.assertIn(
            '1\tarm64\tarm64',
            self.retdec_archive_decompiler_sh.output
        )
        self.assertIn(
            '0\tTatvikMpeg2DemuxBitStreamReader.o',
            self.retdec_archive_decompiler_sh.output
        )
        self.assertIn(
            '1\tTatvikMpeg2DemuxPESDecoder.o',
            self.retdec_archive_decompiler_sh.output
        )
        self.assertIn(
            '2\tTatvikMpeg2TSDemuxer.o',
            self.retdec_archive_decompiler_sh.output
        )
        self.assertIn(
            '3\tTatvikTransportStreamParser.o',
            self.retdec_archive_decompiler_sh.output
        )
