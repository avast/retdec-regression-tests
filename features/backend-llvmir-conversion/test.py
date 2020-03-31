from regression_tests import *

class NoGeneratedLabsTest(Test):
    """Checks that there are no lab_generated_X goto labels.

    There was a bug in WhileTrueToWhileCondOptimizer that caused
    lab_generated_X to be generated instead of using a proper label. For
    example, it converted

        lab_0x11e00:
            while (true) {
                // body
            }

    to

        lab_generated_1:
            // body
            while (cond) {
                // body
            }

    We want the label to be preserved.
    """

    settings = TestSettings(
        input='ackermann.arm.gcc.O0.exe',
    )

    def test_there_are_no_lab_generated_labels(self):
        assert 'lab_generated_' not in self.out_c

class BreakOutsideOfLoopReplacedByGotoTest(Test):
    """
    Checks that if break exists outside of loop, it is replaced
    by goto to the end of loop.
    """

    settings = TestSettings(
        input='IZP-proj1.pic32.gcc.O0.elf',
    )

    def test_there_are_no_breaks(self):
        assert '\n    break' not in self.out_c
        assert '\n        break' not in self.out_c

class UnnecessaryLabelsRemovedTest(Test):
    """
    Checks that no labels are kept after body of labels replaces goto.
    """

    settings = TestSettings(
        input='IZP-proj3.x86.gcc.O3.exe',
    )

    def test_there_are_no_unnecessary_labels(self):
        assert 'lab_0x4018bc' not in self.out_c
        assert 'lab_0x401881' not in self.out_c
        assert 'lab_0x401872' not in self.out_c
        assert 'lab_0x401a29' not in self.out_c
        assert 'lab_0x401a50_2' not in self.out_c
        # TODO: Works only with the new converter, not with the original converter.
        #       Uncomment this when the new converter is used.
        # assert 'lab_0x401aca' not in self.out_c
        assert 'lab_0x401abc_2' not in self.out_c
        assert 'lab_0x401ab8' not in self.out_c

class PostProcessingPerformedCorrectly1(Test):
    settings = TestSettings(
        input='IZP-proj1.x86.gcc.O0.g.exe',
        args='--backend-no-opts'
    )

    # These commented require deep cloning to be introduced first
    # as of right now, if compound statement contains more than one statement
    # cloning will fail.
    def test_labels_replaced_gotos_where_possible(self):
        assert 'lab_0x4016e7' not in self.out_c # had one reference
        assert 'lab_0x4017a2' not in self.out_c # had one reference

        assert 'lab_0x401751_2' not in self.out_c # replaced due to few statements

    # each basic block should keep comments of their address
    # this way we can check the block is really in the code
    # and has not disappeared
    def test_labels_were_correctly_replaced(self):
        assert '0x4016e7' in self.out_c # had one reference
        assert '0x401751' in self.out_c # replaced due to few statements

class PostProcessingPerformedCorrectly2(Test):
    settings = TestSettings(
        input='IZP-proj3.x86.gcc.O0.g.exe',
        args='--backend-no-opts'
    )

    # These commented require deep cloning to be introduced first
    # as of right now, if compound statement contains more than one statement
    # cloning will fail.
    def test_labels_replaced_gotos_where_possible(self):
        #assert 'lab_0x40163f' not in self.out_c # had one reference
        assert 'lab_0x40166c' not in self.out_c # had one reference
        assert 'lab_0x40178c' not in self.out_c # had one reference
        #assert 'lab_0x4016f0' not in self.out_c # had one reference
        #assert 'lab_0x40171c' not in self.out_c # had one reference
        assert 'lab_0x401773' not in self.out_c # had one reference
        assert 'lab_0x40177e_3' not in self.out_c # had one reference
        assert 'lab_0x401914' not in self.out_c # had one reference
        #assert 'lab_0x401cd7' not in self.out_c # had one reference

        '''
        assert 'lab_0x40177e_4' not in self.out_c # had one reference
        This last one is more complicated, in code there is only one goto to it,
        but in internal representation, there are two (result of cloning).. and
        so far I cant figure out a way to tell if predecessor is going to be
        used in code or not.
        '''

    # each basic block should keep comments of their address
    # this way we can check the block is really in the code
    # and has not disappeared
    def test_labels_were_correctly_replaced(self):
        #assert '0x40163f' in self.out_c # had one reference
        assert '0x40166c' in self.out_c # had one reference
        assert '0x40178c' in self.out_c # had one reference
        #assert '0x4016f0' in self.out_c # had one reference
        #assert '0x40171c' in self.out_c # had one reference
        #assert '0x401773' in self.out_c # had one reference
        #assert '0x40177e' in self.out_c # had one reference
        #assert '0x401914' in self.out_c # had one reference
        #assert '0x401cd7' in self.out_c # had one reference

    # this label was referenced by goto, but was not appended to body
    # postprocessing should fix that
    # TODO: Works only with the new converter, not with the original converter.
    #       Uncomment this when the new converter is used.
    # def test_undefined_label_was_corrected(self):
    #     assert 'lab_0x40193d:' in self.out_c # had one reference
