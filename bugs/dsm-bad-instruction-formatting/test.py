from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='sed-strip'
    )

    def test_check_dsm(self):
        # TODO: this test must pass in both branches: master and in capstone-decoder, therefore there are two DSM variants for some tests:
        # assert <Codasip variant> or <Capstone variant>
        assert self.out_dsm.contains('0x80489fa:.*cmovnc edi, ebp') or self.out_dsm.contains('0x80489fa:.*cmovae edi, ebp')
        assert self.out_dsm.contains('0x8048ce8:.*cmovz eax, edx') or self.out_dsm.contains('0x8048ce8:.*cmove eax, edx')
        assert self.out_dsm.contains('0x8048d01:.*movzx eax, byte \[ eax \+ 0x804c80c \]') or self.out_dsm.contains('0x8048d01:.*movzx eax, byte ptr \[eax \+ 0x804c80c\]')
        assert self.out_dsm.contains('0x8048ca9:.*jge 0x8048cc9 <function_804892c\+0x39d>')

