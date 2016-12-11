# coding: utf-8

from .mecab_read import read_mecab_data
from collections import defaultdict

def Q_036():
    """ 36. 単語の出現頻度
    文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
    """

    data = read_mecab_data('data/neko.txt.mecab')
    noun_phrase_set = defaultdict(lambda: 0)
    for sent in data:
        for word in sent:
            noun_phrase_set[word['surface']] += 1

    return [(k, v) for k, v in sorted(noun_phrase_set.items(), key=lambda x:x[1], reverse=True)]

