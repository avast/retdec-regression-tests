from regression_tests import *

class Test(Test):
    settings = TestSettings(
        input='x86-elf-1d991da0b51196786c6e3e8843435d6e',
        args='-k'
    )

    def test_atexit_calls_arguments_are_not_strings(self):
        pass
        #assert self.out_c.contains('__cxa_atexit\(.*0x804b138.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_ZN5boost4asio5error6detail14netdb_categoryD1Ev.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_ZN5boost4asio5error6detail17addrinfo_categoryD1Ev.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_ZN5boost4asio5error6detail12ssl_categoryD1Ev.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id_1.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id_2.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id_3.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id_4.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id_5.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id_6.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_service_id_7.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_destructor_tss_ptr.*\)')
        #assert self.out_c.contains('__cxa_atexit\(.*_ZN5boost4asio5error6detail13misc_categoryD1Ev.*\)')
