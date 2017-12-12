"""Tests for the viewer of the generated DSM and HLL on the web."""

from regression_tests import *

class DSMFormatTest(Test):
    """Checks that the DSM is generated in a format that is recognizable by our
    DSM parser on the web.
    """

    settings = TestSettings(
        input='hello-world.ex'
    )

    # IMPORTANT: Do NOT change the format of the generated DSM because the
    #            parser that is used on the web relies on it. If you want
    #            to change it, consult this with Petr Zemek.

    # Scripts that depend on the DSM format:
    # - web/templates/scripts/decompilation-viewer.js
    # - web/templates/scripts/codemirror/mode/*.js

    def test_comment_with_architecture_has_correct_format(self):
        assert self.out_dsm.contains(r';; Architecture: x86')

    def test_comments_with_functions_have_correct_format(self):
        # The parser needs the name of the function and both addresses,
        # separated by ' at ' and ' -- '.
        assert self.out_dsm.contains(r'; *function: main at 0x[0-9a-f]+ -- 0x[0-9a-f]+')
        assert self.out_dsm.contains(r'; *statically linked function: ___pow5mult_D2A at 0x[0-9a-f]+ -- 0x[0-9a-f]+')

    def test_instructions_are_emitted_in_correct_format(self):
        # The tab before the textual representation is important.
        assert self.out_dsm.contains('0x40775a: *31 c0 *\txor eax, eax')

    def test_calls_have_correct_format(self):
        # The space between the address and '<' is important.
        assert self.out_dsm.contains(r'call 0x402300 <___main>')
