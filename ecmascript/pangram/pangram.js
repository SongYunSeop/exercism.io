class Pangram {
	constructor(sentence) {
		// convert sentence lower case & remove non alphabet
		this.sentence = sentence.toLowerCase().replace(/[^a-z]/g,'');
	}

	isPangram() {
		return new Set(this.sentence.split('')).size == 26
	}
}

export default Pangram;
