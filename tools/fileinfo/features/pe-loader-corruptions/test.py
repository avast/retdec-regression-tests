from regression_tests import *

class Test000(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '000-correct-file-32bit.ex_',
            '000-correct-file-64bit.ex_',
            '000-correct-file-coff-debug-info-32bit.ex_',
            '000-correct-file-small-alignment-32bit.ex_',
            '000-correct-file-size-of-opt-header-zero-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        assert 'loaderError' not in self.fileinfo.output, 'unexpectedly found loader error'


class Test002(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '002-pe-header-offset-unaligned-32bit.ex_',
            '002-pe-header-offset-unaligned-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 2)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_E_LFANEW_UNALIGNED')


class Test008(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '008-missing-executable-bit-32bit.ex_',
            '008-missing-executable-bit-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 8)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_IMAGE_NON_EXECUTABLE')


class Test009(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '009-missing-optional-header-magic-32bit.ex_',
            '009-missing-optional-header-magic-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 9)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_NO_OPTHDR_MAGIC')


class Test010(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '010-size-of-headers-zero-32bit.ex_',
            '010-size-of-headers-zero-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 10)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SIZE_OF_HEADERS_ZERO')

class Test011(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '011-file-alignment-zero-32bit.ex_',
            '011-file-alignment-zero-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 11)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_FILE_ALIGNMENT_ZERO')


class Test012(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '012-file-alignment-not-power-of-two-32bit.ex_',
            '012-file-alignment-not-power-of-two-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 12)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_FILE_ALIGNMENT_NOT_POW2')


class Test013(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '013-section-alignment-zero-32bit.ex_',
            '013-section-alignment-zero-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 13)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SECTION_ALIGNMENT_ZERO')


class Test014(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '014-section-alignment-not-power-of-two-32bit.ex_',
            '014-section-alignment-not-power-of-two-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 14)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SECTION_ALIGNMENT_NOT_POW2')


class Test015(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '015-section-alignment-smaller-than-file-alignment-32bit.ex_',
            '015-section-alignment-smaller-than-file-alignment-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 15)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SECTION_ALIGNMENT_TOO_SMALL')


class Test016(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '016-section-alignment-not-equal-to-file-alignment-32bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 16)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SECTION_ALIGNMENT_INVALID')


class Test017(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '017-size-of-image-too-big-32bit.ex_',
            '017-size-of-image-too-big-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 17)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SIZE_OF_IMAGE_TOO_BIG')


class Test018(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '018-invalid-machine-32bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 18)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_INVALID_MACHINE32')


class Test019(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '019-invalid-machine-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 19)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_INVALID_MACHINE64')

class Test020(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '020-size-of-headers-greater-than-size-of-image-32bit.ex_',
            '020-size-of-headers-greater-than-size-of-image-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 20)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SIZE_OF_HEADERS_INVALID')


class Test021(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '021-size-of-optional-header-not-aligned-32bit.ex_',
            '021-size-of-optional-header-not-aligned-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 21)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SIZE_OF_OPTHDR_NOT_ALIGNED')


class Test023(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '023-image-base-not-aligned-32bit.ex_',
            '023-image-base-not-aligned-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 23)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_IMAGE_BASE_NOT_ALIGNED')


class Test025(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '025-raw-data-overflow-32bit.ex_',
            '025-raw-data-overflow-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 25)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_RAW_DATA_OVERFLOW')


class Test028(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '028-section-size-mismatch-32bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 28)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_SECTION_SIZE_MISMATCH')

class Test029(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '029-invalid-section-va-32bit.ex_',
            '029-invalid-section-va-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 29)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_INVALID_SECTION_VA')


class Test030(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '030-invalid-section-vsize-32bit.ex_',
            '030-invalid-section-vsize-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 30)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_INVALID_SECTION_VSIZE')


class Test032(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '032-invalid-size-of-image-32bit.ex_',
            '032-invalid-size-of-image-64bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 32)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_INVALID_SIZE_OF_IMAGE')


class Test033(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '033-file-is-cut-32bit.ex_',
            '033-file-is-cut-32bit.ex_',
            '033-file-is-cut-small-alignment-32bit.ex_',
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 33)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_FILE_IS_CUT')

class Test034(Test):
    settings=TestSettings(
        tool='fileinfo',
        input=[
            '034-file-is-cut-but-loadable-32bit.ex_',
            '034-file-is-cut-but-loadable-64bit.ex_'
        ],
        args='--json --verbose'
    )

    def test_corrupted_pe(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["loaderError"]["code"], 34)
        self.assertEqual(self.fileinfo.output["loaderError"]["code_text"], 'LDR_ERROR_FILE_IS_CUT_LOADABLE')
