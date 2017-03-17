const dna2Rna = {
  "G": "C",
  "C": "G",
  "T": "A",
  "A":"U"
}

class Transcriptor {

  toRna(dna){
    return dna.split("").map((x) => {
      if (!dna2Rna[x])
        throw new Error('Invalid input DNA.')
      return dna2Rna[x]
    }).join('')
  }
}

export default Transcriptor
