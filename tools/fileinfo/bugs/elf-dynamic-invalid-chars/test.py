from regression_tests import *


# https://github.com/avast-tl/retdec/issues/82
class TestInvalidCharsReplaced(Test):
    settings = TestSettings(
        tool='fileinfo',
        args='--verbose',
        input='C6F0EFA92E641EA31C08B1F0AA859B7402876B4FA2E65B61E657927F9DC9B6C7'
    )

    def test_correctly_replaced_files(self):
        assert self.fileinfo.succeeded
        assert self.fileinfo.output.contains(r'libr\\xf4\.so\.1')
        assert self.fileinfo.output.contains(r'libglib-\\x12\.0nso\.0')

