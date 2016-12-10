# coding: utf-8

from .mecab_read import read_mecab_data

def Q_032():
    """ 32. 動詞の原形
    動詞の原形をすべて抽出せよ．
    """

    data = read_mecab_data('data/neko.txt.mecab')
    verb_base_set = set()
    for sent in data:
        for word in sent:
            if word['pos'] == '動詞':
                verb_base_set.add(word['base'])

    return verb_base_set
