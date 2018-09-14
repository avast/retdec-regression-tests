#
# Tests sample 00A299FD149939CEC860C71224B77209.
# Tests mainly detection of functions called by syscall, but also same other important things.
#

from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='00A2',
        args='-k'
    )

    # These are not all strings recognized in output, just some important/random.
    #
    def test_check_for_strings(self):
        assert self.out_c.has_string_literal('/cgi-bin/php')
        assert self.out_c.has_string_literal('/cgi-bin/php4')
        assert self.out_c.has_string_literal('arm')
        assert self.out_c.has_string_literal('x86')
        #assert self.out_c.has_string_literal('httpd')
        assert self.out_c.has_string_literal('/bin/sh')
        assert self.out_c.has_string_literal('/proc')
        assert self.out_c.has_string_literal('/var/run/.lightscan')
        assert self.out_c.has_string_literal('/var/run/pid')
        assert self.out_c.has_string_literal('/var/tmp/dreams.install.sh')
        assert self.out_c.has_string_literal('/usr/bin/-wget')
        assert self.out_c.has_string_literal('sig')
        assert self.out_c.has_string_literal('nodes')
        #assert self.out_c.has_string_literal('/proc/self/exe')
        assert self.out_c.has_string_literal('HTTP/1.1 200 OK')
        assert self.out_c.has_string_literal('rm -rf ')
        assert self.out_c.has_string_literal('echo -ne ')
        #assert self.out_c.contains(r'"admin"')
        #assert self.out_c.contains(r'"root"')
        #assert self.out_c.has_string_literal('/var/run/.zollard/')
        #assert self.out_c.has_string_literal('\\x53\\x83\\xec\\x08\\x8b\\x5c\\x24\\x10\\x8b\\x53\\x04\\x8b\\x03\\x89\\x02\\x85\\xc0\\x74\\x03\\x89\\x50\\x04\\x83\\xec\\x0c\\x8d\\x43\\x14\\x50\\xe8\\x75\\x0c')
        #assert self.out_c.has_string_literal('\\x55\\x57\\x56\\x53\\x83\\xec\\x0c\\x8b\\x6c\\x24\\x20\\x8b\\x7d\\x04\\x8b\\x75\\x08\\x8b\\x5d\\x0c\\x57\\x68')

    # Syscalled functions are added as linked and should be dumpped as comments in "External Functions" section.
    # Note: these are not all detected external functions.
    #
    def test_external_fncs_from_syscalls(self):
        assert self.out_c.has_comment_matching(r'.*int.*clone\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*int80_syscall\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*sigreturn\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*accept\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*bind\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*connect\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*execve\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*newfstat\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*listen\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*pipe\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*ssize_t.*sendto\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*int.*unlink\(.*\);')
        #assert self.out_c.has_comment_matching(r'.*ssize_t.*write\(.*\);')

    # Right now, we can not check if function X calls function Y, so we just check presence of functions calling syscalls.
    # All of these are in Hex-Rays as well.
    #
    def test_has_functions_using_syscalls(self):
        assert self.out_c.has_func( 'function_804a43c' ) # accept()
        assert self.out_c.has_func( 'function_8049ae6' ) # bind()
        assert self.out_c.has_func( 'function_804a656' ) # connect()
        assert self.out_c.has_func( 'function_80485da' ) # execve()
        assert self.out_c.has_func( 'function_8049b52' ) # newfstat()
        assert self.out_c.has_func( 'function_8049b34' ) # listen()
        assert self.out_c.has_func( 'function_8054b75' ) # pipe()
        assert self.out_c.has_func( 'function_804b0fe' ) # sendto()
        assert self.out_c.has_func( 'function_8048960' ) # unlink()
        assert self.out_c.has_func( 'function_80558c0' ) # write()
