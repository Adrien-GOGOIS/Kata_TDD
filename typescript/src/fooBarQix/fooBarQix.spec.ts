const fooBarQixConverter = (integer: number): string => {
	let result = '';
	
	if (integer % 3 === 0) {
		result += "foo";
	}
	if (integer % 5 === 0) {
		result += "bar";
	}
	if (integer % 7 === 0) {
		result += "qix";
	}

	const splittedInteger = integer.toString().split('')
	for (const number of splittedInteger) {
		if (number === '3') {
			result += "foo"
		}
		if (number === '5') {
			result += "bar"
		}
		if (number === '7') {
			result += "qix"
		}
	}

	if (result === '') {
		return integer.toString();
	}

	return result;
}

describe('FooBarQix testing', () => {
	it.each([
		[1, '1'],
		[2, '2'],
		[6, 'foo'],
		[9, 'foo'],
		[10, 'bar'],
		[14, 'qix'],
		[15, 'foobarbar'],
		[21, 'fooqix'],
		[35, 'barqixfoobar'],
		[105, 'foobarqixbar'],
		[3, 'foofoo'],
		[5, 'barbar'],
		[7, 'qixqix'],
	]) ("The interger %d should be '%s'", (integer, out) => {
		expect(fooBarQixConverter(integer)).toBe(out);
	  });
})