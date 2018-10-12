#
# Makefile for the RetDec's regression-test suite.
#

.PHONY: clean help

help:
	@echo "Use \`make <target>', where <target> is one of"
	@echo "  clean          -> clean all the generated files"

clean:
	@find . -name 'outputs' -type d -exec rm -rf {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*.py[co]' -exec rm -f {} +
	@# Clean empty directories or directories that contain only empty
	@# directories. This is needed because of changes in the structure of
	@# regression tests, like movement of directories. Without this cleaning,
	@# such empty directories would never be removed because git does not show
	@# empty directories in the index.
	@find . -depth -type d -empty -exec rmdir {} \;
