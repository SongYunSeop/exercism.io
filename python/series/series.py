def slices(series, length):
    if length == 0 or len(series) < length:
        raise ValueError()
    return [[int(y) for y in list(series[x:x+length])] for x in range(len(series) - length + 1)]
