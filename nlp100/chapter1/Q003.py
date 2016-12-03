# coding: utf-8

import re

def Q_003():
    """ 03. 円周率
    "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """

    # 単語の文字数が円周率=3.14159265358979になっている
    input_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    word_list = word_split(input_str)
    return [len(word) for word in word_list]

def word_split(sent, regex=r'\W+'):
    """ 単語分割
    単語ごとに分割した文字列リストを作成する
    """
    return [word for word in re.split(regex, sent) if len(word) > 0]
