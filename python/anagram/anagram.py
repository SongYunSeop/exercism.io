import collections

def detect_anagrams(word, candidates):
    # word = word.lower()
    def generator_dict(txt):
        txt = txt.lower()
        anagram_dict = collections.defaultdict(int)
        for x in txt:
            anagram_dict[x] += 1
        return anagram_dict

    base_dict = generator_dict(word) 

    return [candidate for candidate in candidates if base_dict == generator_dict(candidate) and word.lower() != candidate.lower()]
