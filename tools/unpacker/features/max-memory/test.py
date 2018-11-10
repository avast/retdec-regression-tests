from regression_tests import *


class TestUnpackingWhenNoLimit(Test):
    """Checks that the unpacker correctly unpacks a file when there is no
    memory limit.

    Test for https://github.com/avast-tl/retdec/issues/290
    """

    settings = TestSettings(
        tool='unpacker',
        input='mpress.ex',
    )

    def test_correctly_unpacks_file(self):
        assert self.unpacker.succeeded


class TestUnpackingWhenSufficientLimit(Test):
    """Checks that the unpacker correctly unpacks a file when there is a
    sufficient memory limit.

    Test for https://github.com/avast-tl/retdec/issues/290
    """

    settings = TestSettings(
        tool='unpacker',
        args=[
            '--max-memory 104857600',  # 100 MB
            '--max-memory-half-ram',
        ],
        input='mpress.ex',
    )

    def test_correctly_unpacks_file(self):
        assert self.unpacker.succeeded


class TestUnpackingWhenInvalidLimit(Test):
    """Checks that the unpacker fails with an error when the memory limit is
    invalid.

    Test for https://github.com/avast-tl/retdec/issues/290
    """

    settings = TestSettings(
        tool='unpacker',
        args='--max-memory xxx',  # Invalid limit.
        input='mpress.ex',
    )

    def test_fails_to_unpack_file(self):
        assert not self.unpacker.succeeded, 'unpacker succeeded but should have failed'
        assert 'Invalid value for --max-memory' in self.unpacker.output


# Memory limiting does not work correctly on macOS (see
# https://github.com/avast-tl/retdec/issues/379).
if not on_macos():
    class TestUnpackingWhenInsufficientLimit(Test):
        """Checks that the unpacker fails to unpack a file when the memory limit is
        not sufficient.

        Test for https://github.com/avast-tl/retdec/issues/290
        """

        settings = TestSettings(
            tool='unpacker',
            args='--max-memory 4096',  # Minimal limit is 1 page (4096 bytes).
            input='mpress.ex',
        )

        def test_fails_to_unpack_file(self):
            assert not self.unpacker.succeeded, 'unpacker succeeded but should have failed'
