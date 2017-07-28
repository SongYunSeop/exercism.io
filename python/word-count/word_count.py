def word_count(txt):
    import re
    word_list = re.split('[\.\,\_\s]', re.sub('[^0-9a-zA-Z\,\_\\s]', '',txt.lower()))
    result = {}
    for word in word_list:
        if word == '':
            continue
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result
    
