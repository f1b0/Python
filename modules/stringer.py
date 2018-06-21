#!/usr/bin/env python3.6
# -*- encoding: utf-8; py-indent-offset: 2 -*-


def stinger(input_string, ret=int()):
    """Returns a list(char_list,word_list,sentence,word_count,sentence_count)."""
    char = str()            # type: str
    char_list = []          # type: list
    word_list = []          # type: list
    sentence = []           # type: list
    char_count = int()      # type: int
    word_count = int()      # type: int
    sentence_count = int()  # type: int
    returner = [
        char_list,
        word_list,
        sentence,
        char_count,
        word_count,
        sentence_count
    ]

    for st in input_string:
        char_count -= 1
        if ' ' not in st:
            char += st
        elif ' ' in st:
            word_list.append(char)
            char = str()
            word_count += 1
        elif '.' in st:
            sentence.append(word_list)
            sentence_count += 1
            word_list = list()
    return returner[ret]


def stinger_search(input_string, pattern=str(), ret=int()):
    """Returns status as string in result[0], bool in result[1]."""
    returner = stinger(input_string, 0)
    res = ["Nothing found.", False]
    for x in returner:
        print(x)
        if pattern in x:
            res[0] = '[ ' + str(x) + ' ]' + ' found.'
            res[1] = True
    return res[ret]


if __name__ == '__main__':
    a_string = '''In this first video we are going to get started by taking a look at how the finished app should function. 
The idea is that we can use access any valid GitHub user's profile data, and our Symfony 3 web application 
will pull their profile and repository data in, and display it on the page.'''
    print(a_string)
    print(stinger_search(a_string, 'are', 0))
