from regression_tests import *

# https://github.com/avast/retdec/issues/415
# Test for proper anomaly scanning
class Test1(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='c4affaea94863009d90668c9d86291864cd6027d798a20085b5110f6473450b7',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'EpInWritableSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'PackerSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Packer section name: UPX0')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['identifier'], 'UninitSectionHasData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Section UPX0 is marked uninitialized but contains data')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['identifier'], 'PackerSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Packer section name: UPX1')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['identifier'], 'UnusualSectionFlags')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['description'], 'Section .rsrc has unusual characteristics')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['description'], 'Unusual section name: .imports')

class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='CRACKME3.EX',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'EpInLastSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in the last section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'EpInWritableSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Unusual section name: YADO')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['identifier'], 'DuplicitSectionNames')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Multiple sections with name YADO')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['description'], 'Unusual section name: krypton')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['description'], 'Unusual section name: _!_!_!_')

class Test3(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='fact_rec.ex',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'EpInLastSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in the last section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'EpInWritableSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['identifier'], 'UnusualSectionFlags')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Section .text has unusual characteristics')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['identifier'], 'UnusualSectionFlags')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Section .rdata has unusual characteristics')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['description'], 'Unusual section name: /4')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['identifier'], 'UnusualSectionFlags')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['description'], 'Section .bss has unusual characteristics')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['description'], 'Unusual section name: /14')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][7]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][7]['description'], 'Unusual section name: /29')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][8]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][8]['description'], 'Unusual section name: /45')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][9]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][9]['description'], 'Unusual section name: /61')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][10]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][10]['description'], 'Unusual section name: /73')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][11]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][11]['description'], 'Unusual section name: /87')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][12]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][12]['description'], 'Unusual section name: /99')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][13]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][13]['description'], 'Unusual section name: /112')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][14]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][14]['description'], 'Unusual section name: /123')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][15]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][15]['description'], 'Unusual section name: /134')


class Test4(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='tiny_no_sections',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'EpOutsideSections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point is outside of mapped sections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'SizeOfHeaderNotAligned')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'SizeOfHeader is not aligned to multiple of FileAlignment')

class Test5(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='PTTAdresForm.ex',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Unusual section name: CODE\\x11')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Unusual section name: D\\x11TA')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['identifier'], 'UnusualSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Unusual section name: BSS\\x11')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['identifier'], 'OverlappingSections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Sections .idata and .tls overlap')

class Test6(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='tiny_no_sections',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'EpOutsideSections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point is outside of mapped sections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'SizeOfHeaderNotAligned')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'SizeOfHeader is not aligned to multiple of FileAlignment')

class Test7(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='5c6dd5fc0fef8736f8fd1bebab8f1c3e',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'EpInWritableSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'UnusualSectionFlags')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Section .text has unusual characteristics')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['identifier'], 'LargeResource')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Resource 103 has size over 100MB')

class Test8(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='custom_malformed',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'LargeSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Section .text has size over 100MB')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'OverlappingSections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Sections .text and .rsrc overlap')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['identifier'], 'LargeSection')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Section .rsrc has size over 100MB')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['identifier'], 'LargeResource')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Resource 101 has size over 100MB')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['identifier'], 'StretchedResource')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['description'], 'Resource 101 is stretched over multiple sections')

class Test9(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='retdec_unpacker_sections.ex_',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['identifier'], 'PackerSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Packer section name: gu_idata')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['identifier'], 'PackerSectionName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Packer section name: gu_rsrc')
