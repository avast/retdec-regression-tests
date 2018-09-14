from regression_tests import *

class Test1(Test):
    settings=TestSettings(
        tool='unpacker',
        input='0a4b312d721b422ab145038cef877772'
    )

    def test_original_header_is_corrupted(self):
        self.assertEqual(self.unpacker.return_code, 2)
        assert self.unpacker.output.contains("Original header contains corrupted data.")

class Test2(Test):
    settings=TestSettings(
        tool='unpacker',
        input='7b21eef69eed96a1657a78f16147f40a'
    )

    def test_filter_is_detected_correctly(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('Detected filter 0x0 with parameter 0x0 based on UPX metadata.')

class Test3(Test):
    settings=TestSettings(
        tool='unpacker',
        input=[
            '160fd4eaf7720894e8247f69026c4bab',
            'd2df52363bba1927192f4d7808097c4f'
        ]
    )

    def test_not_unpackable(self):
        self.assertEqual(self.unpacker.return_code, 1)
        assert not self.unpacker.output.contains('[UPX]')

class Test4(Test):
    settings=TestSettings(
        tool='unpacker',
        input=[
            'c690197287811f8cd6c7c3a6f47ee10e',
            '06149b3cb29664ad4d900481ad6076e2',
            '5955ac958a61e1e856a090b8bef8fe10'
        ]
    )

    def test_unpacks_successfully(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('NRV2B')

class Test5(Test):
    settings=TestSettings(
        tool='unpacker',
        input='71ef6cf6a52f91e354283dfb82ae364e'
    )

    def test_stops_on_failed_decompression(self):
        self.assertEqual(self.unpacker.return_code, 2)
        assert self.unpacker.output.contains('NRV2B')
        assert self.unpacker.output.contains('Failed to decompress compressed data.')
