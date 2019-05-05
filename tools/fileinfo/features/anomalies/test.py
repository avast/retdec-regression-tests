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
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'epInWritableSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Unusual section name: UPX0')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['abbreviation'], 'packedSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Packer section name: UPX0')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['abbreviation'], 'uninitSecHasData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Section UPX0 is marked uninitialized but contains data')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['description'], 'Unusual section name: UPX1')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['abbreviation'], 'packedSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['description'], 'Packer section name: UPX1')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['abbreviation'], 'unusualSecChar')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['description'], 'Section .rsrc has unusual characteristics')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][7]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][7]['description'], 'Unusual section name: .imports')

class Test2(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='CRACKME3.EX',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'epInLastSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in last section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'epInWritableSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Unusual section name: YADO')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['abbreviation'], 'noRawDataSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Section YADO has zero SizeOfRawData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['abbreviation'], 'duplSecNames')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['description'], 'Multiple sections with name YADO')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['abbreviation'], 'noRawDataSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['description'], 'Section YADO has zero SizeOfRawData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['abbreviation'], 'noRawDataSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['description'], 'Section YADO has zero SizeOfRawData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][7]['abbreviation'], 'noRawDataSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][7]['description'], 'Section YADO has zero SizeOfRawData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][8]['abbreviation'], 'noRawDataSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][8]['description'], 'Section YADO has zero SizeOfRawData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][9]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][9]['description'], 'Unusual section name: krypton')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][10]['abbreviation'], 'noRawDataSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][10]['description'], 'Section krypton has zero SizeOfRawData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][11]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][11]['description'], 'Unusual section name: _!_!_!_')

class Test3(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='fact_rec.ex',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'epInLastSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in last section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'epInWritableSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['abbreviation'], 'epInNonExecSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Entry point in nonexecutable section')

class Test4(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='tiny_no_sections',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'epOutsideSecs')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point is outside of mapped sections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'sizeOfHeadersNotAligned')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'SizeOfHeaders is not aligned to multiple of FileAlignment')

class Test5(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='PTTAdresForm.ex',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Unusual section name: CODE\u0011')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'unusualSecName')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Unusual section name: D\u0011TA')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['abbreviation'], 'overlappingSecs')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Sections D\u0011TA and BSS\u0011 overlap')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['abbreviation'], 'overlappingSecs')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Sections D\u0011TA and .idata overlap')

class Test6(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='tiny_no_sections',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'epOutsideSecs')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point is outside of mapped sections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'sizeOfHeadersNotAligned')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'SizeOfHeaders is not aligned to multiple of FileAlignment')

class Test7(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='5c6dd5fc0fef8736f8fd1bebab8f1c3e',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'epInWritableSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Entry point in writable section')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'unusualSecChar')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Section .text has unusual characteristics')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['abbreviation'], 'largeRes')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Resource 103 has size over 100MB')

class Test8(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='custom_malformed',
        args='--verbose --json'
    )

    def test_anomalies_presented(self):
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['abbreviation'], 'largeSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][0]['description'], 'Section .text has size over 100MB')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['abbreviation'], 'overlappingSecs')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][1]['description'], 'Sections .text and .rsrc overlap')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['abbreviation'], 'noRawDataSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][2]['description'], 'Section .data has zero SizeOfRawData')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['abbreviation'], 'largeSec')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][3]['description'], 'Section .rsrc has size over 100MB')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['abbreviation'], 'largeRes')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][4]['description'], 'Resource 101 has size over 100MB')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['abbreviation'], 'stretchedRes')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][5]['description'], 'Resource 101 is stretched over multiple sections')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['abbreviation'], 'obsoleteCoffFlags')
        self.assertEqual(self.fileinfo.output['anomalyTable']['anomalies'][6]['description'], 'Coff file flags are obsolete')
