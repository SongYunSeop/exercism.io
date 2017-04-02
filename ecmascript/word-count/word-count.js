class Words {
	constructor() {

	}

	count(words) {
		words = words.toLowerCase();
		const wordCount = {}
		const wordList = words.split(/\s/);
		for (let word of wordList) {
			if (word == '') continue;
			if (wordCount.hasOwnProperty(word)) wordCount[word] += 1;
			else wordCount[word] = 1;
		}
		return wordCount;
	}
}

export default Words;
