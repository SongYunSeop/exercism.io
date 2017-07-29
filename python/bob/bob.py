def hey(txt):

    QUESTION_ANSWER = 'Sure.'
    YELL_ANSWER = 'Whoa, chill out!'
    BLANK_ANSWER = 'Fine. Be that way!'
    DEFAULT_ANSWER = 'Whatever.'

    is_question = lambda x: x[-1] == '?'

    is_yelling = lambda x: x == x.upper() and x != x.lower()

    is_blank = lambda x: x == ''

    txt = txt.strip()
    
    if is_blank(txt):
        return BLANK_ANSWER
    elif is_yelling(txt):
        return YELL_ANSWER
    elif is_question(txt):
        return QUESTION_ANSWER
    else:
        return DEFAULT_ANSWER
    

    
