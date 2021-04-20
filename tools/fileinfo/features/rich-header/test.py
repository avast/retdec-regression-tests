from regression_tests import *

class Test_001(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=['file-32bit.ex_', 'file-64bit.ex_']
    )

    def test_rich_header_hashes(self):
        self.assertEqual(self.fileinfo.output['richHeader']['crc32'], '16861530')
        self.assertEqual(self.fileinfo.output['richHeader']['md5'], 'de84ff8c697e83363b298b766d419a35') # checked against VT
        self.assertEqual(self.fileinfo.output['richHeader']['sha256'], 'b25a3fc8763b4ff2188560f49c45a9baf8076f2a5a01394c033a4661ae895b2c')

    def test_rich_header_values(self):
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][0]['count'], '3')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][0]['product_id'], '123.50727')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][0]['product_name'], 'Implib800')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][0]['vs_name'], 'Visual Studio 2005 v8.0')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][1]['count'], '10')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][1]['product_id'], '1.0')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][1]['product_name'], 'Import')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][2]['count'], '1')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][2]['product_id'], '138.30729')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][2]['product_name'], 'Utc1500_LTCG_CPP')
        self.assertEqual(self.fileinfo.output['richHeader']['richHeaderRecords'][2]['vs_name'], 'Visual Studio 2008 v9.0')

