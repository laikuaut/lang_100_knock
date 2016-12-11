# coding: utf-8

from .mecab_read import read_mecab_data

def Q_035():
    """ 35. 名詞の連接
    名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
    """

    data = read_mecab_data('data/neko.txt.mecab')
    noun_phrase_set = set()
    for sent in data:
        pos = 0
        while (pos != len(sent)):
            word_list = []
            for word in sent[pos:len(sent)]:
                pos += 1
                if word['pos'] == '名詞':
                    word_list.append(word)
                else:
                    break
            if len(word_list) > 1:
                noun_phrase_set.add(' '.join([word['surface'] for word in word_list]))

    return noun_phrase_set

