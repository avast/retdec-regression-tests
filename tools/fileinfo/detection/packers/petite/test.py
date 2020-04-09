from regression_tests import *

class Test_12(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite12.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(1\.2\)*')


class Test_13(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite13.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(1\.3\)*')


class Test_13a(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=['fact_rec.ex', 'sample_petite13a.ex_']
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(1\.3a\)*')


class Test_14(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite14.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(1\.4\)*')


class Test_20(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite20.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(2\.0\)*')


class Test_21(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite21.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(2\.1\)*')


class Test_22(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite22.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(2\.2\)*')


class Test_23(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite23.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(2\.3\)*')


class Test_24(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='sample_petite24.ex_'
    )

    def test_correctly_analyzes_input_file(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'.*Petite \(2\.4\)*')
