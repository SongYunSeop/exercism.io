class Pangram {
	constructor(sentence) {
		// convert sentence lower case & remove whitespace
		this.sentence = sentence.toLowerCase().replace(/\s/g,'');
	}

	isPangram() {
		if (this.sentence.length < 26) return false;

		const checkArr = new Array(26).fill(0);

		const aCode = 'a'.charCodeAt()
		const zCode = 'z'.charCodeAt()

		for(let s of this.sentence) {
			const code = s.charCodeAt()
			if (code < aCode || code > zCode) continue;
			checkArr[s.charCodeAt() - aCode] = 1
		}

		return checkArr.filter((e) => { return e == 1 }).length == 26
	}
}

export default Pangram;
