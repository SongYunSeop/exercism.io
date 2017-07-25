def is_pangram(txt):
    import re
    txt = re.sub(r'[^a-zA-Z]', '', txt.lower())

    return len(set([x for x in txt])) == 26
