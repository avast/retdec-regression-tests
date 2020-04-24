from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            '87d55c52d358adb705d0b58f478a3e555acf76b7ba79f9eea6353d18cef558ca',
            'db23546116825fe5fd43210e3f2595cd675eab72e2f900df4a2b6756737379c0'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        astrum_recognised = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'Astrum':
                astrum_recognised = True
        self.assertTrue(astrum_recognised)
