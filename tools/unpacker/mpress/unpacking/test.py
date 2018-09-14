from regression_tests import *

def find_data_in_version_sample(out_c):
    assert out_c.has_string_literal('Hello World!\\r\\n')
    assert out_c.has_func('entry_point')
    ep_func = out_c.funcs['entry_point']
    assert ep_func.calls('printf', 'exit')

def find_data_in_msvc_sample(out_c):
    assert out_c.has_string_literal('Hello World!\\r\\n')
    assert out_c.has_func('main')
    ep_func = out_c.funcs['main']
    assert ep_func.calls('WSAStartup', 'printf')


class TestCodeAfterData105(Test):
    settings = TestSettings(
        input = 'mpress_105_code_after_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeAfterData127(Test):
    settings = TestSettings(
        input = 'mpress_127_code_after_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeAfterData205(Test):
    settings = TestSettings(
        input = 'mpress_205_code_after_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeAfterData219(Test):
    settings = TestSettings(
        input = 'mpress_219_code_after_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)

class TestCodeBeforeData105(Test):
    settings = TestSettings(
        input = 'mpress_105_code_before_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeBeforeData127(Test):
    settings = TestSettings(
        input = 'mpress_127_code_before_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeBeforeData205(Test):
    settings = TestSettings(
        input = 'mpress_205_code_before_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeBeforeData219(Test):
    settings = TestSettings(
        input = 'mpress_219_code_before_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)

class TestCodeInBetweenData105(Test):
    settings = TestSettings(
        input = 'mpress_105_code_in_between_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeInBetweenData127(Test):
    settings = TestSettings(
        input = 'mpress_127_code_in_between_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeInBetweenData205(Test):
    settings = TestSettings(
        input = 'mpress_205_code_in_between_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestCodeInBetweenData219(Test):
    settings = TestSettings(
        input = 'mpress_219_code_in_between_data'
    )

    def test(self):
        find_data_in_version_sample(self.out_c)


class TestMsvcLzmaSample(Test):
    settings = TestSettings(
        input = 'mpress_219_msvc_lzma'
    )

    def test(self):
        find_data_in_msvc_sample(self.out_c)


class TestMsvcLzmatSample(Test):
    settings = TestSettings(
        input = 'mpress_219_msvc_lzmat'
    )

    def test(self):
        find_data_in_msvc_sample(self.out_c)
