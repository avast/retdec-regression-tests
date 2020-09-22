from regression_tests import *

class Test(Test):
    settings = TestSettings(
        tool='fileinfo',
        input=[
            'Setup47_1_free.exe_',
            'Setup48_free_empty.exe_'
        ],
        args='--json'
    )

    def test_correctly_analyzes_input_file(self):
        create_install_recognized = False

        self.assertTrue(self.fileinfo.succeeded)
        for tool in self.fileinfo.output['tools']:
            if tool['type'] == 'installer' and tool['name'] == 'GhostInstaller':
                create_install_recognized = True
        self.assertTrue(create_install_recognized)
