from regression_tests import *

class Test(Test):
    """Checks that we do not optimize stack variables produced in a selective
    decompilation, even if their value is not used.

    For example, in a selective decompilation, we may want to keep the
    following variable assignment, even if the variable is never used:

        v1 = (int32_t)"/var/run/m";
        unknown_80559c4();

    See #1146 for more details.
    """

    settings = TestSettings(
        input='00A2',
        args='--select-ranges=0x8048960-0x8048b9d --select-decode-only'
    )

    def test_accesses_to_stack_variables_are_not_optimized(self):
        # This is simply tested by checking the presence of the strings that
        # are stored into the variables.
        assert self.out_c.has_string_literal('/bin/mi')
        assert self.out_c.has_string_literal('/bin/mii')
        assert self.out_c.has_string_literal('/bin/pp')
        assert self.out_c.has_string_literal('/bin/wget')
        assert self.out_c.has_string_literal('/usr/bin/-wget')
        assert self.out_c.has_string_literal('/usr/bin/wget')
        assert self.out_c.has_string_literal('/var/run/.lightscan')
        assert self.out_c.has_string_literal('/var/run/32')
        assert self.out_c.has_string_literal('/var/run/a')
        assert self.out_c.has_string_literal('/var/run/arm')
        assert self.out_c.has_string_literal('/var/run/arm')
        assert self.out_c.has_string_literal('/var/run/arml')
        assert self.out_c.has_string_literal('/var/run/ax')
        assert self.out_c.has_string_literal('/var/run/dev')
        assert self.out_c.has_string_literal('/var/run/gcc')
        assert self.out_c.has_string_literal('/var/run/lightscan')
        assert self.out_c.has_string_literal('/var/run/m')
        assert self.out_c.has_string_literal('/var/run/mi')
        assert self.out_c.has_string_literal('/var/run/mips')
        assert self.out_c.has_string_literal('/var/run/mips.l')
        assert self.out_c.has_string_literal('/var/run/mipsel')
        assert self.out_c.has_string_literal('/var/run/mipsell')
        assert self.out_c.has_string_literal('/var/run/mpl')
        assert self.out_c.has_string_literal('/var/run/mps')
        assert self.out_c.has_string_literal('/var/run/msx')
        assert self.out_c.has_string_literal('/var/run/mx')
        assert self.out_c.has_string_literal('/var/run/p')
        assert self.out_c.has_string_literal('/var/run/pid')
        assert self.out_c.has_string_literal('/var/run/ppc')
        assert self.out_c.has_string_literal('/var/run/ppcl')
        assert self.out_c.has_string_literal('/var/run/psx')
        assert self.out_c.has_string_literal('/var/run/px')
        assert self.out_c.has_string_literal('/var/run/s')
        assert self.out_c.has_string_literal('/var/run/sel')
        assert self.out_c.has_string_literal('/var/run/sh')
        assert self.out_c.has_string_literal('/var/run/shl')
        assert self.out_c.has_string_literal('/var/run/sph')
        assert self.out_c.has_string_literal('/var/run/sx')
        assert self.out_c.has_string_literal('/var/tmp/dreams.install.sh')
        assert self.out_c.has_string_literal('/var/tmp/ep2.ppc')
