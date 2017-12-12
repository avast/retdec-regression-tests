from regression_tests import *

class TestUpxshit(Test):
    settings = TestSettings(
        tool='unpacker',
        input=[
            'fact_rec.ex',
            'pbmsrch_max.ex'
        ]
    )

    def test_scrambler_upxshit(self):
        assert self.unpacker.succeeded
        assert self.unpacker.output.contains('UPX\$HIT scrambler')
