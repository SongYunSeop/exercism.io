import re


def verify(isbn):
    regex = r'^\d-?\d{3}-?\d{5}-?[\d|X]$'

    if not re.match(regex, isbn):
        return False
    else:
        if sum([(10 - idx) * int(x if x != 'X' else 10)
                for idx, x in enumerate(isbn.replace('-', ''))]) % 11 == 0:
            return True
        else:
            return False
