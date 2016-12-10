# coding: utf-8

from .mecab_read import read_mecab_data

def Q_031():
    """ 31. 動詞
    動詞の表層形をすべて抽出せよ．
    """

    data = read_mecab_data('data/neko.txt.mecab')
    verb_set = set()
    for sent in data:
        for word in sent:
            if word['pos'] == '動詞':
                verb_set.add(word['surface'])

    return verb_set
