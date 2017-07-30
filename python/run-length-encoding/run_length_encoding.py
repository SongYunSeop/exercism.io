def decode(txt):
    import re
    decoder = lambda x, y: x + ((y[-1] * int(y[:-1]))  if len(y) > 1 else y)
    return reduce(decoder, [x.group(0) for x in re.finditer('\d*(\w|\s)',txt)], '')
    


def encode(txt):
    import re
    char_list = [x.group(0) for x in re.finditer(r'(\s|\w)\1*', txt)]

    encoder = lambda x, y: x + (str(len(y)) + y[0] if len(y) > 1 else y[0])
    return reduce(encoder, char_list, '')
