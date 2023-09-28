from codeCracker import CodeCracker

class TestCodeCracker:
	game = CodeCracker()

	def test_exclamation_mark_should_return_A(self):
		assert(self.game.decode('!')) == 'a'

	def test_a_should_return_l(self):
		assert(self.game.decode('a')) == 'l'

	def test_o_should_return_z(self):
		assert(self.game.decode('o')) == 'z'

	def test_b_should_return_closing(self):
		assert(self.game.decode(')')) == 'b'

	def test_d_should_return_opening(self):
		assert(self.game.decode('(')) == 'd'

	def test_d_should_return_opening(self):
		assert(self.game.decode('@')) == 'k'

