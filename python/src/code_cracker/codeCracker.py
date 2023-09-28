class CodeCracker:
	CODE = {
		'!': 'a',
		')': 'b',
		'"': 'c',
		'(': 'd',
		'£': 'e',
		'*': 'f',
		'%': 'g',
		'&': 'h',
		'>': 'i',
		'<': 'j',
		'@': 'k' 
	}
	def decode(self, letter: str) -> str:
		if ord(letter) >= 97:
			return chr(ord(letter) + 11)
		return self.CODE[letter]