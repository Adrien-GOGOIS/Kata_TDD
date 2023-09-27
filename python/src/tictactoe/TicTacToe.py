from collections import namedtuple
from Player import Player

class TicTacToe:
	playedCases = []
	equality = False
	winner: Player | None = None
	__lastPlayer: Player

	def __init__(self, player_1: Player, player_2: Player):
		self.player_1 = player_1
		self.player_2 = player_2
		self.playedCases = ["."] * 9

	def play(self, player: Player, position: int) -> bool:
		self.__lastPlayer = player
		if (self.playedCases[position] != "."):
			return False

		self.playedCases[position] = player.symbol

		if self.__isWon(self.__lastPlayer.symbol):
			self.winner = self.__lastPlayer

		if not '.' in self.playedCases:
			self.equality = True
			
		return True
		
	
	def __isWon(self, symbol: str) -> bool:
		if (
			self.playedCases[0] == symbol and self.playedCases[1] == symbol and self.playedCases[2] == symbol
			) or (
			self.playedCases[3] == symbol and self.playedCases[4] == symbol and self.playedCases[5] == symbol
			) or (
			self.playedCases[6] == symbol and self.playedCases[7] == symbol and self.playedCases[8] == symbol
			) or (
			self.playedCases[0] == symbol and self.playedCases[3] == symbol and self.playedCases[6] == symbol
			) or (
			self.playedCases[1] == symbol and self.playedCases[4] == symbol and self.playedCases[7] == symbol
			) or (
			self.playedCases[2] == symbol and self.playedCases[5] == symbol and self.playedCases[8] == symbol
			) or (
			self.playedCases[0] == symbol and self.playedCases[4] == symbol and self.playedCases[8] == symbol
			) or (
			self.playedCases[2] == symbol and self.playedCases[4] == symbol and self.playedCases[6] == symbol
			):
			return True
		return False