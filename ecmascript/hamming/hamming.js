
class Hamming {
  compute(left, right) {
    if (left.length != right.length) {
      throw new Error('DNA strands must be of equal length.');
    }
    const leftArray = left.split("")
    const rightArray = right.split("")
    return leftArray.filter((s, i) => {return s != rightArray[i]}).length

  }
}

export default Hamming
