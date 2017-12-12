from regression_tests import *

class Test(Test):
    settings=TestSettings(
        tool='fileinfo',
        args='--json --verbose',
        input=[
            '059518DC5FC25F1C14E1820DCE1D3B707363F84F281B5F5BA978FDF39B2A77C4.dat',
            '17125778A3CDCCDEB8A5348D4857823CD8615B02C6A73C91C460D8F7AA5C6946.dat',
            '8F289DBC2F980F59A27DF64B158DEE47519D2098BE4D78A4BDDD2C15E5DEFCF6.dat',
            'AA8B82BCABDB93A8C1411FA03F67BEFF6AFEC00A6EBBEE05AD091712BC0A645A.dat',
            '3B173E93A73CC767E826D0B331B871DEF4109DD1DA2E9BC2B7BE9E10AF641EF8.dat',
            '9FBCB70FCB1906858D19B0C3DF1936344DC95A2C7731DCE671E435F67DA31E88.dat'
        ])

    def test_fileinfo_does_not_crash_and_has_dotnet_info(self):
        assert self.fileinfo.succeeded
        assert len(self.fileinfo.output['dotnetInfo']['classes']) > 0
