from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='EsetCrackme2015a.ex',
    )

    def test_check_for_strings(self):
        assert self.out_c.has_string_literal( 'EsetCrackme2015' )

    def test_check_for_currently_detected_functions(self):
        assert self.out_c.has_func( 'entry_point' )

    def test_check_calls_in_entry_point(self):
        fnc = self.out_c.funcs[ 'entry_point' ]

        assert fnc.calls( 'CreateMutexA' )
        assert fnc.calls( 'GetLastError' )
        assert fnc.calls( 'MessageBoxA' )
        assert fnc.calls( 'GetModuleFileNameA' )
        assert fnc.calls( 'LoadLibraryA' )

        # This is extremely fragile, but there currently is no better way to
        # check for exact arguments and  we want to know about any change.
        assert self.out_c.contains( 'CreateMutexA\(NULL, true,.*"EsetCrackme2015"\)' )

        # TODO
        #assert self.out_c.contains( 'lpCaption = "Error";' )
        #assert (self.out_c.contains( 'MessageBoxA\(NULL, .*"Application already launched ... ", .*lpCaption, 48\)' )
                #or (self.out_c.contains('lpText =.*Application already launched ... ')
                #and self.out_c.contains('MessageBoxA\(NULL, .*lpText, .*lpCaption, 48\)')))
        assert self.out_c.contains( 'GetModuleFileNameA\(NULL, .*&lpFilename, 260\)' )
        assert self.out_c.contains( 'LoadLibraryA\(.*&lpFilename\)' )
        #assert self.out_c.contains( 'lpCaption = "Missing DLL file";' )
        #assert (self.out_c.contains( 'MessageBoxA\(NULL, .*lpFilename, .*lpCaption, 48\)' )
                #or self.out_c.contains( 'MessageBoxA\(NULL, .*lpText, .*lpCaption, 48\)' ))
