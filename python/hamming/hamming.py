def distance(left, right):

    if len(left) != len(right):
        raise ValueError()

    add = lambda x, y: x + y
    not_equal = lambda x, y: x != y 

    return reduce(add, map(not_equal, left, right), 0)
