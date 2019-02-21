from regression_tests import *

class Test(Test):
    settings=TestSettings(
        input='test.bin',
        mode='raw',
        arch='mips',
        args='--endian little --raw-entry-point 0x400000 --raw-section-vma 0x400000'
    )

    def test_for_branches(self):
        assert self.out_ll.contains('%dec_label_pc_400000')
        assert self.out_ll.contains('br label %dec_label_pc_400010')
        assert self.out_ll.contains('%dec_label_pc_400010')
        assert self.out_ll.contains('; preds = %dec_label_pc_400000, %dec_label_pc_400010')
