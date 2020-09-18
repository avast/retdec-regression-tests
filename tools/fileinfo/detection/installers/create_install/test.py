from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'CreateInstall-example-491.exe_',
            'CreateInstall-example-801.exe_'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        create_install_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'CreateInstall':
                create_install_recognized = True
        self.assertTrue(create_install_recognized)
