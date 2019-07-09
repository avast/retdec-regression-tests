from regression_tests import *

class TestX86GccExe(Test):
    settings = TestSettings(
        tool='r2plugin',
        input='ack.x86.mingw32-gcc-4.7.3.O0.g.ex',
        #args=''
    )

    def test(self):
        print('===========> TestX86GccExe::test()')
