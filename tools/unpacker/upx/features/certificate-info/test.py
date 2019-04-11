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
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][0]["sha256"], "f63b42f1e0c3950730d95b3b6b78b8f7c7991097b5f8d81f64b2c83a1decf5ca")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][1]["sha256"], "8ef8f2565be30e7ce7ba6302bb18b42a3acd148a0ddb4779e4c03e862f39589b")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][2]["sha256"], "2cf1ec6ab594113bd538df6d5c940e3319b424f8756d975888072c6ab558b771")
        self.assertEqual(self.fileinfo.output["certificateTable"]["certificates"][3]["sha256"], "2463525300d9e8e0a6f5d79e2b20b9f5182fe40d3fd7c85ddaf48e6c25bedf5d")
