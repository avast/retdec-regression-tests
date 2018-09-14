from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='8575',
        args='-k'
    )

    def test_check_for_some_random_strings(self):
        assert self.out_c.has_string_literal('%d')
        assert self.out_c.has_string_literal('%lf %lf')
        assert self.out_c.has_string_literal('% .*lf % .*lf\\n')
        assert self.out_c.has_string_literal('r')
        assert self.out_c.has_string_literal('w')
        assert self.out_c.has_string_literal('Verdana')
        assert self.out_c.has_string_literal('coredll.dll')
        assert self.out_c.has_string_literal('ReportFault')

    def test_has_all_exported_functions(self):
        assert self.out_c.has_func( '_3f__3f_0CGpcx_40__40_QAA_40_XZ' )
        assert self.out_c.has_func( '_3f__3f_4CGpcx_40__40_QAAAAV0_40_ABV0_40__40_Z' )
        assert self.out_c.has_func( '_3f_GetSubPolygonArea_40__40_YAXPAUgpc_polygon_40__40_NPAUgpc_line_40__40__NN0PAN0_40_Z' )
        assert self.out_c.has_func( 'AddContour' )
        assert self.out_c.has_func( 'BoxToPolygon' )
        assert self.out_c.has_func( 'DeleteFont' )
        assert self.out_c.has_func( 'DividePolygon' )
        assert self.out_c.has_func( 'DrawContour' )
        assert self.out_c.has_func( 'DrawString' )
        assert self.out_c.has_func( 'FreePolygon' )
        assert self.out_c.has_func( 'GetBoundingBox' )
        assert self.out_c.has_func( 'GetCentroid' )
        assert self.out_c.has_func( 'GetContour' )
        assert self.out_c.has_func( 'GetPolygonArea' )
        assert self.out_c.has_func( 'GetPolygonPerimeter' )
        assert self.out_c.has_func( 'GpcDifference' )
        assert self.out_c.has_func( 'GpcExclusiveOr' )
        assert self.out_c.has_func( 'GpcIntersect' )
        assert self.out_c.has_func( 'GpcUnion' )
        assert self.out_c.has_func( 'IsHole' )
        assert self.out_c.has_func( 'IsInsideBox' )
        assert self.out_c.has_func( 'IsInsidePolygon' )
        assert self.out_c.has_func( 'ReadPolygon' )
        assert self.out_c.has_func( 'Ring' )
        assert self.out_c.has_func( 'RingVertex' )
        assert self.out_c.has_func( 'SetFont' )
        assert self.out_c.has_func( 'WritePolygon' )

    def test_has_some_random_imported_functions(self):
        assert self.out_c.has_comment_matching(r'.*int32_t _addd\(.*a1.*') # a2.*')
        assert self.out_c.has_comment_matching(r'.*int32_t.*_led\(.*a1.*a2.*')
        assert self.out_c.has_comment_matching(r'.*int32_t.*_subd\(.*\);')
        assert self.out_c.has_comment_matching(r'.*HPEN.*CreatePen\(.*\);')
        assert self.out_c.has_comment_matching(r'.*HGDIOBJ.*SelectObject\(.*\);')
        assert self.out_c.has_comment_matching(r'.*UINT.*SetTextAlign\(.*\);')
        assert self.out_c.has_comment_matching(r'.*size_t.*wcstombs\(.*\);')
        assert self.out_c.has_comment_matching(r'.*COLORREF.*SetTextColor\(.*\);')
        assert self.out_c.has_comment_matching(r'.*FARPROC.*GetProcAddressW\(.*\);')
        assert self.out_c.has_comment_matching(r'.*void.*GetCurrentFT\(.*lpFileTime\);')
