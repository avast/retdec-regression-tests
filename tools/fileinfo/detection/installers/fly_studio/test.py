from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            '04d0163cfa2c35b1c34c2669cc9c53e5.ex',
            '067bc8935fed7e353168eef7592bb7e3.ex'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        create_install_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'FlyStudio':
                create_install_recognized = True
        self.assertTrue(create_install_recognized)
