//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

class Bob {

	constructor() {
		this.QUESTION_ANSWER = 'Sure.';
		this.YELLING_ANSWER = 'Whoa, chill out!';
		this.BLANK_ANSWER = 'Fine. Be that way!';
		this.DEFAULT_ANSWER = "Whatever.";
	}

	isQuestion(message) {
		return message.slice(-1) == '?'
	}

	isYELLING(message) {
		return message == message.toUpperCase() && message !== message.toLowerCase()
	}

	hey(message) {
		//
		// YOUR CODE GOES HERE
		//
		message = message.trim()
		if (message === '') return this.BLANK_ANSWER
		if (this.isYELLING(message)) return this.YELLING_ANSWER
		if (this.isQuestion(message)) return this.QUESTION_ANSWER
		return this.DEFAULT_ANSWER


	}
}

export default Bob;
