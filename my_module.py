def count_fre_word(text:str)->dict:
    '''docstring'''
    words = text.split()
    fre_words = {}
    for w in words:
        if w in fre_words:
            fre_words[w] += 1
        else:
            fre_words[w] = 1
    return fre_words

DATA = ['Hello LAEM', {"score":[6,5,4,5,4,9]}]

print('your module is imported')