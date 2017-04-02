class PerfectNumbers {

	constructor() {
		this.PERFECT = 'perfect';
		this.ABUNDANT = 'abundant';
		this.DEFICIENT = 'deficient';
		this.INVALID_INPUT = 'Classification is only possible for natural numbers.';
	}

	aliquot(number) {
		const max = Math.ceil(Math.sqrt(number))
		const aliquotSet = [];
		for (let i = 2; i < max; i++) {
			if ( number % i == 0) aliquotSet.push(i);
		}
		return aliquotSet
	}

	classify(number) {
		if (number < 1) return this.INVALID_INPUT;

		const aliquotSet = this.aliquot(number);

		if (aliquotSet.length < 1) return this.DEFICIENT;

		const aliquotSum = aliquotSet.reduce((x,y) => {return x + y + number / y }, 1)

		if (aliquotSum == number) {
			return this.PERFECT;
		} else if (aliquotSum > number) {
			return this.ABUNDANT;
		} else if (aliquotSum < number) {
			return this.DEFICIENT;
		}
	}
}

export default PerfectNumbers;
