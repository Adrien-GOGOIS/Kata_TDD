const ARABIC_TO_ROMAN = {
	'M': 1000,
	'CM': 900,
	'D': 500,
	'CD': 400,
	'C': 100,
	'XC': 90,
	'L': 50,
	'XL': 40,
	'X': 10,
	'IX': 9,
	'V': 5,
	'IV': 4,
	'I': 1,
}

const arabicToRoman = (arabicNumber: number): string => {
	for (const [key, value] of Object.entries(ARABIC_TO_ROMAN)) {
			if (arabicNumber >= value) {
				return key + arabicToRoman(arabicNumber - value)
			}
		}
	return ''
}

describe('Parameterized test', () => {
	it.each([
		[0, ''],
		[1, 'I'],
		[2, 'II'],
		[3, 'III'],
		[4, 'IV'],
		[5, 'V'],
		[6, 'VI'],
		[7, "VII"],
		[8, "VIII"],
		[9, "IX"],
		[50, "L"],
		[98, "XCVIII"],
		[598, "DXCVIII"],
		[1988, "MCMLXXXVIII"],
		[23, "XXIII"],
		[10347, "MMMMMMMMMMCCCXLVII"]
	]) ("Arabic number %d should be '%s' in roman", (arabicNumber, roman) => {
		expect(arabicToRoman(arabicNumber)).toBe(roman);
	  });
})
