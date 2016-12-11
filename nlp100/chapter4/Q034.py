# coding: utf-8

from .mecab_read import read_mecab_data

def Q_034():
    """ 34. 「AのB」
    2つの名詞が「の」で連結されている名詞句を抽出せよ．
    """

    data = read_mecab_data('data/neko.txt.mecab')
    noun_phrase_set = set()
    for sent in data:
        ngram_3_list = ngram(sent, 3)
        for ngram_3 in ngram_3_list:
            if ngram_3[0]['pos'] == '名詞' and \
               ngram_3[1]['surface'] == 'の' and \
               ngram_3[2]['pos'] == '名詞':
                   noun_phrase_set.add(' '.join([word['surface'] for word in ngram_3]))

    return noun_phrase_set

def ngram(input, n):
    """ Ngram取得
    入力変数を指定のgram数でngramリストを作成する
    """
    last = len(input) - n + 1
    return [input[i:i+n] for i in range(0, last)]
