
from regression_tests import *

class Test(Test):
	settings = TestSettings(
		input='f79820d57ddef5d48a5f654105298707',
		args='-k',
	)

	def test_has_important_fncs(self):
		assert self.out_c.has_funcs('_start','ls_cmd','cat_cmd','ping_cmd','shell_cmd','lotto_cmd','sleep_cmd','quote_cmd','admin_cmd','run_cmd','create_sock','sock_print','tok_gen','shell','process_sock')

	def test_sock_print_return_send(self):
		#
		# back-end might decide to store result to temp var and return it instead of this direct send() return.
		#
		assert self.out_c.contains(r'return send\(sock')

	# Some of these are inside shell() functions, so check for their presence also checks for the shell()'s body.
	#
	def test_check_for_all_currently_detected_strings(self):
		assert self.out_c.has_string_literal( '.' )
		#assert self.out_c.has_string_literal( '\\n' )
		assert self.out_c.has_string_literal( 'Meow~\\n' )
		assert self.out_c.has_string_literal( 'ping -c 4 localhost' )
		assert self.out_c.has_string_literal( 'Ret: %d\\n' )
		assert self.out_c.has_string_literal( 'Dest  : %p\\n' )
		assert self.out_c.has_string_literal( '>Lotto Game<\\nPick a level between 1 and 4.\\n: ' )
		assert self.out_c.has_string_literal( 'Pick your lotto numbers!\\n' )
		assert self.out_c.has_string_literal( 'You win!\\n' )
		assert self.out_c.has_string_literal( 'You lose...\\nThe correct numbers were:\\n%u, %u, %u, %u\\n\\nBetter luck next time!\\n' )
		assert self.out_c.has_string_literal( '%s\\n' )
		assert self.out_c.has_string_literal( 'NO\\n' )
		assert self.out_c.has_string_literal( 'YES\\n' )
		assert self.out_c.has_string_literal( 'OK\\n' )
		assert self.out_c.has_string_literal( 'FAIL\\n' )
		assert self.out_c.has_string_literal( 'Username: ' )
		assert self.out_c.has_string_literal( 'root' )
		assert self.out_c.has_string_literal( 'key' )
		assert self.out_c.has_string_literal( 'Source: %p\\n' )
		assert self.out_c.has_string_literal( 'ish$ ' )
