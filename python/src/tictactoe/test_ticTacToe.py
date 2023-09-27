from TicTacToe import TicTacToe
from Player import Player

class TestTicTacToe:
	player_1 = Player("X")
	player_2 = Player("O")
	
	def test_game_begin_with_empty_grid(self):
		game = TicTacToe(self.player_1, self.player_2)
		assert len(game.playedCases) is 9
		assert game.playedCases == [
			'.', '.', '.', 
			'.', '.', '.', 
			'.', '.', '.'
			]

	def test_game_accept_any_case_at_beginning(self):
		game = TicTacToe(self.player_1, self.player_2)
		assert game.play(self.player_1, 2) is True
		assert game.playedCases[2] is "X"
		assert game.winner() is None
		assert game.playedCases == [
			'.', '.', 'X', 
			'.', '.', '.', 
			'.', '.', '.'
			]

	def test_should_not_accept_move_is_case_not_empty(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_1, 2)
		assert game.play(self.player_2, 2) is False
		assert game.playedCases[2] is "X"
		assert game.playedCases == [
			'.', '.', 'X', 
			'.', '.', '.', 
			'.', '.', '.'
			]

	def test_player_1_should_win_if_first_line_full_of_X(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_1, 0)
		game.play(self.player_1, 1)
		game.play(self.player_1, 2)
		assert game.playedCases == [
			'X', 'X', 'X', 
			'.', '.', '.', 
			'.', '.', '.'
			]
		assert game.winner() is self.player_1 

	def test_player_2_should_win_if_first_line_full_of_O(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_2, 0)
		game.play(self.player_2, 1)
		game.play(self.player_2, 2)
		assert game.playedCases == [
			'O', 'O', 'O', 
			'.', '.', '.', 
			'.', '.', '.'
			]
		assert game.winner() is self.player_2

	def test_player_1_should_win_if_second_line_full_of_X(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_1, 3)
		game.play(self.player_1, 4)
		game.play(self.player_1, 5)
		assert game.playedCases == [
			'.', '.', '.', 
			'X', 'X', 'X', 
			'.', '.', '.'
			]
		assert game.winner() is self.player_1 is self.player_1

	def test_player_1_should_win_if_third_line_full_of_X(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_1, 6)
		game.play(self.player_1, 7)
		game.play(self.player_1, 8)
		assert game.playedCases == [
			'.', '.', '.',  
			'.', '.', '.',
			'X', 'X', 'X'
			]
		assert game.winner() is self.player_1 is self.player_1

	def test_player_1_should_win_if_first_column_full_of_X(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_1, 0)
		game.play(self.player_1, 3)
		game.play(self.player_1, 6)
		assert game.playedCases == [
			'X', '.', '.',  
			'X', '.', '.',
			'X', '.', '.'
			]
		assert game.winner() is self.player_1 is self.player_1

	def test_player_1_should_win_if_third_column_full_of_X(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_1, 2)
		game.play(self.player_1, 5)
		game.play(self.player_1, 8)
		assert game.playedCases == [
			'.', '.', 'X',  
			'.', '.', 'X',
			'.', '.', 'X'
			]
		assert game.winner() is self.player_1 is self.player_1

	def test_player_2_should_win_if_first_diagonal_full_of_O(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_2, 0)
		game.play(self.player_2, 4)
		game.play(self.player_2, 8)
		assert game.playedCases == [
			'O', '.', '.',  
			'.', 'O', '.',
			'.', '.', 'O'
			]
		assert game.winner() is self.player_2 is self.player_2

	def test_player_2_should_win_if_second_diagonal_full_of_O(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_2, 2)
		game.play(self.player_2, 4)
		game.play(self.player_2, 6)
		assert game.playedCases == [
			'.', '.', 'O',  
			'.', 'O', '.',
			'O', '.', '.'
			]
		assert game.winner() is self.player_2 is self.player_2

	def test_play_a_full_game_with_player_1_winner(self):
		game = TicTacToe(self.player_1, self.player_2)
		game.play(self.player_1, 4)
		game.play(self.player_2, 0)
		game.play(self.player_1, 1)
		game.play(self.player_2, 7)
		game.play(self.player_1, 6)
		game.play(self.player_2, 8)
		game.play(self.player_1, 2)
		assert game.playedCases == [
			'O', 'X', 'X',  
			'.', 'X', '.',
			'X', 'O', 'O'
			]
		assert game.winner() is self.player_1 is self.player_1

if __name__ == 'main':
	unittest.main()