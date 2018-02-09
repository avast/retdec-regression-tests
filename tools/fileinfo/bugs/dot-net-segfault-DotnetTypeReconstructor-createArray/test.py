from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input='C9A34DAE49FBC70270C75FA250239796DFF340813209CCB3421E147052392BF8.dat'
    )

    def test_has_dotnet_info_with_array(self):
        self.assertEqual(self.fileinfo.output['dotnetInfo']['classes'][20]['methods'][0]['returnType'], 'sbyte[6...6,2...2,4...4,,9...9,4...4,2...2,4...4]')
        self.assertEqual(self.fileinfo.output['dotnetInfo']['classes'][20]['methods'][1]['returnType'], 'sbyte[6...6,2...2,4...4,,9...9,4...4,2...2,4...4]')
