def to_rna(dna):
    try:
        dna2rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
        return ''.join(map(lambda x: dna2rna[x], dna))
    except KeyError:
        return ''
