from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='sgrep-strip',
        args='-k'  # TODO: matula, not sure if some functions are not called, or we just do not detect it.
    )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal( '                  ' )
        assert self.out_c.has_string_literal( '                                    \\r' )
        assert self.out_c.has_string_literal( '                              \\r' )
        assert self.out_c.has_string_literal( '  %-18s%6.2fs %6.2fs %6.2fs\\n' )
        assert self.out_c.has_string_literal( '  -----------------------------------------\\n' )
        assert self.out_c.has_string_literal( ' %d gc blocks used, %d gc blocks allocated.\\n' )
        assert self.out_c.has_string_literal( ' %d gc lists, %d gc lists allocated\\n' )
        assert self.out_c.has_string_literal( ' %d same phrases\\n' )
        assert self.out_c.has_string_literal( ' %d sorts optimized\\n' )
        assert self.out_c.has_string_literal( ' %dK nest stack size, %dK inner tablesize\\n' )
        assert self.out_c.has_string_literal( ' Longest list size was %d regions.\\n' )
        assert self.out_c.has_string_literal( " ] 'expr' [<files...>]\\n" )
        assert self.out_c.has_string_literal( '%-18s%8s%8s%8s\\n' )
        assert self.out_c.has_string_literal( '%15s:%-4d%6s:%-4d%5s:%-4d%5s:%-4d%11s:%-4d%4s:%-4d\\n' )
        assert self.out_c.has_string_literal( '%15s:%-4d%6s:%-4d\\n' )
        assert self.out_c.has_string_literal( '%d\\n' )
        assert self.out_c.has_string_literal( '%s %d%% done%s\\r' )
        assert self.out_c.has_string_literal( '%s: short read\\n' )
        assert self.out_c.has_string_literal( '%s\\n' )
        assert self.out_c.has_string_literal( '(*n1)->label_left!=2 || (*n1)->right==((void *)0)' )
        assert self.out_c.has_string_literal( '(s->sorted) && (!s->end_sorted)' )
        assert self.out_c.has_string_literal( '++rounds<1000' )
        assert self.out_c.has_string_literal( '-%c requires an argument\\n' )
        assert self.out_c.has_string_literal( '/use/local/lib/sgreprc' )
        #assert self.out_c.has_string_literal( '<input exceeded>' )
        #assert self.out_c.has_string_literal( '<stdin>' )
        assert self.out_c.has_string_literal( 'ACsearch' )
        assert self.out_c.has_string_literal( 'Basic expression expected\\n' )
        assert self.out_c.has_string_literal( "Can't read input from stdin, it's already used\\n" )
        assert self.out_c.has_string_literal( 'Command file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'Copyright (C) 1996  University of Helsinki' )
        assert self.out_c.has_string_literal( 'Empty command file %s\\n' )
        assert self.out_c.has_string_literal( 'Empty stdin\\n' )
        assert self.out_c.has_string_literal( 'Empty style file %s\\n' )
        assert self.out_c.has_string_literal( 'Expression too long (>%d)\\n' )
        assert self.out_c.has_string_literal( 'File %s truncated before search\\n' )
        assert self.out_c.has_string_literal( 'HOME' )
        assert self.out_c.has_string_literal( 'If no files are given stdin is used instead.' )
        assert self.out_c.has_string_literal( 'Inbuilt preprocessor not implemented yet.\\n' )
        assert self.out_c.has_string_literal( 'Invalid SGREPOPT (SGREPOPT=%s)\\n' )
        #assert self.out_c.has_string_literal( 'Invalid character' )
        assert self.out_c.has_string_literal( 'Memory allocation failed.\\n' )
        assert self.out_c.has_string_literal( 'Memory:\\n %dK memory allocated, %d realloc operations\\n' )
        assert self.out_c.has_string_literal( 'No files or expressions allowed in SGREPOPT\\n' )
        assert self.out_c.has_string_literal( 'No valid files\\n' )
        assert self.out_c.has_string_literal( 'Operations:\\n%15s:%-4d%6s:%-4d%5s:%-4d%5s:%-4d%11s:%-4d%3s:%-4d\\n' )
        assert self.out_c.has_string_literal( 'Operator expected' )
        assert self.out_c.has_string_literal( 'Operator tree size was %d, optimized %d\\n' )
        assert self.out_c.has_string_literal( 'Options can also be specified with SGREPOPT environment variable' )
        assert self.out_c.has_string_literal( 'Output list size was %d regions.\\n' )
        assert self.out_c.has_string_literal( 'Parse error on line %d column %d :\\n\\t%s\\n%s\\n' )
        assert self.out_c.has_string_literal( "Premature end of parsing. ( This shouldn't happen!! )\\n" )
        assert self.out_c.has_string_literal( 'Read command file' )
        assert self.out_c.has_string_literal( 'SGREPOPT' )
        assert self.out_c.has_string_literal( 'Scanned %d files, having total of %dK size finding %d phrases.\\n' )
        assert self.out_c.has_string_literal( 'Short write to tempfile\\n' )
        assert self.out_c.has_string_literal( "Stdin already read, Can't read expressions from stdin\\n" )
        assert self.out_c.has_string_literal( 'Strange expression type\\n' )
        assert self.out_c.has_string_literal( 'Things done:\\n %d %s, %d %s, %d %s\\n %d %s, %d %s\\n' )
        assert self.out_c.has_string_literal( 'Too complex SGREPOPT\\n' )
        assert self.out_c.has_string_literal( "Too many )'s" )
        assert self.out_c.has_string_literal( 'Unexpected end of expression' )
        assert self.out_c.has_string_literal( 'Unsupported operation in parse tree (%d)\\n' )
        assert self.out_c.has_string_literal( "Usage: sgrep <options> 'region expression' [<files...>]" )
        assert self.out_c.has_string_literal( 'Usage: sgrep [ -' )
        assert self.out_c.has_string_literal( 'Warning: region end point greater than input size detected\\n' )
        assert self.out_c.has_string_literal( 'Warning: region start point greater than input size detected\\n' )
        assert self.out_c.has_string_literal( "You have to give an expression line if you don't use -f or -e switch.\\n" )
        assert self.out_c.has_string_literal( '\\nCopyright (C) 1996 University of Helsinki. Use sgrep -C for details,\\n' )
        assert self.out_c.has_string_literal( '\\noptions are:' )
        assert self.out_c.has_string_literal( '\\t' )
        assert self.out_c.has_string_literal( '\\t%s\\n' )
        assert self.out_c.has_string_literal( '\\t-%c %s\\t%s\\n' )
        assert self.out_c.has_string_literal( '\\t--\\t\\tno more options' )
        assert self.out_c.has_string_literal( 'acsearch' )
        assert self.out_c.has_string_literal( 'bin_file_search' )
        assert self.out_c.has_string_literal( 'c->length==0 && c->last==c->first' )
        assert self.out_c.has_string_literal( 'c_reg.start<inner_stack[inq_ind-1].start || c_reg.end>inner_stack[inq_ind-1].end' )
        assert self.out_c.has_string_literal( 'common.c' )
        assert self.out_c.has_string_literal( 'comp_tree_nodes' )
        assert self.out_c.has_string_literal( 'concat' )
        #assert self.out_c.has_string_literal( 'constant gc list must be sorted' )
        assert self.out_c.has_string_literal( 'containing' )
        assert self.out_c.has_string_literal( 'create_reference_counters' )
        assert self.out_c.has_string_literal( 'creating tempfile: open' )
        assert self.out_c.has_string_literal( 'dad->left!=((void *)0)' )
        assert self.out_c.has_string_literal( 'do_add_region' )
        assert self.out_c.has_string_literal( 'do_prev_region' )
        assert self.out_c.has_string_literal( 'equal' )
        assert self.out_c.has_string_literal( 'eval' )
        assert self.out_c.has_string_literal( 'eval.c' )
        assert self.out_c.has_string_literal( 'evaluating' )
        assert self.out_c.has_string_literal( 'exprs>0' )
        assert self.out_c.has_string_literal( 'extracting' )
        assert self.out_c.has_string_literal( 'fork' )
        assert self.out_c.has_string_literal( 'free_tree_node' )
        assert self.out_c.has_string_literal( 'gc lists scanned' )
        assert self.out_c.has_string_literal( 'gc_lists_now<=4' )
        assert self.out_c.has_string_literal( 'gc_lists_now==stats.constant_lists' )
        assert self.out_c.has_string_literal( 'handle->list->last->next==((void *)0)' )
        assert self.out_c.has_string_literal( 'in' )
        assert self.out_c.has_string_literal( 'inner' )
        assert self.out_c.has_string_literal( 'inner_stack[i].start<=c_reg.start' )
        assert self.out_c.has_string_literal( 'invalid constant region list' )
        assert self.out_c.has_string_literal( 'join' )
        assert self.out_c.has_string_literal( 'l->first!=((void *)0)' )
        assert self.out_c.has_string_literal( 'l->length==0 || !l->sorted || l->end_sorted|| l->nested || e>l->last->list[l->length-1].end' )
        assert self.out_c.has_string_literal( 'lseek %s: %s\\n' )
        assert self.out_c.has_string_literal( 'lseek <stdin>' )
        assert self.out_c.has_string_literal( 'lseek style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'main.c' )
        assert self.out_c.has_string_literal( 'n_reg.start>=c_reg.start || n_reg.start==-1' )
        assert self.out_c.has_string_literal( 'node->GC_list->refcount>=0 || node->GC_list->refcount==-1' )
        assert self.out_c.has_string_literal( 'not containing' )
        assert self.out_c.has_string_literal( 'not equal' )
        assert self.out_c.has_string_literal( 'not in' )
        assert self.out_c.has_string_literal( 'number>0' )
        assert self.out_c.has_string_literal( 'op->phrase->GC_list!=((void *)0)' )
        assert self.out_c.has_string_literal( 'open %s: %s\\n' )
        assert self.out_c.has_string_literal( 'open style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'optimize.c' )
        assert self.out_c.has_string_literal( 'or' )
        assert self.out_c.has_string_literal( 'order' )
        assert self.out_c.has_string_literal( 'outer' )
        assert self.out_c.has_string_literal( 'output' )
        assert self.out_c.has_string_literal( 'output.c' )
        assert self.out_c.has_string_literal( 'parsing' )
        assert self.out_c.has_string_literal( 'pmatch.c' )
        assert self.out_c.has_string_literal( 'pn->parent!=((void *)0)' )
        assert self.out_c.has_string_literal( 'pn->parent->label_left==4' )
        assert self.out_c.has_string_literal( 'preprocessor' )
        assert self.out_c.has_string_literal( 'quote' )
        assert self.out_c.has_string_literal( 'quote: invalid oper type\\n' )
        assert self.out_c.has_string_literal( 'r.node!=((void *)0)' )
        assert self.out_c.has_string_literal( 'r1.start!=-1' )
        assert self.out_c.has_string_literal( 'read %s: %s\\n' )
        assert self.out_c.has_string_literal( 'read <stdin>' )
        assert self.out_c.has_string_literal( 'read stdin' )
        assert self.out_c.has_string_literal( 'read style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'read_expressions' )
        assert self.out_c.has_string_literal( 'reg1.end<reg2.end' )
        #assert self.out_c.has_string_literal( 'region end point must be greater than start point' )
        assert self.out_c.has_string_literal( 'regions created' )
        assert self.out_c.has_string_literal( 'remove_duplicate_phrases' )
        assert self.out_c.has_string_literal( 'remove_duplicates' )
        assert self.out_c.has_string_literal( 'root->leaf->GC_list!=((void *)0)' )
        assert self.out_c.has_string_literal( 'root->refcount>=0 || root->refcount==-1' )
        assert self.out_c.has_string_literal( 'run_one_by_one' )
        assert self.out_c.has_string_literal( 'run_stream' )
        assert self.out_c.has_string_literal( 'searching phrases %d%% done\\r' )
        assert self.out_c.has_string_literal( 'sgrep -h for help\\n' )
        assert self.out_c.has_string_literal( 'sgrep time usage' )
        assert self.out_c.has_string_literal( 'sgrep version 0.99 - search a file for structured pattern' )
        assert self.out_c.has_string_literal( 'sgrep warning: unlinking temp file failed' )
        assert self.out_c.has_string_literal( 'sgrep: %s: %s\\n' )
        assert self.out_c.has_string_literal( 'sgrep: lseek tmpfile' )
        assert self.out_c.has_string_literal( 'short read <stdin>' )
        assert self.out_c.has_string_literal( 'shrink_tree' )
        assert self.out_c.has_string_literal( 'sorts by end point' )
        assert self.out_c.has_string_literal( 'sorts by start point' )
        assert self.out_c.has_string_literal( 'sys' )
        assert self.out_c.has_string_literal( 'tmpp.ind==tmp->length && tmpp.node->next==((void *)0)' )
        assert self.out_c.has_string_literal( 'to_chars' )
        assert self.out_c.has_string_literal( 'total' )
        assert self.out_c.has_string_literal( 'usr' )
        assert self.out_c.has_string_literal( 'write tempfile' )
        assert self.out_c.has_string_literal( 'Illegal option -%c\\n' )
        assert self.out_c.has_string_literal( 'handle->list->last->next==((void *)0)' )
        assert self.out_c.has_string_literal( 'l->length<=( 1 << 7 )' )
        assert self.out_c.has_string_literal( 'start_region_search' )
        assert self.out_c.has_string_literal( ' -%c %s' )
        #assert self.out_c.has_string_literal( 'l->last->next==((void *)0)' )          # TODO: non-deterministic, sometimes it is there, sometimes it is not.
        #assert self.out_c.has_string_literal( 'handle->list->length<=( 1 << 7 )' )          # TODO: non-deterministic, sometimes it is there, sometimes it is not.
        #assert self.out_c.has_string_literal( 'do_get_region' )          # TODO: non-deterministic, sometimes it is there, sometimes it is not.

    # Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
    #
    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( 'function_10000974' )  #
        #assert self.out_c.has_func( 'function_10000988' )  #
        assert self.out_c.has_func( 'entry_point' )  # function_100009c0
        assert self.out_c.has_func( 'function_100009e4' )  #
        assert self.out_c.has_func( 'function_10000a8c' )  #
        assert self.out_c.has_func( 'function_10000aa8' )  #
        assert self.out_c.has_func( 'function_10000af0' )  #
        assert self.out_c.has_func( 'function_10000b0c' )  #
        assert self.out_c.has_func( 'function_10000ed8' )  #
        assert self.out_c.has_func( 'function_1000103c' )  #
        assert self.out_c.has_func( 'function_10001100' )  #
        assert self.out_c.has_func( 'function_1000117c' )  #
        assert self.out_c.has_func( 'function_1000123c' )  #
        assert self.out_c.has_func( 'function_100012d4' )  #
        assert self.out_c.has_func( 'function_100014d4' )  #
        assert self.out_c.has_func( 'function_1000163c' )  #
        assert self.out_c.has_func( 'function_100017c8' )  #
        assert self.out_c.has_func( 'function_100017f8' )  #
        assert self.out_c.has_func( 'function_10001b10' )  #
        assert self.out_c.has_func( 'function_10001b50' )  #
        assert self.out_c.has_func( 'function_10001bdc' )  #
        assert self.out_c.has_func( 'function_10001d20' )  #
        assert self.out_c.has_func( 'function_10001fcc' )  #
        assert self.out_c.has_func( 'function_10002228' )  #
        assert self.out_c.has_func( 'function_10002290' )  #
        assert self.out_c.has_func( 'function_100026cc' )  #
        assert self.out_c.has_func( 'main' )  #
        assert self.out_c.has_func( 'function_10002cf8' )  #
        assert self.out_c.has_func( 'function_10002de8' )  # end_first
        assert self.out_c.has_func( 'function_10002e40' )  # start_first
        assert self.out_c.has_func( 'function_10002e98' )  #
        assert self.out_c.has_func( 'function_10002f00' )  #
        assert self.out_c.has_func( 'function_10002f88' )  #
        assert self.out_c.has_func( 'function_10002fc8' )  #
        assert self.out_c.has_func( 'function_10003030' )  #
        assert self.out_c.has_func( 'function_1000309c' )  #
        assert self.out_c.has_func( 'function_100030fc' )  #
        assert self.out_c.has_func( 'function_10003190' )  #
        assert self.out_c.has_func( 'function_10003240' )  #
        assert self.out_c.has_func( 'function_10003494' )  #
        assert self.out_c.has_func( 'function_10003574' )  #
        assert self.out_c.has_func( 'function_1000371c' )  #
        assert self.out_c.has_func( 'function_10003944' )  #
        assert self.out_c.has_func( 'function_1000398c' )  #
        assert self.out_c.has_func( 'function_100039f8' )  #
        assert self.out_c.has_func( 'function_10003be8' )  #
        assert self.out_c.has_func( 'function_10003c88' )  #
        #assert self.out_c.has_func( 'function_10003d30' )  # give_oper_name
        #assert self.out_c.has_func( 'function_10003d50' )  #
        #assert self.out_c.has_func( 'function_10003d5c' )  #
        #assert self.out_c.has_func( 'function_10003d68' )  #
        #assert self.out_c.has_func( 'function_10003d74' )  #
        #assert self.out_c.has_func( 'function_10003d80' )  #
        #assert self.out_c.has_func( 'function_10003d8c' )  #
        #assert self.out_c.has_func( 'function_10003d98' )  #
        #assert self.out_c.has_func( 'function_10003da4' )  #
        #assert self.out_c.has_func( 'function_10003db0' )  #
        #assert self.out_c.has_func( 'function_10003dbc' )  #
        #assert self.out_c.has_func( 'function_10003dc8' )  #
        #assert self.out_c.has_func( 'function_10003dd4' )  #
        #assert self.out_c.has_func( 'function_10003de0' )  #
        #assert self.out_c.has_func( 'function_10003dec' )  #
        #assert self.out_c.has_func( 'function_10003df8' )  #
        #assert self.out_c.has_func( 'function_10003e04' )  #
        #assert self.out_c.has_func( 'function_10003e10' )  #
        #assert self.out_c.has_func( 'function_10003e1c' )  #
        assert self.out_c.has_func( 'function_10003e34' )  #
        assert self.out_c.has_func( 'function_10003fe4' )  #
        assert self.out_c.has_func( 'function_10004060' )  #
        assert self.out_c.has_func( 'function_100041c0' )  #
        assert self.out_c.has_func( 'function_10004940' )  #
        assert self.out_c.has_func( 'function_100049a0' )  #
        assert self.out_c.has_func( 'function_100049fc' )  #
        assert self.out_c.has_func( 'function_10004be4' )  #
        assert self.out_c.has_func( 'function_10004de8' )  #
        assert self.out_c.has_func( 'function_10004e6c' )  #
        assert self.out_c.has_func( 'function_100051d0' )  #
        assert self.out_c.has_func( 'function_10005298' )  #
        assert self.out_c.has_func( 'function_100053a4' )  #
        assert self.out_c.has_func( 'function_100054a0' )  #
        assert self.out_c.has_func( 'function_1000568c' )  #
        assert self.out_c.has_func( 'function_10005768' )  #
        assert self.out_c.has_func( 'function_100057e0' )  #
        assert self.out_c.has_func( 'function_1000580c' )  #
        assert self.out_c.has_func( 'function_10005ac8' )  #
        assert self.out_c.has_func( 'function_10005b98' )  #
        assert self.out_c.has_func( 'function_10005bfc' )  #
        assert self.out_c.has_func( 'function_10005e68' )  #
        assert self.out_c.has_func( 'function_10005ecc' )  #
        assert self.out_c.has_func( 'function_10005f3c' )  #
        assert self.out_c.has_func( 'function_1000608c' )  #
        assert self.out_c.has_func( 'function_10006108' )  #
        assert self.out_c.has_func( 'function_10006270' )  #
        assert self.out_c.has_func( 'function_100065d4' )  #
        assert self.out_c.has_func( 'function_10006688' )  #
        assert self.out_c.has_func( 'function_100066e4' )  #
        assert self.out_c.has_func( 'function_10006858' )  #
        assert self.out_c.has_func( 'function_100069c4' )  #
        assert self.out_c.has_func( 'function_10006d80' )  #
        assert self.out_c.has_func( 'function_10006f9c' )  #
        assert self.out_c.has_func( 'function_100073f8' )  #
        assert self.out_c.has_func( 'function_100077b0' )  #
        assert self.out_c.has_func( 'function_10007ac0' )  #
        assert self.out_c.has_func( 'function_10007df8' )  #
        assert self.out_c.has_func( 'function_10007f48' )  #
        assert self.out_c.has_func( 'function_10008324' )  #
        assert self.out_c.has_func( 'function_1000855c' )  #
        assert self.out_c.has_func( 'function_1000882c' )  #
        assert self.out_c.has_func( 'function_100089b8' )  #
        assert self.out_c.has_func( 'function_10008bb4' )  #
        assert self.out_c.has_func( 'function_10008f0c' )  #
        assert self.out_c.has_func( 'function_10009004' )  #
        assert self.out_c.has_func( 'function_100090c0' )  #
        assert self.out_c.has_func( 'function_100091ac' )  #
        assert self.out_c.has_func( 'function_10009420' )  #
        assert self.out_c.has_func( 'function_10009544' )  #
        assert self.out_c.has_func( 'function_1000980c' )  #
        assert self.out_c.has_func( 'function_100098c4' )  #
        assert self.out_c.has_func( 'function_10009c70' )  #
