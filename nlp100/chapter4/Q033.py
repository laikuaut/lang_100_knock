# coding: utf-8

from .mecab_read import read_mecab_data

def Q_033():
    """ 33. サ変名詞
    サ変接続の名詞をすべて抽出せよ．
    """

    data = read_mecab_data('data/neko.txt.mecab')
    noun_set = set()
    for sent in data:
        for word in sent:
            if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':

                noun_set.add(word['surface'])

    return noun_set
