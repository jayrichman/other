#!/usr/bin/env python

def pig_latin(sentence):

    vowels = 'aeiou'
    words = sentence.split()
    new_sentence = ''

    cntr = 1
    for word in words:
        if len(word) > 1 and word[0] in vowels:
            word = word[1:] + word[0]
        word += 'ni' + 'j'*cntr
        cntr += 1
        new_sentence += word + ' '

    return new_sentence.rstrip()

if __name__ == '__main__':

    print pig_latin("This is just a small sentence")
