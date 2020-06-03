from regression_tests import *
import json

class TestArchiveIdentification(Test):
    settings = TestSettings(
        input=[
            'free_bsd.a',
            'gnu.a'
        ]
    )

    def setUp(self):
        # Fail expected.
        pass

    def test_check_archive_identification(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert 'fact_x86.o' in self.decompiler.output
        assert 'lib.o' in self.decompiler.output

class TestArchiveEmptyInputArchive(Test):
    settings = TestSettings(
        input='empty.a',
    )

    def setUp(self):
        # Fail expected.
        pass

    def test_check_archive_identification(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'This file is an archive!')
        assert self.decompiler.log.contains(r'Error: The input archive is empty.')

class TestArchiveWithEmptyFile(Test):
    settings = TestSettings(
        input='with_empty_file.a',
        ar_index=0
    )

    def setUp(self):
        # Fail expected.
        pass

    def test_is_archive_but_the_format_of_file_inside_it_is_unsupported(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        # The archive contains an empty file, so the archive is valid and its
        # extraction should succeed. However, fileinfo should fail because the
        # format is not supported.
        assert self.decompiler.log.contains(r'Error: Failed to load input file')

class TestArchiveInvalidInputArchive(Test):
    settings = TestSettings(
        input='invalid.a',
    )

    def setUp(self):
        # Fail expected.
        pass

    def test_check_archive_identification(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'This file is an archive!')
        assert self.decompiler.log.contains(
            r'Error: The input archive has invalid format.'
        )

class TestArchiveDecompilationFreeBSD(Test):
    settings = TestSettings(
        input='free_bsd.a',
        args=[
            '--ar-name=lib.o',
            '--ar-index=0'
        ]
    )

    def test_check_decompilation(self):
        assert self.out_c.has_func('ack')
        assert self.out_c.has_func('factorial')

class TestArchiveDecompilationGNU(Test):
    settings = TestSettings(
        input='gnu.a',
        args=[
            '--ar-name=fact_x86.o',
            '--ar-index=0'
        ]
    )

    def test_check_decompilation(self):
        assert self.out_c.has_func('__Z9factoriali')

class TestArchiveDecompilationMSVC(Test):
    settings = TestSettings(
        input='msvc.lib',
        args=[
            '--ar-name=Debug\\Factorial.obj',
            '--ar-index=0'
        ]
    )

    def test_check_decompilation(self):
        assert self.out_c.has_func('_factorial')

class TestArchiveInvalidIndex_1(Test):
    settings = TestSettings(
        input='free_bsd.a',
        ar_index=[
            '2'
        ]
    )

    def setUp(self):
        # Fail expected.
        pass

    def test_check_failure(self):
        self.assertTrue(self.decompiler.failed)
        assert not self.decompiler.log.contains(r'integer expression expected')
        assert self.decompiler.log.contains(
            r'Error: File on index \'.*\' was not found in the input archive. '
            'Valid indexes are 0-1.'
        )

class TestArchiveInvalidIndex_2(Test):
    settings = TestSettings(
        input='free_bsd.a',
        ar_index=[
            '1111111111111111111111111111111111111',
            'notanumber',
        ]
    )

    def setUp(self):
        # Fail expected.
        pass

    def test_check_failure(self):
        self.assertTrue(self.decompiler.failed)
        assert not self.decompiler.log.contains(r'integer expression expected')
        assert self.decompiler.log.contains(
            r'\[--ar-index\] invalid index:'
        )

class TestArchiveInvalidIndexOneFile(Test):
    settings = TestSettings(
        input='leading_ws.a',
        args='--ar-index=1'
    )

    def setUp(self):
        # Expecting failure.
        pass

    def test_check_failure(self):
        self.assertTrue(self.decompiler.failed)
        assert not self.decompiler.log.contains(r'integer expression expected')
        assert self.decompiler.log.contains(
            r'Error: File on index \'.*\' was not found in the input archive. '
            'Valid indexes are 0-0.'
        )

class TestArchiveInvalidName(Test):
    settings = TestSettings(
        input='free_bsd.a',
        ar_name='notavalidname'
    )

    def setUp(self):
        # Expecting failure.
        pass

    def test_check_failure(self):
        self.assertTrue(self.decompiler.failed)
        assert self.decompiler.log.contains(
            r'Error: File named \'notavalidname\' was '
            'not found in the input archive.'
        )

class TestDecompileArchiveList(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='gnu.a',
        args='--json'
    )

    def test_check_list(self):
        assert self.retdec_archive_decompiler_py.succeeded
        as_json = json.loads(self.retdec_archive_decompiler_py.output)
        self.assertEqual(as_json['objects'][0]['name'], 'fact_x86.o')
        self.assertEqual(as_json['objects'][0]['index'], 0)
        self.assertEqual(as_json['objects'][1]['name'], 'lib.o')
        self.assertEqual(as_json['objects'][1]['index'], 1)

class TestDecompileArchiveListPlainText(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='gnu.a',
        args='--plain'
    )

    def test_check_list(self):
        assert self.retdec_archive_decompiler_py.succeeded
        assert '0\tfact_x86.o' in self.retdec_archive_decompiler_py.output
        assert '1\tlib.o' in self.retdec_archive_decompiler_py.output

class TestDecompileArchiveNoInput(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        args='--plain'
    )

    def test_check_list(self):
        assert 'error: the following arguments are required: FILE' in self.retdec_archive_decompiler_py.output

class TestDecompileArchiveNoInputJson(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        args='--json'
    )

    def test_check_list(self):
        assert 'error: the following arguments are required: FILE' in self.retdec_archive_decompiler_py.output

class TestDecompileArchiveExclusiveArgs(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        args='--plain --json',
        input='quotes .a',
    )

    def test_check_list(self):
        assert self.retdec_archive_decompiler_py.failed
        assert self.retdec_archive_decompiler_py.log.contains(
            'Arguments --plain and --json are mutually exclusive.'
        )

class TestDecompileArchiveListQuotesEscaped(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='quotes .a',
        args='--json'
    )

    def test_check_list(self):
        assert self.retdec_archive_decompiler_py.succeeded
        as_json = json.loads(self.retdec_archive_decompiler_py.output)
        self.assertEqual(as_json['objects'][0]['name'], 'myobject_.o')
        self.assertEqual(as_json['objects'][0]['index'], 0)

class TestDecompileArchiveListNamesEscaped(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='msvc.lib',
        args='--json'
    )

    def test_check_list(self):
        assert self.retdec_archive_decompiler_py.succeeded
        as_json = json.loads(self.retdec_archive_decompiler_py.output)
        self.assertEqual(as_json['objects'][0]['name'], 'Debug\\Factorial.obj')
        self.assertEqual(as_json['objects'][1]['name'], 'Debug\\Ack.obj')

class TestDecompileArchiveListLeadingWSJson(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='leading_ws.a',
        args='--json'
    )

    def test_check_list(self):
        as_json = json.loads(self.retdec_archive_decompiler_py.output)
        self.assertEqual(as_json['objects'][0]['name'], ' file.o')

class TestDecompileArchiveListLeadingWSPlainText(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='leading_ws.a',
        args='--plain'
    )

    def test_check_list(self):
        assert '0\t file.o' in self.retdec_archive_decompiler_py.output

#class TestArchiveDecompilationLeadingWSIndex(Test):
#    settings = TestSettings(
#        input='leading_ws.a',
#        args=r'--ar-index=0'
#    )
#
#    def test_check_decompilation(self):
#        assert self.out_c.has_func('main')
#        assert self.out_c.funcs['main'].calls('puts')

#class TestArchiveDecompilationLeadingWSName(Test):
#    settings = TestSettings(
#        input='leading_ws.a',
#        ar_name=' file.o'
#    )
#
#    def test_check_decompilation(self):
#        assert self.out_c.has_func('main')
#        assert self.out_c.funcs['main'].calls('puts')

#class TestArchiveDecompilationEscapedNewline(Test):
#    settings = TestSettings(
#        input='newline.a',
#        ar_name='fi_le.o'
#    )
#
#    def test_check_decompilation(self):
#        assert self.out_c.has_func('main')
#        assert self.out_c.funcs['main'].calls('puts')

class TestDecompileArchiveListLeadingWSPlainText(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='newline.a',
        args='--plain'
    )

    def test_check_list(self):
        assert '0\tfi_le.o' in self.retdec_archive_decompiler_py.output

class TestArchiveThinInputArchive(Test):
    settings = TestSettings(
        input='thin.a',
    )

    def setUp(self):
        # Fail expected. Thin archives cannot be used as decompilation target.
        pass

    def test_check_thin_archive_identification(self):
        self.assertNotEqual(self.decompiler.return_code, 0)
        assert self.decompiler.log.contains(r'This file is an archive!')
        assert self.decompiler.log.contains(
            r'Error: File is a thin archive and cannot be decompiled.'
        )

class TestDecompileArchiveThinInputArchive(Test):
    settings = TestSettings(
        tool='retdec-archive-decompiler.py',
        input='thin.a',
    )

    def test_check_thin_archive_identification(self):
        assert self.retdec_archive_decompiler_py.failed
        assert self.retdec_archive_decompiler_py.log.contains(
            r'Error: File is a thin archive and cannot be decompiled.'
        )

class TestArchiveDecompilationMultipleSameNamesFirst(Test):
    settings = TestSettings(
        input='multiple.a',
        args='--ar-index=0'
    )

    def test_check_decompilation(self):
        assert self.out_c.has_func('factorial')
        assert self.out_c.funcs['factorial'].calls('factorial')

class TestArchiveDecompilationMultipleSameNamesSecond(Test):
    settings = TestSettings(
        input='multiple.a',
        args='--ar-index=1'
    )

    def test_check_decompilation(self):
        assert self.out_c.has_func('ack')
        assert self.out_c.funcs['ack'].calls('ack')
