import re

def rotate(txt, rotate):
    is_lowercase = re.compile(r'[a-z]')
    is_uppercase = re.compile(r'[A-Z]')

    def convert(char):
        offset = rotate % 26
        if re.match(is_lowercase, char):
            first = ord('a')
            last = ord('z')
            return chr(ord(char) + offset) if ord(char) + offset <= last else chr(ord(char) + offset - 26)
        elif re.match(is_uppercase, char):
            first = ord('A')
            last = ord('Z')
            return chr(ord(char) + offset) if ord(char) + offset <= last else chr(ord(char) + offset - 26)
        else:
            return char

    return ''.join([convert(char) for char in txt])
