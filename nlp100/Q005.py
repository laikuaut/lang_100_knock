# config: utf-8

import re

def Q_005_1(n):
    """ 05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    文字bi-gramを処理
    """

    input_str = "I am an NLPer"
    return ngram(input_str, n)

def Q_005_2(n):
    """ 05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    単語bi-gramを処理
    """

    input_str = "I am an NLPer"
    word_list = [word for word in re.split(r'\W+', input_str) if len(word) > 0]
    return ngram(word_list, n)

def ngram(input, n):
    last = len(input) - n + 1
    return [input[i:i+n] for i in range(0, last)]

