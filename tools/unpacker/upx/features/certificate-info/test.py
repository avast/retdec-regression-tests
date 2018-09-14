from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='unpacker',
        input='x86-pe-4a66a6fea03ce7005bef7085a4e87e42',
        run_fileinfo=True
    )

    def test_certificate_directory(self):
        assert self.unpacker.succeeded
        assert self.fileinfo.succeeded
        self.assertEqual(self.fileinfo.output["certificateTable"]["numberOfCertificates"], "4")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "F63B42F1E0C3950730D95B3B6B78B8F7C7991097B5F8D81F64B2C83A1DECF5CA")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "8EF8F2565BE30E7CE7BA6302BB18B42A3ACD148A0DDB4779E4C03E862F39589B")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "2CF1EC6AB594113BD538DF6D5C940E3319B424F8756D975888072C6AB558B771")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "2463525300D9E8E0A6F5D79E2B20B9F5182FE40D3FD7C85DDAF48E6C25BEDF5D")
