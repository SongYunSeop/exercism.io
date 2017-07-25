def is_isogram(txt):
    import re
    txt = re.sub(r'[^a-zA-Z]', '', txt.lower())

    return len(txt) == len(set([x for x in txt]))
