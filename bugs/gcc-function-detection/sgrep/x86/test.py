from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='sgrep-strip',
        args='-k'
    )

    def test_check_for_all_currently_detected_strings(self):
        assert self.out_c.has_string_literal( '                  ' )
        assert self.out_c.has_string_literal( '                              \\r' )
        assert self.out_c.has_string_literal( '  %-18s%6.2fs %6.2fs %6.2fs\\n' )
        assert self.out_c.has_string_literal( '  -----------------------------------------\\n' )
        assert self.out_c.has_string_literal( ' %d gc blocks used, %d gc blocks allocated.\\n' )
        assert self.out_c.has_string_literal( ' %d gc lists, %d gc lists allocated\\n' )
        assert self.out_c.has_string_literal( ' %d same phrases\\n' )
        assert self.out_c.has_string_literal( ' %d sorts optimized\\n' )
        assert self.out_c.has_string_literal( ' %dK nest stack size, %dK inner tablesize\\n' )
        assert self.out_c.has_string_literal( ' -%c %s' )
        assert self.out_c.has_string_literal( ' Longest list size was %d regions.\\n' )
        assert self.out_c.has_string_literal( " ] 'expr' [<files...>]\\n" )
        assert self.out_c.has_string_literal( '%-18s%8s%8s%8s\\n' )
        assert self.out_c.has_string_literal( '%15s:%-4d%6s:%-4d%5s:%-4d%5s:%-4d%11s:%-4d%4s:%-4d\\n' )
        assert self.out_c.has_string_literal( '%15s:%-4d%6s:%-4d\\n' )
        assert self.out_c.has_string_literal( '%d' )
        assert self.out_c.has_string_literal( '%d\\n' )
        assert self.out_c.has_string_literal( '%s %d%% done%s\\r' )
        assert self.out_c.has_string_literal( '%s ( > %d ) %s %d\\n%s\\n%s\\n' )
        assert self.out_c.has_string_literal( '%s: short read\\n' )
        assert self.out_c.has_string_literal( '%s\\n' )
        assert self.out_c.has_string_literal( '(*n1)->label_left!=2 || (*n1)->right==((void *)0)' )
        assert self.out_c.has_string_literal( '(*n2)->label_left!=2 || (*n2)->right==((void *)0)' )
        assert self.out_c.has_string_literal( '(s->sorted) && (!s->end_sorted)' )
        assert self.out_c.has_string_literal( ') expected' )
        assert self.out_c.has_string_literal( '++rounds<1000' )
        assert self.out_c.has_string_literal( '-%c requires an argument\\n' )
        assert self.out_c.has_string_literal( '/use/local/lib/sgreprc' )
        assert self.out_c.has_string_literal( '0.99' )
        assert self.out_c.has_string_literal( '<input exceeded>' )
        assert self.out_c.has_string_literal( '<stdin>' )
        assert self.out_c.has_string_literal( 'ACsearch' )
        assert self.out_c.has_string_literal( 'Aug 28 2014' )
        assert self.out_c.has_string_literal( 'Basic expression expected\\n' )
        assert self.out_c.has_string_literal( "Can't read input from stdin, it's already used\\n" )
        assert self.out_c.has_string_literal( 'Command file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'Copyright (C) 1996  University of Helsinki' )
        assert self.out_c.has_string_literal( 'Either you have forgotten the quote  at the end of phrase or' )
        assert self.out_c.has_string_literal( 'Empty command file %s\\n' )
        assert self.out_c.has_string_literal( 'Empty stdin\\n' )
        assert self.out_c.has_string_literal( 'Empty style file %s\\n' )
        assert self.out_c.has_string_literal( 'Expression too long (>%d)\\n' )
        assert self.out_c.has_string_literal( 'File %s truncated before search\\n' )
        assert self.out_c.has_string_literal( 'HOME' )
        assert self.out_c.has_string_literal( 'If no files are given stdin is used instead.' )
        assert self.out_c.has_string_literal( 'Illegal option -%c\\n' )
        assert self.out_c.has_string_literal( 'Inbuilt preprocessor not implemented yet.\\n' )
        assert self.out_c.has_string_literal( 'Invalid SGREPOPT (SGREPOPT=%s)\\n' )
        assert self.out_c.has_string_literal( 'Memory allocation failed.\\n' )
        assert self.out_c.has_string_literal( 'Memory:\\n %dK memory allocated, %d realloc operations\\n' )
        assert self.out_c.has_string_literal( 'No files or expressions allowed in SGREPOPT\\n' )
        assert self.out_c.has_string_literal( 'No valid files\\n' )
        assert self.out_c.has_string_literal( 'Operations:\\n%15s:%-4d%6s:%-4d%5s:%-4d%5s:%-4d%11s:%-4d%3s:%-4d\\n' )
        assert self.out_c.has_string_literal( 'Operator tree size was %d, optimized %d\\n' )
        assert self.out_c.has_string_literal( 'Options can also be specified with SGREPOPT environment variable' )
        assert self.out_c.has_string_literal( 'Output list size was %d regions.\\n' )
        assert self.out_c.has_string_literal( 'Parse error on line %d column %d :\\n\\t%s\\n%s\\n' )
        assert self.out_c.has_string_literal( 'Phrase length exceeds' )
        assert self.out_c.has_string_literal( "Premature end of parsing. ( This shouldn't happen!! )\\n" )
        assert self.out_c.has_string_literal( 'Read command file' )
        assert self.out_c.has_string_literal( 'SGREPOPT' )
        assert self.out_c.has_string_literal( 'Scanned %d files, having total of %dK size finding %d phrases.\\n' )
        assert self.out_c.has_string_literal( 'Short write to tempfile\\n' )
        assert self.out_c.has_string_literal( "Stdin already read, Can't read expressions from stdin\\n" )
        assert self.out_c.has_string_literal( 'Strange expression type\\n' )
        assert self.out_c.has_string_literal( 'Things done:\\n %d %s, %d %s, %d %s\\n %d %s, %d %s\\n' )
        assert self.out_c.has_string_literal( 'Too complex SGREPOPT\\n' )
        assert self.out_c.has_string_literal( 'Unsupported operation in parse tree (%d)\\n' )
        assert self.out_c.has_string_literal( "Usage: sgrep <options> 'region expression' [<files...>]" )
        assert self.out_c.has_string_literal( 'Usage: sgrep [ -' )
        assert self.out_c.has_string_literal( 'Warning: region end point greater than input size detected\\n' )
        assert self.out_c.has_string_literal( 'Warning: region start point greater than input size detected\\n' )
        assert self.out_c.has_string_literal( "You have to give an expression line if you don't use -f or -e switch.\\n" )
        assert self.out_c.has_string_literal( '\\nCopyright (C) 1996 University of Helsinki. Use sgrep -C for details,\\n' )
        assert self.out_c.has_string_literal( '\\noptions are:' )
        assert self.out_c.has_string_literal( '\\t%s\\n' )
        assert self.out_c.has_string_literal( '\\t-%c %s\\t%s\\n' )
        assert self.out_c.has_string_literal( '\\t--\\t\\tno more options' )
        assert self.out_c.has_string_literal( '_quote' )
        assert self.out_c.has_string_literal( '_quote_' )
        assert self.out_c.has_string_literal( 'add_parents' )
        assert self.out_c.has_string_literal( 'bin_file_search' )
        assert self.out_c.has_string_literal( 'c->length==0 && c->last==c->first' )
        assert self.out_c.has_string_literal( 'c_reg.start<inner_stack[inq_ind-1].start || c_reg.end>inner_stack[inq_ind-1].end' )
        assert self.out_c.has_string_literal( 'common.c' )
        assert self.out_c.has_string_literal( 'comp_tree_nodes' )
        assert self.out_c.has_string_literal( 'concat' )
        assert self.out_c.has_string_literal( 'constant gc list must be sorted' )
        assert self.out_c.has_string_literal( 'containing' )
        assert self.out_c.has_string_literal( 'create_reference_counters' )
        assert self.out_c.has_string_literal( 'creating tempfile: open' )
        assert self.out_c.has_string_literal( 'dad->left!=((void *)0)' )
        assert self.out_c.has_string_literal( 'do_add_region' )
        assert self.out_c.has_string_literal( 'do_get_region' )
        assert self.out_c.has_string_literal( 'do_prev_region' )
        assert self.out_c.has_string_literal( 'equal' )
        assert self.out_c.has_string_literal( 'eval' )
        assert self.out_c.has_string_literal( 'eval.c' )
        assert self.out_c.has_string_literal( 'exprs>0' )
        assert self.out_c.has_string_literal( 'extracting' )
        assert self.out_c.has_string_literal( 'fork' )
        assert self.out_c.has_string_literal( 'free_tree_node' )
        assert self.out_c.has_string_literal( 'gc lists scanned' )
        assert self.out_c.has_string_literal( 'gc_lists_now<=4' )
        assert self.out_c.has_string_literal( 'gc_lists_now==stats.constant_lists' )
        assert self.out_c.has_string_literal( 'handle->ind<=( 1 << 7 )' )
        assert self.out_c.has_string_literal( 'handle->ind>=0' )
        assert self.out_c.has_string_literal( 'handle->list->last->next==((void *)0)' )
        assert self.out_c.has_string_literal( 'handle->list->length<=( 1 << 7 )' )
        assert self.out_c.has_string_literal( 'handle->list->length>=0' )
        assert self.out_c.has_string_literal( 'handle->node!=((void *)0)' )
        assert self.out_c.has_string_literal( 'in' )
        assert self.out_c.has_string_literal( 'inner' )
        assert self.out_c.has_string_literal( 'invalid constant region list' )
        assert self.out_c.has_string_literal( 'join' )
        assert self.out_c.has_string_literal( 'join expected comma: join(NUMBER,expression)' )
        assert self.out_c.has_string_literal( 'join needs a number: join(NUMBER,expression)' )
        assert self.out_c.has_string_literal( 'join number must be >= 1' )
        assert self.out_c.has_string_literal( 'l->first!=((void *)0)' )
        assert self.out_c.has_string_literal( 'l->last->list[l->length-1].start!=s || l->last->list[l->length-1].end<e' )
        #assert self.out_c.has_string_literal( 'l->last->list[l->length-1].start<=s' )
        assert self.out_c.has_string_literal( 'l->last->next==((void *)0)' )
        assert self.out_c.has_string_literal( 'l->length<=( 1 << 7 )' )
        assert self.out_c.has_string_literal( 'l->length==0 || !l->sorted || l->end_sorted|| l->nested || e>l->last->list[l->length-1].end' )
        assert self.out_c.has_string_literal( 'l->length>=0' )
        assert self.out_c.has_string_literal( 'lseek %s: %s\\n' )
        assert self.out_c.has_string_literal( 'lseek <stdin>' )
        assert self.out_c.has_string_literal( 'lseek style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'main.c' )
        assert self.out_c.has_string_literal( 'node->GC_list->refcount>=0 || node->GC_list->refcount==-1' )
        assert self.out_c.has_string_literal( 'node->label_right==-1' )
        assert self.out_c.has_string_literal( 'node->left!=((void *)0)' )
        assert self.out_c.has_string_literal( 'not containing' )
        assert self.out_c.has_string_literal( 'not equal' )
        assert self.out_c.has_string_literal( 'not in' )
        assert self.out_c.has_string_literal( 'number>0' )
        assert self.out_c.has_string_literal( 'on line' )
        assert self.out_c.has_string_literal( 'op->phrase->GC_list!=((void *)0)' )
        assert self.out_c.has_string_literal( 'open %s: %s\\n' )
        assert self.out_c.has_string_literal( 'open style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'optimize.c' )
        assert self.out_c.has_string_literal( 'or' )
        assert self.out_c.has_string_literal( 'order' )
        assert self.out_c.has_string_literal( 'outer' )
        assert self.out_c.has_string_literal( 'output.c' )
        assert self.out_c.has_string_literal( 'pmatch.c' )
        assert self.out_c.has_string_literal( 'pn->parent!=((void *)0)' )
        assert self.out_c.has_string_literal( 'pn->parent->label_left==4' )
        assert self.out_c.has_string_literal( 'quote' )
        assert self.out_c.has_string_literal( 'quote_' )
        assert self.out_c.has_string_literal( 'r.node!=((void *)0)' )
        assert self.out_c.has_string_literal( 'read %s: %s\\n' )
        assert self.out_c.has_string_literal( 'read <stdin>' )
        assert self.out_c.has_string_literal( 'read style file %s : %s\\n' )
        assert self.out_c.has_string_literal( 'read_expressions' )
        assert self.out_c.has_string_literal( 'real_eval' )
        assert self.out_c.has_string_literal( 'reg1.end<reg2.end' )
        assert self.out_c.has_string_literal( 'region end point must be greater than start point' )
        assert self.out_c.has_string_literal( 'regions created' )
        assert self.out_c.has_string_literal( 'regions scanned' )
        assert self.out_c.has_string_literal( 'remove_duplicate_phrases' )
        assert self.out_c.has_string_literal( 'remove_duplicates' )
        assert self.out_c.has_string_literal( 'root->leaf->GC_list!=((void *)0)' )
        assert self.out_c.has_string_literal( 'root->left!=((void *)0)' )
        assert self.out_c.has_string_literal( 'root->oper!=INVALID' )
        assert self.out_c.has_string_literal( 'root->refcount>=0 || root->refcount==-1' )
        assert self.out_c.has_string_literal( 'run_one_by_one' )
        assert self.out_c.has_string_literal( 'run_stream' )
        assert self.out_c.has_string_literal( 's<=(end_list->first->list[0].end)' )
        assert self.out_c.has_string_literal( 's<=e' )
        assert self.out_c.has_string_literal( 'searching phrases %d%% done\\r' )
        assert self.out_c.has_string_literal( 'sgrep -h for help\\n' )
        assert self.out_c.has_string_literal( 'sgrep time usage' )
        assert self.out_c.has_string_literal( 'sgrep version %s compiled at %s\\n' )
        assert self.out_c.has_string_literal( 'sgrep version 0.99 - search a file for structured pattern' )
        assert self.out_c.has_string_literal( 'sgrep warning: unlinking temp file failed' )
        assert self.out_c.has_string_literal( 'sgrep: %s: %s\\n' )
        assert self.out_c.has_string_literal( 'sgrep: lseek tmpfile' )
        assert self.out_c.has_string_literal( 'short read <stdin>' )
        assert self.out_c.has_string_literal( 'shrink_tree' )
        assert self.out_c.has_string_literal( 'sorts by end point' )
        assert self.out_c.has_string_literal( 'sorts by start point' )
        assert self.out_c.has_string_literal( 'start_region_search' )
        assert self.out_c.has_string_literal( 'sys' )
        assert self.out_c.has_string_literal( 'to_chars' )
        assert self.out_c.has_string_literal( 'too many expressions. (-e and -f options more than %d)\\n' )
        assert self.out_c.has_string_literal( 'total' )
        assert self.out_c.has_string_literal( 'usr' )
        assert self.out_c.has_string_literal( 'you have to recompile with greater MAX_PHRASE_LENGTH.' )
        assert self.out_c.has_string_literal( '                                    \\r' )
        assert self.out_c.has_string_literal( 'r1.start!=-1' )
        assert self.out_c.has_string_literal( 'tmpp.ind==tmp->length && tmpp.node->next==((void *)0)' )

    # Currently detected functions which have their named (from symbols) counterparts in not-stripped binary.
    #
    def test_check_for_all_currently_detected_functions(self):
        assert self.out_c.has_func( 'function_80488d4' )  # _init
        assert self.out_c.has_func( 'entry_point' )  # _start
        assert self.out_c.has_func( 'function_8048b90' )  # __x86_get_pc_thunk_bx
        assert self.out_c.has_func( 'function_8048ba0' )  # deregister_tm_clones
        assert self.out_c.has_func( 'function_8048bd0' )  # register_tm_clones
        assert self.out_c.has_func( 'function_8048c10' )  #
        assert self.out_c.has_func( 'function_8048c70' )  # frame_dummy
        assert self.out_c.has_func( 'function_8048ca0' )  # run_one_by_one
        assert self.out_c.has_func( 'function_8048f9f' )  # run_stream
        assert self.out_c.has_func( 'function_80490b3' )  # print_help
        assert self.out_c.has_func( 'function_8049151' )  # create_constant_lists
        assert self.out_c.has_func( 'function_80491bb' )  # get_arg
        assert self.out_c.has_func( 'function_804925b' )  # add_command
        assert self.out_c.has_func( 'function_80492f3' )  # read_com_file
        assert self.out_c.has_func( 'function_8049491' )  # read_expressions
        assert self.out_c.has_func( 'function_8049588' )  # read_style_file
        assert self.out_c.has_func( 'function_8049701' )  # clear_stats
        assert self.out_c.has_func( 'function_8049717' )  # show_stats
        assert self.out_c.has_func( 'function_8049a6d' )  # calc_time
        assert self.out_c.has_func( 'function_8049a88' )  # print_time
        assert self.out_c.has_func( 'function_8049af4' )  # show_times
        assert self.out_c.has_func( 'function_8049c1b' )  # read_stdin
        assert self.out_c.has_func( 'function_8049e44' )  # check_files
        assert self.out_c.has_func( 'function_8049ff7' )  # copyright_notice
        assert self.out_c.has_func( 'function_804a02d' )  # get_options
        assert self.out_c.has_func( 'function_804a3b8' )  # environ_options
        assert self.out_c.has_func( 'function_804a974' )  # preprocess
        assert self.out_c.has_func( 'function_804ab00' )  # e_malloc
        assert self.out_c.has_func( 'function_804ab50' )  # e_realloc
        assert self.out_c.has_func( 'function_804abb9' )  # new_string
        assert self.out_c.has_func( 'function_804abde' )  # init_string
        assert self.out_c.has_func( 'function_804ac24' )  #
        assert self.out_c.has_func( 'function_804ac5d' )  #
        assert self.out_c.has_func( 'function_804acb5' )  #
        assert self.out_c.has_func( 'function_804acff' )  #
        assert self.out_c.has_func( 'function_804ad8b' )  #
        assert self.out_c.has_func( 'function_804af4d' )  #
        assert self.out_c.has_func( 'function_804affc' )  #
        assert self.out_c.has_func( 'function_804b13d' )  #
        assert self.out_c.has_func( 'function_804b2f2' )  #
        assert self.out_c.has_func( 'function_804b328' )  #
        assert self.out_c.has_func( 'function_804b367' )  #
        assert self.out_c.has_func( 'function_804b537' )  #
        assert self.out_c.has_func( 'function_804b5af' )  #
        assert self.out_c.has_func( 'function_804b627' )  # give_oper_name
        assert self.out_c.has_func( 'function_804b6a9' )  #
        assert self.out_c.has_func( 'function_804b820' )  #
        assert self.out_c.has_func( 'function_804b86d' )  #
        assert self.out_c.has_func( 'function_804b9ae' )  #
        assert self.out_c.has_func( 'function_804bf78' )  #
        assert self.out_c.has_func( 'function_804bfd0' )  #
        assert self.out_c.has_func( 'function_804c006' )  #
        assert self.out_c.has_func( 'function_804c17b' )  #
        assert self.out_c.has_func( 'function_804c344' )  #
        assert self.out_c.has_func( 'function_804c39c' )  #
        assert self.out_c.has_func( 'function_804c6ac' )  #
        assert self.out_c.has_func( 'function_804c750' )  #
        assert self.out_c.has_func( 'function_804c80b' )  #
        assert self.out_c.has_func( 'function_804c8bf' )  #
        assert self.out_c.has_func( 'function_804ca23' )  #
        assert self.out_c.has_func( 'function_804cac6' )  #
        assert self.out_c.has_func( 'function_804cb20' )  #
        assert self.out_c.has_func( 'function_804cb4b' )  #
        assert self.out_c.has_func( 'function_804cd38' )  #
        assert self.out_c.has_func( 'function_804cdcd' )  #
        assert self.out_c.has_func( 'function_804ce20' )  #
        assert self.out_c.has_func( 'function_804cfef' )  #
        assert self.out_c.has_func( 'function_804d04d' )  #
        assert self.out_c.has_func( 'function_804d09a' )  #
        assert self.out_c.has_func( 'function_804d176' )  #
        assert self.out_c.has_func( 'function_804d1c1' )  #
        assert self.out_c.has_func( 'function_804d2d7' )  #
        assert self.out_c.has_func( 'function_804d550' )  #
        assert self.out_c.has_func( 'function_804d5d7' )  #
        assert self.out_c.has_func( 'function_804d622' )  #
        assert self.out_c.has_func( 'function_804d766' )  #
        assert self.out_c.has_func( 'function_804d878' )  #
        assert self.out_c.has_func( 'function_804db5c' )  #
        assert self.out_c.has_func( 'function_804dd48' )  #
        assert self.out_c.has_func( 'function_804e1ea' )  #
        assert self.out_c.has_func( 'function_804e4a6' )  #
        assert self.out_c.has_func( 'function_804e792' )  #
        assert self.out_c.has_func( 'function_804ead2' )  #
        assert self.out_c.has_func( 'function_804ebe9' )  #
        assert self.out_c.has_func( 'function_804ef8f' )  #
        assert self.out_c.has_func( 'function_804f177' )  #
        assert self.out_c.has_func( 'function_804f3ef' )  #
        assert self.out_c.has_func( 'function_804f586' )  #
        assert self.out_c.has_func( 'function_804f740' )  #
        assert self.out_c.has_func( 'function_804f9d6' )  #
        assert self.out_c.has_func( 'function_804fa9e' )  #
        assert self.out_c.has_func( 'function_804fb37' )  #
        assert self.out_c.has_func( 'function_804fbcc' )  #
        assert self.out_c.has_func( 'function_804fdc6' )  #
        assert self.out_c.has_func( 'function_804ff02' )  #
        assert self.out_c.has_func( 'function_80501c0' )  #
        assert self.out_c.has_func( 'function_804a51a' )  # main
        assert self.out_c.has_func( 'function_804aa50' )  # end_first
        assert self.out_c.has_func( 'function_804aaa8' )  # start_first
        assert self.out_c.has_func( 'function_8050140' )  # __libc_csu_init
        #assert self.out_c.has_func( 'function_80501b0' )  # __libc_csu_fini
