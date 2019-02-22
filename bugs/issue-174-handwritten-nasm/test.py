from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='CLR.exe',
    )

    def test_quality(self):
        # Checked against IDA
        assert self.out_c.has_comment_matching('// Address range: 0x401000 - 0x4010cb')
        fnc = self.out_c.funcs['entry_point']
        assert fnc.calls('GetStdHandle')
        assert fnc.calls('GetProcessHeap')
        assert fnc.calls('GetConsoleMode')
        assert fnc.calls('GetConsoleScreenBufferInfo')
        assert fnc.calls('GetCommandLineW')
        assert fnc.calls('lstrlenW')
        assert fnc.calls('WideCharToMultiByte')
        assert fnc.calls('HeapAlloc')
        assert fnc.calls('WideCharToMultiByte')
        assert fnc.calls('function_4010cb')
        assert fnc.calls('ExitProcess')

        # Checked against IDA
        assert self.out_c.has_comment_matching('// Address range: 0x4010cb - 0x401188')
        fnc = self.out_c.funcs['function_4010cb']
        assert fnc.calls('WriteFile')

        # Checked against IDA
        assert self.out_c.has_comment_matching('// Address range: 0x401188 - 0x4011a2')
        fnc = self.out_c.funcs['function_401188']

        assert self.out_c.has_comment_matching('// Address range: 0x40129c - 0x4012a2')
        fnc = self.out_c.funcs['function_40129c']
        assert fnc.calls('lstrlenW')

        assert self.out_c.has_comment_matching('// Address range: 0x4012a4 - 0x4012aa')
        fnc = self.out_c.funcs['function_4012a4']
        assert fnc.calls('WriteFile')

        assert self.out_c.has_comment_matching('// Address range: 0x4012ac - 0x4012b2')
        fnc = self.out_c.funcs['function_4012ac']
        assert fnc.calls('WideCharToMultiByte')

        assert self.out_c.has_comment_matching('// Address range: 0x4012b4 - 0x4012ba')
        fnc = self.out_c.funcs['function_4012b4']
        assert fnc.calls('SetConsoleTextAttribute')

        assert self.out_c.has_comment_matching('// Address range: 0x4012bc - 0x4012c2')
        fnc = self.out_c.funcs['function_4012bc']
        assert fnc.calls('HeapAlloc')

        assert self.out_c.has_comment_matching('// Address range: 0x4012c4 - 0x4012ca')
        fnc = self.out_c.funcs['function_4012c4']
        assert fnc.calls('GetStdHandle')

        assert self.out_c.has_comment_matching('// Address range: 0x4012cc - 0x4012d2')
        fnc = self.out_c.funcs['function_4012cc']
        assert fnc.calls('GetProcessHeap')

        assert self.out_c.has_comment_matching('// Address range: 0x4012d4 - 0x4012da')
        fnc = self.out_c.funcs['function_4012d4']
        assert fnc.calls('GetConsoleScreenBufferInfo')

        assert self.out_c.has_comment_matching('// Address range: 0x4012dc - 0x4012e2')
        fnc = self.out_c.funcs['function_4012dc']
        assert fnc.calls('GetConsoleMode')

        assert self.out_c.has_comment_matching('// Address range: 0x4012e4 - 0x4012ea')
        fnc = self.out_c.funcs['function_4012e4']
        assert fnc.calls('GetCommandLineW')

        assert self.out_c.has_comment_matching('// Address range: 0x4012ec - 0x4012f2')
        fnc = self.out_c.funcs['function_4012ec']
        assert fnc.calls('ExitProcess')

        # There are no more functions.
        assert len(self.out_c.funcs) == 14
