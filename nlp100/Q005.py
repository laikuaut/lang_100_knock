# coding: utf-8

from . import Q003

def Q_005_1(n):
    """ 05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
    この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    文字bi-gramを処理
    """

    input_str = "I am an NLPer"
    return ngram(input_str, n)

def Q_005_2(n):
    """ 05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
    この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    単語bi-gramを処理
    """

    input_str = "I am an NLPer"
    word_list = Q003.word_split(input_str)
    return ngram(word_list, n)

def ngram(input, n):
    """ Ngram取得
    入力変数を指定のgram数でngramリストを作成する
    """
    last = len(input) - n + 1
    return [input[i:i+n] for i in range(0, last)]

